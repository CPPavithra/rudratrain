import serial
import time

# Open the serial port (change '/dev/ttyUSB0' to your actual port)
ser = serial.Serial('/dev/ttyUSB0', 9600)
ser.timeout = 1

try:
    while True:
        # Move forward
        forward_speed = 60  # Speed from 1 to 127
        print(f"Sending forward speed: {forward_speed}")
        ser.write(bytes([forward_speed]))  # Send as byte
        time.sleep(2)

        # Stop
        print("Sending stop command")
        ser.write(bytes([0]))  # Stop
        time.sleep(2)

        # Move backward
        backward_speed = 60  # Speed from 1 to 127
        print(f"Sending backward speed: {backward_speed + 128}")
        ser.write(bytes([backward_speed + 128]))  # Send as byte
        time.sleep(2)

        # Stop
        print("Sending stop command")
        ser.write(bytes([0]))  # Stop
        time.sleep(2)

except KeyboardInterrupt:
    print("Program interrupted.")

finally:
    ser.close()  # Close the serial port when done

