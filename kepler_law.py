#Script by Alfian Herdiyanto
#Theoretical PHYSICS STUDENT 

import numpy as np
import matplotlib.pyplot as plt

# Constants
npoints = 2500    # Number of time steps
dt = 0.05         # Time step in years
max_time = 20      # Set a maximum time limit for simulation

# Initialize time and position of the planet (in AU)
t = 0             # Initial time
x = 1             # Initial x position (AU)
y = 0             # Initial y position (AU)

# Initialize velocity of the planet (in AU per year)
v_x = 0           # Initial velocity in x direction (AU/year)
v_y = 8           # Initial velocity in y direction (AU/year)

# Plot the Sun at the origin
plt.plot(0, 0, 'oy', markersize=30, markerfacecolor='yellow')  # Sun as a yellow circle
plt.xlabel('x (AU)')
plt.ylabel('y (AU)')
plt.title("Planetary Orbit Simulation")
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.ion()  # Enable interactive mode for real-time plotting

# Initialize arrays to store x and y coordinates
x_vals = [x]
y_vals = [y]

# Loop over the time steps with a break condition
for step in range(npoints):
    # Calculate the distance (radius) from the planet to the Sun
    radius = np.sqrt(x**2 + y**2)
    
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
    
    # Store the new positions
    x_vals.append(x_new)
    y_vals.append(y_new)
    
    # Update the plot in real-time
    plt.plot(x_vals, y_vals, '-k')
    plt.draw()
    plt.pause(0.01)  # Pause to simulate real-time plotting
    
    # Update velocities and positions for the next step
    v_x = v_x_new
    v_y = v_y_new
    x = x_new
    y = y_new
    t += dt  # Update time

    # Check if maximum time is reached
    if t >= max_time:
        print("Simulation stopped: Maximum time reached.")
        break

plt.ioff()  # Turn off interactive mode
plt.show()  # Display the final plot