import numpy as np
import matplotlib.pyplot as plt

# Define physical parameters
l = 1       # Pendulum length in meters
g = 9.8     # Acceleration due to gravity in m/s^2
npoints = 250    # Number of time points for the simulation (intervals)
dt = 0.04   # Time step (iteration) in seconds

# Initialize variables
omega = np.zeros(npoints)
theta = np.zeros(npoints)
time = np.zeros(npoints)

# Set initial angular displacement
theta[0] = 0.2

# Enable interactive plotting
plt.ion()
fig, ax = plt.subplots()
line, = ax.plot([], [], 'r')  # Initial plot for the pendulum motion
ax.set_xlim(0, npoints * dt)
ax.set_ylim(-0.5, 0.5)
ax.set_xlabel('Time (seconds)')
ax.set_ylabel('Theta (radians)')
ax.set_title('Real-time Simple Pendulum Simulation using Euler Method')
ax.grid(True)

# Simulation loop with real-time plotting
for step in range(npoints - 1):
    omega[step + 1] = omega[step] - (g / l) * theta[step] * dt
    theta[step + 1] = theta[step] + omega[step] * dt
    time[step + 1] = time[step] + dt

    # Update the plot in real-time
    line.set_xdata(time[:step + 2])  # Update x values (time)
    line.set_ydata(theta[:step + 2])  # Update y values (theta)
    
    # Adjust limits dynamically (optional)
    ax.relim()
    ax.autoscale_view()

    plt.draw()  # Redraw the figure
    plt.pause(0.01)  # Pause to allow for real-time plotting

# Turn off interactive plotting and display the final result
plt.ioff()
plt.show()