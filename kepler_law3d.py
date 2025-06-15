import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
npoints = 2500    # Number of time steps
dt = 0.05         # Time step in years
max_time = 30     # Set a maximum time limit for simulation

# Initialize time and position of the planet (in AU)
t = 0             # Initial time
x = 1             # Initial x position (AU)
y = 0             # Initial y position (AU)
z = 0             # Initial z position (AU) for 3D

# Initialize velocity of the planet (in AU per year)
v_x = 0           # Initial velocity in x direction (AU/year)
v_y = 8           # Initial velocity in y direction (AU/year)
v_z = 0           # Initial velocity in z direction (AU/year)

# Prepare for 3D plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(0, 0, 0, color='yellow', s=100)  # Sun at the origin
ax.set_xlabel('X (AU)')
ax.set_ylabel('Y (AU)')
ax.set_zlabel('Z (AU)')
ax.set_title("3D Planetary Orbit Simulation")

# Initialize arrays to store coordinates
x_vals = [x]
y_vals = [y]
z_vals = [z]

# Loop over the time steps
for step in range(npoints):
    # Calculate the distance (radius) from the planet to the Sun
    radius = np.sqrt(x**2 + y**2 + z**2)
    
    # Runge-Kutta method for the y direction
    y_dash = y + 0.5 * v_y * dt
    v_y_dash = v_y - 0.5 * (4 * np.pi**2 * y * dt) / (radius**3)
    y_new = y + v_y_dash * dt
    v_y_new = v_y - (4 * np.pi**2 * y_dash * dt) / (radius**3)
    
    # Runge-Kutta method for the x direction
    x_dash = x + 0.5 * v_x * dt
    v_x_dash = v_x - 0.5 * (4 * np.pi**2 * x * dt) / (radius**3)
    x_new = x + v_x_dash * dt
    v_x_new = v_x - (4 * np.pi**2 * x_dash * dt) / (radius**3)

    # Runge-Kutta method for the z direction (assuming no force acts in z direction)
    z_new = z + v_z * dt
    
    # Store the new positions
    x_vals.append(x_new)
    y_vals.append(y_new)
    z_vals.append(z_new)
    
    # Update the plot in real-time
    ax.plot(x_vals, y_vals, z_vals, color='black')
    
    # Update velocities and positions for the next step
    v_x = v_x_new
    v_y = v_y_new
    x = x_new
    y = y_new
    z = z_new
    t += dt  # Update time

    # Check if maximum time is reached
    if t >= max_time:
        print("Simulation stopped: Maximum time reached.")
        break

plt.show()  # Display the final plot
