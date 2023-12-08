# libs
import cv2
import numpy as np
import holostic as holostic
import imgpro as ip
import csv
import serial
import time

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense


ser = serial.Serial('/dev/tty.usbmodem142301', 9600, timeout=1)
time.sleep(2)

with open('model/newlabelstrain.csv', newline='') as f:
    reader = csv.reader(f)
    data = [row[0] for row in reader]



actions = np.array(data)
model = Sequential()  # instantiating the model
model.add(LSTM(64, return_sequences=True, activation='relu', input_shape=(30, 63)))
model.add(LSTM(128, return_sequences=True, activation='relu'))
model.add(LSTM(64, return_sequences=False, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(actions.shape[0], activation='softmax'))

model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])
model.load_weights('model/action.h5')
sequence = []
sentence = []
threshold = 0.7



# Initialize the video stream
cap = cv2.VideoCapture(0)

with holostic.mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
        # Read the frame from the video stream
        ret, frame = cap.read()
        image, results = holostic.mediapipe_detection(frame, holistic)
        holostic.draw_styled_landmarks(image, results)
        right_hand_coords = holostic.get_hand_landmarks(results)




        bulbs = ip.detect_bulbs(image)

        image = ip.draw_boxes(image, bulbs)

        image = cv2.flip(image, 1)

        # prediction logic
        keypoints = holostic.extract_keypoints(results)
        sequence.insert(0, keypoints)
        sequence = sequence[:30]
        if len(sequence) == 30:
            res = model.predict(np.expand_dims(sequence, axis=0))[0]
            if res[np.argmax(res)] > threshold:
                gesture = actions[np.argmax(res)]
                print(gesture)
                try:
                    if right_hand_coords[0] < holostic.get_distance():
                        if gesture == "on":
                            ser.write(b'2')
                        elif gesture == "off":
                            ser.write(b'1')
                        else: pass

                    else:
                        if gesture == "on":
                            ser.write(b'4')
                        elif gesture == "off":
                            ser.write(b'3')
                        else: pass
                except Exception as e:
                    pass

        # show to screen
        cv2.imshow('OpenCV Freed', image)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()

