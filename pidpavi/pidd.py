import random

class PID:
    def __init__(self, Kp, Ki, Kd, set_point):
        self.Kp = Kp  # Proportional gain
        self.Ki = Ki  # Integral gain
        self.Kd = Kd  # Derivative gain
        self.set_point = set_point
        self.previous_error = 0
        self.integral = 0

    def compute(self, current_angle):
        error = self.set_point - current_angle
        self.integral += error
        derivative = error - self.previous_error
        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        self.previous_error = error
        return output

# Parameters
initial_angle = 0
target_angle = 90
increment = 1
error_step = 50  # Introduce fixed error at 50 degrees
fixed_error_value = 5  # Fixed error of 5 degrees

# Gaussian noise parameters
mu = 0
sigma = 2

Kp = 1.0
Ki = 0.1
Kd = 0.05

pid_controller = PID(Kp, Ki, Kd, target_angle)

for step in range(0, target_angle + increment, increment):
    # Introduce fixed error at the error step
    current_angle = step + (fixed_error_value if step >= error_step else 0)

    # Add Gaussian noise to the current angle
    gaussian_noise = random.gauss(mu, sigma)
    current_angle_with_noise = current_angle + gaussian_noise

    # Ensure the actual angle remains between 0 and 90
    current_angle_with_noise = max(0, min(90, current_angle_with_noise))

    # Apply PID correction
    pid_output = pid_controller.compute(current_angle_with_noise)

    # Calculate the corrected angle
    corrected_angle = current_angle_with_noise + pid_output

    # Ensure the corrected angle remains between 0 and 90
    corrected_angle = max(0, min(90, corrected_angle))

    # Print the values for each step
    print(f"Step: {step} degrees")
    print(f"Actual Angle with Noise: {current_angle_with_noise:.2f} degrees")
    print(f"PID Output: {pid_output:.2f}")
    print(f"Corrected Angle: {corrected_angle:.2f} degrees")
    print('-' * 40)

