import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, TextBox

x0 = 0
y0 = 0.4

# Initial velocity and launch angle
initial_velocity = 12  # m/s
launch_angle = 32  # degrees


def projectile_motion(v0, x0, y0, angle_deg, g=9.81, steps=50):
    angle_rad = np.deg2rad(angle_deg)
    a = -0.5 * g
    b = v0 * np.sin(angle_rad)
    c = y0
    t_flight = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    t = np.linspace(0, t_flight, steps)

    x = x0 + v0 * np.cos(angle_rad) * t
    y = y0 + v0 * np.sin(angle_rad) * t - 0.5 * g * t ** 2

    return x, y


# Calculate trajectory
x_values, y_values = projectile_motion(initial_velocity, 0, 0.4, launch_angle)

# Create the figure and axes
fig, ax = plt.subplots(figsize=(6, 4))
plt.subplots_adjust(bottom=0.35, left=0.1, right=0.9)  # Adjust margins for the widgets

# Plot the projectile motion trajectory as dots
trajectory_dots, = ax.plot(x_values, y_values, marker='o', linestyle='', markersize=4, color='blue',
                           label='Projectile Motion')

# Customize the plot
ax.set_title('Frisbee Launching Sim')
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.grid()
ax.legend()
# Set the grid limits for x and y axes
ax.set_xlim(0, 10)
ax.set_ylim(0, 3)

# Slider for launch angle
angle_slider_ax = plt.axes([0.24, 0.2, 0.65, 0.03])  # [left, bottom, width, height]
angle_slider = Slider(angle_slider_ax, 'Launch Angle (deg)', 0, 90, valinit=launch_angle)

# Text box for x0
x0_slider_ax = plt.axes([0.05, 0.1, 0.2, 0.03])
x0_slider = Slider(x0_slider_ax, 'x0  ', 0, 6, valinit=x0)

# Text box for y0
y0_slider_ax = plt.axes([0.37, 0.1, 0.2, 0.03])
y0_slider = Slider(y0_slider_ax, 'y0:', 0, 0.9, valinit=y0)

# Text box for v0
initial_velocity_slider_ax = plt.axes([0.7, 0.1, 0.2, 0.03])
initial_velocity_slider = Slider(initial_velocity_slider_ax, 'v0:', 5, 15, valinit=initial_velocity)

# Marked points
points = [(7.2, 1.4), (8.2, 1.8), (9.2, 2.2)]
x_coords = [point[0] for point in points]
y_coords = [point[1] for point in points]
ax.plot(x_coords, y_coords, 'o', color='red', markersize=8, label='Marked Points')

ax.axvline(x=6, color='green', linestyle='-', label='Vertical Line at x=6')
ax.plot([7.2, 7.2], [0, 1.4], color='purple', linestyle='-', label='Line Segment')  # 籃框
ax.plot([8.2, 8.2], [0, 1.8], color='purple', linestyle='-', label='Line Segment')  # 籃框
ax.plot([9.2, 9.2], [0, 2.2], color='purple', linestyle='-', label='Line Segment')  # 籃框


# Update function for slider and text boxes
def update(val):
    new_angle = angle_slider.val
    new_x0 = float(x0_slider.val)
    new_y0 = float(y0_slider.val)
    new_initial_velocity = float(initial_velocity_slider.val)
    x_vals, y_vals = projectile_motion(new_initial_velocity, new_x0, new_y0, new_angle)
    trajectory_dots.set_data(x_vals, y_vals)
    fig.canvas.draw_idle()


angle_slider.on_changed(update)  # Connect slider to update function
x0_slider.on_changed(update)  # Connect text box to update function
y0_slider.on_changed(update)  # Connect text box to update function
initial_velocity_slider.on_changed(update)

# Show the plot
plt.show()
