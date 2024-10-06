import serial
import time
import tkinter as tk

try:
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)  
    print(f"Connected to {ser.portstr}")  
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
def forward():
    s=speed_slider.get()
    print("Forward")
    send_command(64 + s)  
    send_command(192 + s)  

def backward():
    s=speed_slider.get()
    print("Backward")
    send_command(64 - s)  
    send_command(192 - s)  

def left():
    s=speed_slider.get()
    print("Left")
    send_command(64 - s)  
    send_command(192 + s)  

def right():
    s=speed_slider.get()
    print("Right")
    send_command(64 + s)  
    send_command(192 - s)  

def stop():
    print("Stop")
    send_command(64)  
    send_command(192)  

def quit_program():
    stop_motors()
    ser.close()
    root.quit()

root = tk.Tk()
root.title("Speed Slider")

forward_button = tk.Button(root, text="Forward (W)", command=forward, width=15, height=2)
backward_button = tk.Button(root, text="Backward (S)", command=backward, width=15, height=2)
left_button = tk.Button(root, text="Left (A)", command=left, width=15, height=2)
right_button = tk.Button(root, text="Right (D)", command=right, width=15, height=2)
stop_button = tk.Button(root, text="Stop", command=stop, width=15, height=2)
quit_button = tk.Button(root, text="Quit (Q)", command=quit_program, width=15, height=2)

# Create a speed control slider
speed_slider = tk.Scale(root, from_=1, to=63, orient=tk.HORIZONTAL, label="Speed", length=300)
speed_slider.set(0)  


# Layout the buttons and slider in a grid
forward_button.grid(row=0, column=1, padx=10, pady=10)
left_button.grid(row=1, column=0, padx=10, pady=10)
stop_button.grid(row=1, column=1, padx=10, pady=10)
right_button.grid(row=1, column=2, padx=10, pady=10)
backward_button.grid(row=2, column=1, padx=10, pady=10)
quit_button.grid(row=3, column=1, padx=10, pady=10)
speed_slider.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

