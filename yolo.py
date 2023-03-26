import cv2
import numpy as np
import json

def detect_objects():
    # Load the pre-trained YOLOv3 model
    model_weights = "yolov3.weights"
    model_config = "yolov3.cfg"
    net = cv2.dnn.readNetFromDarknet(model_config, model_weights)

    # Define the classes of objects that the model can detect
    classes = []
    with open("coco.names", "r") as f:
        classes = [line.strip() for line in f.readlines()]

    # Set the input size of the model
    input_size = (416, 416)

    # Initialize the video stream and start looping over frames from the video stream
    cap = cv2.VideoCapture(0)

    # Initialize variables to store object detection results
    num_objects = 0
    object_data = []

    while True:
        # Read the frame from the video stream
        ret, frame = cap.read()

        # Convert the frame to a blob
        blob = cv2.dnn.blobFromImage(frame, 1/255, input_size, swapRB=True, crop=False)

        # Set the input of the model to the blob
        net.setInput(blob)

        # Run the model forward and get the output
        output_layers = net.getUnconnectedOutLayersNames()
        layer_outputs = net.forward(output_layers)

        # Process the output and draw the boxes around the detected objects
        boxes = []
        confidences = []
        class_ids = []
        for output in layer_outputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    center_x = int(detection[0] * frame.shape[1])
                    center_y = int(detection[1] * frame.shape[0])
                    w = int(detection[2] * frame.shape[1])
                    h = int(detection[3] * frame.shape[0])
                    x = int(center_x - w/2)
                    y = int(center_y - h/2)
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        # Apply non-maximum suppression to remove redundant boxes
        indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

        # Draw the boxes around the detected objects and show the output
        if len(indices) > 0:
            for i in indices.flatten():
                x, y, w, h = boxes[i]
                label = classes[class_ids[i]]
                confidence = confidences[i]
                color = (255, 0, 0)
                cv2.rectangle(frame, (x, y), (x+w, y+h), color, 3)
                cv2.putText(frame, f"{label}: {confidence:.2f}", (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

                # Update object detection results
                num_objects += 1
                object_data.append({"name": label, "x": x, "y": y, "w": w, "h": h})

        cv2.imshow("Object Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        # num_objects = len(indices)  
        # print(num_objects)  
        json_string = json.dumps(object_data)
        # print(json_string)
    # Release the video stream and close all windows
    cap.release()
    cv2.destroyAllWindows()
    return num_objects, json_string

# # Call the function to detect objects and check if any object is detected
# for object_detected in detect_objects():
#     if object_detected:
#         print("Object detected!")
#     else:
#         print("No object detected.")
a,b=detect_objects()
print(a,b)