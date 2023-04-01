# libs
import cv2
import numpy as np
import holostic as holostic
import imgpro as ip
import csv

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense


with open('model/newlabelstrain.csv', newline='') as f:
    reader = csv.reader(f)
    data = [row[0] for row in reader]



actions = np.array(data)
model = Sequential()  # instantiating the model
model.add(LSTM(64, return_sequences=True, activation='relu', input_shape=(30, 126)))
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

        bulbs = ip.detect_bulbs(image)

        image = ip.draw_boxes(image, bulbs)




        # prediction logic
        keypoints = holostic.extract_keypoints(results)
        sequence.insert(0, keypoints)
        sequence = sequence[:30]
        if len(sequence) == 30:
            res = model.predict(np.expand_dims(sequence, axis=0))[0]
            print(actions[np.argmax(res)])
            if res[np.argmax(res)] > threshold:
                print(res[np.argmax(res)])
                if len(sentence) > 0:
                    if actions[np.argmax(res)] != sentence[-1]:
                        sentence.append(actions[np.argmax(res)])
                else:
                    sentence.append(actions[np.argmax(res)])

            if len(sentence) > 5:
                sentence = sentence[-5:]

            cv2.rectangle(image, (0, 0), (1920, 40), (245, 117, 16), -1)
            cv2.putText(image, ' '.join(sentence), (3, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2,
                        cv2.LINE_AA)

        # show to screen
        cv2.imshow('OpenCV Freed', image)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()

