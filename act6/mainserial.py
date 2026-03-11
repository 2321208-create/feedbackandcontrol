import serial
import time

arduino = serial.Serial(port='COM5', baudrate=9600, timeout=1)
time.sleep(2)

while True:
    command = input("Enter 1 to turn ON LED, 0 to turn OFF LED, q to quit: ")

    if command == '1':
        arduino.write(b'1')
    elif command == '0':
        arduino.write(b'0')
    elif command == 'q':
        break
    else:
        print("Invalid command")

arduino.close()