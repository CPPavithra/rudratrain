import numpy as np
import matplotlib.pyplot as plt
import random

# PID Controller Parameters
Kp = 1.0
Ki = 0.5
Kd = 0.2

# Simulation Parameters
dt = 0.01  # Sampling time
simulation_time = 10  # Simulation duration
target_angle = 90  # Target angle (degrees)

# Initialize variables
angle = 0  # Initial angle
error = 0
integral = 0
derivative = 0
previous_error = 0
integral_limit = 5
# Create lists to store data for plotting
time_steps = []
actual_angles = []
noisy_angles = []
corrected_angles = []

# Simulation loop
for t in np.arange(0, simulation_time, dt):
    # Calculate error
    error = target_angle - angle

    # Calculate integral
    integral += error * dt
    integral = np.clip(integral, -integral_limit, integral_limit)
    # Calculate derivative
    derivative = (error - previous_error) / dt

    # Calculate PID output
    output = Kp * error + Ki * integral + Kd * derivative
    # Add Gaussian noise to the angle
    noisy_angle = angle + random.gauss(0, 1)  # Adjust standard deviation as needed

    # Update angle based on output
    angle += output * dt
    angle = np.clip(angle, 0, 90)
    # Store data for plotting
    time_steps.append(t)
    actual_angles.append(angle)
    noisy_angles.append(noisy_angle)
    corrected_angles.append(angle)

    # Update previous error for derivative calculation
    previous_error = error
    
    print(f"Time: {t:.2f} s")
    print(f"Error: {error:.2f}")
    print(f"Integral: {integral:.2f}")
    print(f"Derivative: {derivative:.2f}")
    print(f"Output: {output:.2f}")
    print(f"Actual Angle: {angle:.2f} degrees")
    print(f"Noisy Angle: {noisy_angle:.2f} degrees")
    print(f"Corrected Angle: {angle:.2f} degrees")
    print()

# Plotting
plt.figure(figsize=(12, 6))

# Plot target angle
plt.axhline(y=target_angle, color='g', linestyle='-', label='Target Angle')

# Plot actual angle with noise
plt.plot(time_steps, noisy_angles, color='b', linestyle='-', label='Actual Angle with Noise')

# Plot corrected angle
plt.plot(time_steps, corrected_angles, color='r', linestyle='-', label='Corrected Angle')

plt.xlabel('Time (s)')
plt.ylabel('Angle (degrees)')
plt.title('PID Controller with Gaussian Noise')
plt.legend()
plt.grid(True)
plt.show()
