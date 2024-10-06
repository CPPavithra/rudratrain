import serial
import time
import tkinter as tk

# Attempt to create a serial connection
try:
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    print(f"Connected to {ser.portstr}")
except serial.SerialException as e:
    print(f"Error: {e}")
    exit(1)

def send_command(command):
    try:
        command_byte = bytes([command])
        ser.write(command_byte)
        print(f"Command sent: {command} (0x{command:02X})")  # Show command in hex for clarity
    except Exception as e:
        print(f"Failed to send command: {e}")

# Motor control functions
def forward():
    global direction
    direction = "forward"
    print("Moving forward with real-time speed")
    send_command(64 + current_speed)
    send_command(192 + current_speed)

def backward():
    global direction
    direction = "backward"
    print("Moving backward with real-time speed")
    send_command(64 - current_speed)
    send_command(192 - current_speed)

def left():
    global direction
    direction = "left"
    print("Turning left with real-time speed")
    send_command(64 - current_speed)
    send_command(192 + current_speed)

def right():
    global direction
    direction = "right"
    print("Turning right with real-time speed")
    send_command(64 + current_speed)
    send_command(192 - current_speed)

def stop():
    global direction
    direction = None
    print("Stopping motors")
    send_command(64)  # Stop motor 1
    send_command(192)  # Stop motor 2

def update_speed(value):
    global current_speed
    current_speed = int(value)  # Convert the slider value to an integer
    print(f"Real-time speed updated to {current_speed}")
    
    # Automatically send the command based on the current direction
    if direction == "forward":
        send_command(64 + current_speed)
        send_command(192 + current_speed)
    elif direction == "backward":
        send_command(64 - current_speed)
        send_command(192 - current_speed)
    elif direction == "left":
        send_command(64 - current_speed)
        send_command(192 + current_speed)
    elif direction == "right":
        send_command(64 + current_speed)
        send_command(192 - current_speed)

def quit_program():
    stop()  # Use stop() to halt the motors before quitting
    ser.close()
    root.quit()

# Create the Tkinter window
root = tk.Tk()
root.title("Motor Control with Real-Time Speed Control")

# Global variables for direction and speed
direction = None
current_speed = 32  # Initialize speed at a mid value

# Create control buttons
forward_button = tk.Button(root, text="Forward (W)", command=forward, width=15, height=2)
backward_button = tk.Button(root, text="Backward (S)", command=backward, width=15, height=2)
left_button = tk.Button(root, text="Left (A)", command=left, width=15, height=2)
right_button = tk.Button(root, text="Right (D)", command=right, width=15, height=2)
stop_button = tk.Button(root, text="Stop", command=stop, width=15, height=2)
quit_button = tk.Button(root, text="Quit (Q)", command=quit_program, width=15, height=2)

# Create a real-time speed control slider
speed_slider = tk.Scale(root, from_=1, to=63, orient=tk.HORIZONTAL, label="Speed", length=300, command=update_speed)
speed_slider.set(current_speed)  # Set initial value of the slider

# Layout the buttons and slider in a grid
forward_button.grid(row=0, column=1, padx=10, pady=10)
left_button.grid(row=1, column=0, padx=10, pady=10)
stop_button.grid(row=1, column=1, padx=10, pady=10)
right_button.grid(row=1, column=2, padx=10, pady=10)
backward_button.grid(row=2, column=1, padx=10, pady=10)
quit_button.grid(row=3, column=1, padx=10, pady=10)
speed_slider.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

# Run the Tkinter main loop
root.mainloop()

