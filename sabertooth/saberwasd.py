import serial
import time
import keyboard

# Attempt to create a serial connection
try:
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)  # Adjust as needed
    print(f"Connected to {ser.portstr}")  # Confirm connection
except serial.SerialException as e:
    print(f"Error: {e}")
    exit(1)

def send_command(command):
    try:
        # Ensure command is sent as a single byte
        command_byte = bytes([command])
        ser.write(command_byte)
        print(f"Command sent: {command} (0x{command:02X})")  # Show command in hex for clarity
    except Exception as e:
        print(f"Failed to send command: {e}")

# Motor control instructions
print("Control the motors with W/A/S/D keys. Press 'Q' to quit.")

while True:
    if keyboard.is_pressed('w'):  # Move both motors forward
        print("Moving forward")
        send_command(64 + 30)  # Move motor 1 forward
        send_command(192 + 30)  # Move motor 2 forward
        time.sleep(0.5)  # Short delay to avoid sending too many commands
        
    elif keyboard.is_pressed('s'):  # Move both motors backward
        print("Moving backward")
        send_command(64 - 30)  # Move motor 1 backward
        send_command(192 - 30)  # Move motor 2 backward
        time.sleep(0.5)
        
    elif keyboard.is_pressed('a'):  # Turn left
        print("Turning left")
        send_command(64 - 30)  # Motor 1 backward
        send_command(192 + 30)  # Motor 2 forward
        time.sleep(0.5)
        
    elif keyboard.is_pressed('d'):  # Turn right
        print("Turning right")
        send_command(64 + 30)  # Motor 1 forward
        send_command(192 - 30)  # Motor 2 backward
        time.sleep(0.5)

    elif keyboard.is_pressed('t'):
        send_command(64)
        send_command(192)
        time.sleep(1)

    elif keyboard.is_pressed('q'):  # Quit the program
        print("Quitting...")
        break
    
    # Wait for a short time to avoid high CPU usage
    time.sleep(0.1)

# Stop the motors when quitting
send_command(64)  # Stop motor 1
send_command(192)  # Stop motor 2
ser.close()
print("Connection closed.")

