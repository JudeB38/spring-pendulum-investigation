import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

mu = 2
mass = 1

def get_theta2dot(a, b):
    return -9.8*np.sin(a) - (mu / mass)*b

gamma = np.array([2., -3.])

max_t = 10
dt = 0.01
t = 0
theta_points, thetad_points = [], []
while t <= max_t:
    theta_points.append(gamma[0])
    thetad_points.append(gamma[1])

    #print(f"{gamma[0]:.2}, {gamma[1]:.2}")

    gamma = gamma + dt*np.array([gamma[1], get_theta2dot(gamma[0], gamma[1])])

    t += dt
    

x, y = np.meshgrid(np.linspace(-7, 7, 70), np.linspace(-5, 5, 70))
u, v = y, get_theta2dot(x, y)
c = np.sqrt(u**2 + v**2)

plt.quiver(x, y, u/c, v/c, c, cmap='gnuplot2')
plt.colorbar()
plt.plot(theta_points, thetad_points, lw='4', color='black')
plt.show()