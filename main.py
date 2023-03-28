# libs
import cv2
import numpy as np
import holostic as holostic
import imgpro as ip


# test

# local
import yolo as yolo

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

        # show to screenq
        cv2.imshow('OpenCV Freed', image)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()

