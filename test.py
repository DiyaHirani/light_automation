import serial
import time

# Open serial connection to Arduino
ser = serial.Serial('/dev/tty.usbmodem142301', 9600, timeout=1)

# Wait for serial connection to be established
time.sleep(2)

# Loop to read user input and send commands to Arduino
while True:
    # Read user input
    cmd = input("Enter command (1 or 2): ")

    # Send command to Arduino
    if cmd == '1':
        ser.write(b'1')
        print("Bulb 1 turned on.")
    elif cmd == '2':
        ser.write(b'2')
        print("Bulb 1 turned off.")
    elif cmd == '3':
        ser.write(b'3')
        print("Bulb 2 turned on.")
    elif cmd == '4':
        ser.write(b'4')
        print("Bulb 2 turned off.")
    else:
        print("Invalid command. Please enter 1, 2, 3 or 4.")
