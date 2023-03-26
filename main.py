# libs
import cv2
import numpy as np


# local
import yolo as yolo

# Initialize the video stream
cap = cv2.VideoCapture(0)

while True:
    # Read the frame from the video stream
    ret, frame = cap.read()

    # Detect objects in the frame
    object_data = yolo.detect_objects(frame)

    # Show the output
    cv2.imshow("Object Detection", frame)
    print(object_data)
    # Check if the user wants to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


