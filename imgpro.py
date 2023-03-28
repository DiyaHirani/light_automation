import cv2
import numpy as np

def detect_bulbs(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply a threshold to the image
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours by area and circularity to find potential bulbs
    bulbs = []
    for contour in contours:
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)
        try:
            circularity = 4 * np.pi * (area / (perimeter ** 2))
        except Exception as e:
            circularity = 0
        if area > 500 and circularity > 0.3:
            # Calculate the centroid of the contour and add it to the list of potential bulbs
            M = cv2.moments(contour)
            x = int(M["m10"] / M["m00"])
            y = int(M["m01"] / M["m00"])
            bulbs.append((x, y))

    # Return the list of potential bulbs
    return bulbs


def draw_boxes(frame, bulbs):
    # Draw bounding boxes around the detected bulbs
    box_radius = 40
    for (x, y) in bulbs:
        cv2.rectangle(frame, (x-box_radius, y-box_radius), (x+box_radius, y+box_radius), (0, 255, 0), 5)

    # Return the frame with the boxes drawn
    return frame

