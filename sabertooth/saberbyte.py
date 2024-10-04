# Simulated Serial Communication for Sabertooth 2x60

import time
import serial

# Set the serial port to your CP210x device
#SERIAL_PORT = '/dev/ttyUSB0'  # Change this to your actual port
#BAUD_RATE = 9600

To connect the Sabertooth 2x60 motor driver to your Silicon Labs CP210x UART Bridge and control it using Python, you’ll need to follow a few steps. Here’s a detailed guide:

### **1. Wiring the Sabertooth 2x60**
Before you can run the motor, ensure that your wiring is correct.

1. **Connect Power:**
   - Connect the appropriate power supply to the Sabertooth. The power supply should match the voltage rating for your motors (typically 6V to 30V).

2. **Connect Motors:**
   - Connect your DC motors to the output terminals on the Sabertooth (M1 and M2).

3. **Connect the Serial Port:**
   - Connect the **CP210x UART Bridge** to the **S1** terminal on the Sabertooth. This is usually done by:
     - **TX** (from CP210x) to **S1 RX** (on Sabertooth).
     - **RX** (from CP210x) to **S1 TX** (on Sabertooth).
     - **GND** (from CP210x) to **GND** (on Sabertooth).
   - If the CP210x is being powered from USB, ensure that the ground is shared with the Sabertooth.

### **2. Python Code to Control the Sabertooth**
Below is a Python script you can use to control the Sabertooth 2x60 in simplified serial mode. This example assumes you have already connected your CP210x to your computer and identified the port (like `/dev/ttyUSB0`).

```python
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
    print("Program interrupted.")`

finally:
    ser.close()  # Close the serial port when done
```

### **3. Running the Code**
1. **Install Python Serial Library:**
   If you haven't installed the `pyserial` library yet, you can do so using pip:

   ```bash
   pip install pyserial
   ```

2. **Run the Script:**
   Open a terminal and navigate to the directory where your script is saved. Then run the script with:

   ```bash
   python your_script_name.py
   ```

### **4. Verify Everything is Working**
- Make sure the power supply is connected to the Sabertooth and that the motors are wired correctly.
- The code will make the motors move forward for 2 seconds, stop for 2 seconds, move backward for 2 seconds, and then stop again in a loop. You should hear the motors running and see the output in the terminal.

### **5. Troubleshooting**
- If the motors do not run, check the following:
  - Ensure all connections are secure.
  - Verify that the correct serial port is specified in the script.
  - Check that the power supply to the Sabertooth is adequate.
  - Monitor the terminal for any error messages and resolve them accordingly.

By following these steps, you should be able to successfully connect and control the Sabertooth 2x60 motor driver     print(f"Sending command: {command}")

try:
    while True:
        # Send command to move forward
        forward_speed = 60  # Speed from 1 to 127
        print(f"Sending forward speed: {forward_speed}")
        send_command(bytes([forward_speed]))  # Simulated send as byte
        time.sleep(2)

        # Send command to stop
        print("Sending stop command")
        send_command(bytes([0]))  # Simulated stop
        time.sleep(2)

        # Send command to move backward
        backward_speed = 60  # Speed from 1 to 127
        print(f"Sending backward speed: {backward_speed + 128}")
        send_command(bytes([backward_speed + 128]))  # Simulated send as byte
        time.sleep(2)

        # Send command to stop
        print("Sending stop command")
        send_command(bytes([0]))  # Simulated stop
        time.sleep(2)

except KeyboardInterrupt:
    print("Program interrupted.")

finally:
    ser.close()  # Close the serial port when done
