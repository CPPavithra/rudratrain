import numpy as np
import matplotlib.pyplot as plt
import random

# PID controller class
class PID:
    def __init__(self, Kp, Ki, Kd, set_point):
        self.Kp = Kp  # Proportional gain
        self.Ki = Ki  # Integral gain
        self.Kd = Kd  # Derivative gain
        self.set_point = set_point  # Desired target angle
        self.previous_error = 0  # To store the last error value
        self.integral = 0  # To accumulate the sum of errors (for integral term)

    def compute(self, current_angle):
        error = self.set_point - current_angle  # Calculate the current error
        self.integral += error  # Accumulate the error for the integral term
        derivative = error - self.previous_error  # Calculate the change in error for the derivative term
        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative  # PID formula
        self.previous_error = error  # Store the current error for the next iteration
        return output  # Return the PID output

# Parameters
initial_angle = 0
target_angle = 90
increment = 1
error_step = 50  # Introduce fixed error at 50 degrees
fixed_error_value = 5  # Fixed error of 5 degrees

# Gaussian noise parameters
mu = 0   # Mean of the Gaussian distribution
sigma = 2  # Standard deviation for Gaussian noise

# PID controller parameters
Kp = 5.0
Ki = 0.1
Kd = 0.5

# Initialize the PID controller
pid_controller = PID(Kp, Ki, Kd, target_angle)

# Simulate time steps
time_steps = np.arange(0, target_angle + increment, increment)
actual_angles_with_noise = []
corrected_angles = []

# Simulate the system
for step in time_steps:
    # Introduce fixed error at the error step
    current_angle = step + (fixed_error_value if step >= error_step else 0)

    # Add Gaussian noise to the current angle
    gaussian_noise = random.gauss(mu, sigma)
    current_angle_with_noise = current_angle + gaussian_noise

    # Apply PID correction
    pid_output = pid_controller.compute(current_angle_with_noise)
    corrected_angle = current_angle_with_noise + pid_output

    # Store the actual noisy and corrected angles
    actual_angles_with_noise.append(current_angle_with_noise)
    corrected_angles.append(corrected_angle)

# Plotting the results
plt.figure(figsize=(12, 6))

plt.plot(time_steps, actual_angles_with_noise, label='Actual Angle with Noise', color='r', linestyle='--')
plt.plot(time_steps, corrected_angles, label='Corrected Angle by PID', color='b')

plt.title('Angle vs Time using PID Control')
plt.xlabel('Time (steps)')
plt.ylabel('Angle (degrees)')
plt.legend()
plt.grid(True)

# Set x and y-axis limits
plt.xlim(0, target_angle)  # X-axis limit from 0 to 90 degrees
plt.ylim(0, 90)  # Y-axis limit from 0 to 90 degrees

plt.show()

