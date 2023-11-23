# Media Pipe - Holistic Based Home Automation
## MediaPipe Holisitc approach

This project aims to create a smart lighting control system that allows users to control light bulbs using hand gestures.

This project allows users to control light bulbs using hand gestures captured by a webcam. The system uses the MediaPipe Holistic library to detect hand gestures, OpenCV to process images, and TensorFlow Keras and NumPy for machine learning and data analysis. The control of the light bulbs is implemented using an Arduino microcontroller connected to a relay that switches the bulbs on and off.

https://github.com/DiyaHirani/light_automation/assets/53598504/fc7629fe-6dcd-4677-89f9-0ea6703721f3

## Requirements

**Python** (version 3.6 or higher)

**OpenCV**

**MediaPipe**

**TensorFlow 2+**

**NumPy**

You will also need an Arduino board, a relay module, and a USB cable to connect the Arduino to your computer.


## Authors

Credits 

[Hirak Desai](https://www.github.com/hirak214)

[Diya Hirani](https://github.com/DiyaHirani)

[Yashvi Agrawal](https://github.com/yashviagrawal)


## Approach

- **Hand Detection:** Use MediaPipe and OpenCV to detect the user's hand and track its movements.

- **Bulb Detection:** Use image processing techniques to detect the location of the bulbs in the space. This involves finding the brightest pixels in the image and marking them as bulbs.

- **Gesture Detection:** Train a deep learning model to recognize hand gestures. The model will take as input a cropped image of the hand and output a predicted gesture.


- **Bulb Selection:** Use artificial intelligence to determine which bulb is being targeted by the user's hand. This can be done by analyzing the location of the hand relative to the positions of the bulbs.

- **Relay Activation:** Use an Arduino board and a relay module to activate the selected bulb. Using serial communication.


## Usage

To use the system, run the smart_lighting.py script. This will start the system and open a video stream showing the detected hand and bulbs. To control the bulbs, make one of the following gestures:

**Gestures**

* Fist: turn off the selected bulb
* Palm spread: turn on the selected bulb

To select a bulb, move your hand so that it is directly above the desired bulb. The system will automatically select the nearest bulb to your hand.


## Arduino

To connect the Arduino board to the system, follow these steps:

1. Connect the relay module to the Arduino board as follows:

* VCC pin to 5V pin on the Arduino board
* GND pin to GND pin on the Arduino board
* IN1 pin to digital pin 2 on the Arduino board
* IN2 pin to digital pin 3 on the Arduino board
* IN3 pin to digital pin 4 on the Arduino board
* IN4 pin to digital pin 5 on the Arduino board
2. Connect the USB cable to the Arduino board and your computer.
3. Run the smart_lighting.py script. The system will automatically detect the Arduino and establish a serial connection.


## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute the code as you see fit.
[MIT](https://choosealicense.com/licenses/mit/)

