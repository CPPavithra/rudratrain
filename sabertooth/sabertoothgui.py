import serial
import time
import tkinter as tk

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

# Motor control functions
def move_forward():
    print("Moving forward")
    send_command(64 + 30)  # Motor 1 forward
    send_command(192 + 30)  # Motor 2 forward

def move_backward():
    print("Moving backward")
    send_command(64 - 30)  # Motor 1 backward
    send_command(192 - 30)  # Motor 2 backward

def turn_left():
    print("Turning left")
    send_command(64 - 30)  # Motor 1 backward
    send_command(192 + 30)  # Motor 2 forward

def turn_right():
    print("Turning right")
    send_command(64 + 30)  # Motor 1 forward
    send_command(192 - 30)  # Motor 2 backward

def stop_motors():
    print("Stopping motors")
    send_command(64)  # Stop motor 1
    send_command(192)  # Stop motor 2

def quit_program():
    stop_motors()
    ser.close()
    root.quit()

# Create the tkinter window
root = tk.Tk()
root.title("Motor Control")

# Create buttons for motor control
forward_button = tk.Button(root, text="Forward (W)", command=move_forward, width=15, height=2)
backward_button = tk.Button(root, text="Backward (S)", command=move_backward, width=15, height=2)
left_button = tk.Button(root, text="Left (A)", command=turn_left, width=15, height=2)
right_button = tk.Button(root, text="Right (D)", command=turn_right, width=15, height=2)
stop_button = tk.Button(root, text="Stop", command=stop_motors, width=15, height=2)
quit_button = tk.Button(root, text="Quit (Q)", command=quit_program, width=15, height=2)

# Layout the buttons in a grid
forward_button.grid(row=0, column=1, padx=10, pady=10)
left_button.grid(row=1, column=0, padx=10, pady=10)
stop_button.grid(row=1, column=1, padx=10, pady=10)
right_button.grid(row=1, column=2, padx=10, pady=10)
backward_button.grid(row=2, column=1, padx=10, pady=10)
quit_button.grid(row=3, column=1, padx=10, pady=10)

# Run the tkinter event loop
root.mainloop()

