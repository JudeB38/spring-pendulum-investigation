import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anm
import ffmpeg

mu = 2
mass = 1

def get_theta2dot(a, b):
    return -9.8*np.sin(a) - (mu / mass)*b



x, y = np.meshgrid(np.linspace(-8, 8, 50), np.linspace(-4, 4, 50))
u, v = y, get_theta2dot(x, y)
c = np.sqrt(u**2 + v**2)



fig = plt.figure()
ax = plt.axes(xlim=(-8, 8), ylim=(-4, 4))
ax.quiver(x, y, u/c, v/c, c, cmap='gnuplot2')
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

global gamma
gamma = np.array([2., -3.])

dt = 0.01
t = 0
theta_points, thetad_points = [], [] 
def animate(i):
    global gamma
    x, y = gamma[0], gamma[1]
    theta_points.append(x)
    thetad_points.append(y)

    line.set_data(theta_points, thetad_points)
    gamma = gamma + dt*np.array([gamma[1], get_theta2dot(gamma[0], gamma[1])])
    
    
    return line,

anim = anm.FuncAnimation(fig, animate, init_func=init, frames=600, interval=20, blit=True)
    



#plt.plot(theta_points, thetad_points, lw='4', color='black')
#plt.show()
anim.save('simple-pendulum\\animation.gif', 
          writer = 'Pillow', fps = 30)
print("DONE")
