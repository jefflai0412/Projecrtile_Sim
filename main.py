from tkinter import filedialog

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


def projectile_motion(v0, angle_deg, g=9.81, steps=100):
    angle_rad = np.deg2rad(angle_deg)
    t_flight = 2 * v0 * np.sin(angle_rad) / g
    t = np.linspace(0, t_flight, steps)

    x = v0 * np.cos(angle_rad) * t
    y = v0 * np.sin(angle_rad) * t - 0.5 * g * t ** 2

    return x, y


# Initial velocity and launch angle
initial_velocity = 20  # m/s
launch_angle = 45     # degrees

# Calculate trajectory
x_values, y_values = projectile_motion(initial_velocity, launch_angle)

# Plot the trajectory with an image background
plt.figure(figsize=(8, 6))

# Load an image
file_path = r"C:\Users\Jeff\OneDrive\桌面\fourfools.jpg"
img = plt.imread(file_path)  # Replace with the path to your image file

# Set up the plot with the image background
plt.imshow(img, extent=[0, max(x_values), 0, max(y_values)], aspect='auto')

# Plot the projectile motion trajectory on top of the image
plt.plot(x_values, y_values, color='red', label='Projectile Motion')

# Add image annotation (optional)
# imagebox = OffsetImage(img, zoom=0.15)
# ab = AnnotationBbox(imagebox, (max(x_values)*0.8, max(y_values)*0.6))
# plt.gca().add_artist(ab)

# Customize the plot
plt.title('Projectile Motion with Image Background')
plt.xlabel('Horizontal Distance (m)')
plt.ylabel('Vertical Distance (m)')
plt.grid()
plt.legend()

# Show the plot
plt.show()
