# import dependencies
import cv2
import mediapipe as mp
import numpy as np

# Key points using MP Holistic

mp_holistic = mp.solutions.holistic  # Holisitc Model
mp_drawing = mp.solutions.drawing_utils  # Drawing utilities


def mediapipe_detection(image, model):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # COLOR CONVERSION BGR 2 RGB
    image.flags.writeable = False  # image is no longer Writeable
    results = model.process(image)  # make prediciton
    image.flags.writeable = True  # image is now writeable
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # COLOR CONVERSION RGB 2 BGR
    return image, results


def extract_keypoints(results):
    # lh = np.array([[res.x, res.y, res.z] for res in results.left_hand_landmarks.landmark]).flatten() \
    #     if results.left_hand_landmarks else np.zeros(21 * 3)  # 63
    rh = np.array([[res.x, res.y, res.z] for res in results.right_hand_landmarks.landmark]).flatten() \
        if results.right_hand_landmarks else np.zeros(21 * 3)  # 63
    return np.concatenate([rh])

def draw_styled_landmarks(image, results):
    # # Draw Left Hand Connections
    # mp_drawing.draw_landmarks(image, results.left_hand_landmarks,
    #                           mp_holistic.HAND_CONNECTIONS,
    #                           mp_drawing.DrawingSpec(color=(121, 22, 76), thickness=1, circle_radius=1),
    #                           mp_drawing.DrawingSpec(color=(121, 44, 350), thickness=1, circle_radius=1))
    # Draw Right Hand Connections
    mp_drawing.draw_landmarks(image, results.right_hand_landmarks,
                              mp_holistic.HAND_CONNECTIONS,
                              mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=1, circle_radius=1),
                              mp_drawing.DrawingSpec(color=(245, 66, 230), thickness=1, circle_radius=1))

def get_hand_landmarks(results):
    # left_landmarks = results.left_hand_landmarks
    right_landmarks = results.right_hand_landmarks

    # left_hand_coords = []
    right_hand_coords = []

    # # Get x, y, z coordinates for each landmark of left hand
    # if left_landmarks is not None:
    #     for landmark in left_landmarks.landmark:
    #         left_hand_coords = [landmark.x, landmark.y, landmark.z]

    # Get x, y, z coordinates for each landmark of right hand
    if right_landmarks is not None:
        for landmark in right_landmarks.landmark:
            right_hand_coords = [landmark.x, landmark.y, landmark.z]

    return right_hand_coords


def get_distance():
    return 0.5
