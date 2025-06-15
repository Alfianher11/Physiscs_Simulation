import numpy as np
import matplotlib.pyplot as plt

#define parameter fisik

l = 1       #Ppanjang pandulum dalam meter
g = 9.8     #percepatan gravitasi dalam m/s^2
npoints = 250    #jumlah titik waktu untuk simulasi (interval)
dt = 0.04   #time step (iterasi) dalam detik

#define inisiasi variabel
omega = np.zeros(npoints)
theta = np.zeros(npoints)
time = np.zeros(npoints)

#set kecepatan sudut awal
theta[0] = 0.2

for step in range(npoints - 1):
    omega[step + 1] = omega[step] - (g/l) * theta[step] * dt
    theta[step + 1] = theta[step] + omega[step] * dt
    time[step + 1] = time[step] + dt
    
#plot hasil simulasi
plt.plot(time, theta, 'r')  # Plot sudut theta sebagai fungsi waktu
plt.xlabel('Time (seconds)')
plt.ylabel('Theta (radians)')
plt.title('Simple Pendulum Simulation using Euler Method')
plt.grid(True)
plt.show()