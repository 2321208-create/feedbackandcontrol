import serial
import time

SERIAL_PORT = 'COM5'
BAUD_RATE = 9600

def main():

    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)

    while True:

        angle = input("Enter angle (0-180): ")

        ser.write((angle + "\n").encode())

        print("Sent:", angle)

if __name__ == "__main__":
    main()