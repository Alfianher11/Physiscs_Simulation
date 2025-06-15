import numpy as np
import matplotlib.pyplot as plt

#  Euler_cromer calculation of motion of simple pendulum 
#  by Kevin Berwick, translated to python by alfian herdiyanto
#  based on 'Computational Physics' book by N Giordano and H Nakanishi

length = 1       #pendulum length in metres                                   
g = 9.8           #acceleration due to gravity       
npoints = 250   #Discretize time into 250 intervals 
dt = 0.04       # time step in seconds 
                    
omega = np.zeros(npoints)   # initializes omega, a vector of dimension npoints X 1,to being all zeros 
theta = np.zeros(npoints)   # initializes theta, a vector of dimension npoints X 1,to being all zeros  
time = np.zeros(npoints)    # this initializes the vector time to being all zeros  
theta[0] = 0.2                              

 
# you need to have some initial displacement, otherwise the pendulum will 
for step in range(npoints-1): 
    omega[step+1] = omega[step] - (g/length) * theta[step]*dt 
    theta[step+1] = theta[step] + omega[step+1]*dt    
    time[step+1] = time[step] + dt  

plt.plot(time,theta,'r' ) #plots the numerical solution in red  
plt.xlabel('time (seconds) ') 
plt.ylabel('theta (radians)') 
plt.title('Simple Pendulum Simulation using cromer Method')
plt.grid(True)
plt.show()