import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anm

spring_const = 50
mass = 4
initial_length = 1
mu = 1
g = 9.81
global gamma

def get_ml2d(th, l):
    return mass*g*np.cos(th) - spring_const*(l - initial_length)

def get_mth2d(th, thd, l, ld):
    return -mass*g*np.sin(th)-mu*l*thd - th*get_ml2d(th, l) - 2*mass*thd*ld

def get_ngamma(gamma):
    return np.array([gamma[1]/mass, get_mth2d(gamma[0], gamma[1]/mass, gamma[2], gamma[3]/mass), gamma[3]/mass, get_ml2d(gamma[0], gamma[2])])

gamma = np.array([0.3, 2., 1., -1.])

dt = 0.01
time_elapsed = 5

fig = plt.figure()
ax = plt.axes(xlim=(-1.5, 1.5), ylim=(-4, 1))
ax.scatter([0], [0])
line, = ax.plot([], [], lw=2)


def init():
    line.set_data([], [])
    return line,

x_l, y_l = [], []
def animate(t):
    global gamma
    print(f"t={t*dt:.3}: {gamma[0]:.2}, {gamma[1]:.2}, {gamma[2]:.2}, {gamma[3]:.2}")
    gamma += dt*get_ngamma(gamma)
    
    
    x = gamma[2]*np.sin(gamma[0])
    y = -1*gamma[2]*np.cos(gamma[0])
    x_l.append(x)
    y_l.append(y)
    line.set_data(x_l, y_l)

    return line,


FRAMES = int(time_elapsed/dt)
FPS = int(1/dt)
INTERVAL = int(dt*1000)

anim = anm.FuncAnimation(fig, animate, init_func=init, frames=FRAMES, interval=INTERVAL, blit=True)
anim.save('animation.gif', fps = FPS)
print("DONE")



