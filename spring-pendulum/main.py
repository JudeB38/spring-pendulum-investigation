import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anm
import matplotlib as mpl

mpl.rcParams['animation.ffmpeg_path'] = r'C:\\Users\\joann\\Documents\\FFmpeg\\ffmpeg-master-latest-win64-gpl\\bin\\ffmpeg.exe'

spring_const = 50
mass = 4
initial_length = 1
mu = 1
g = 9.81
parameters = spring_const, mass, initial_length, mu, g
global gamma

def get_ml2d(th, l):
    return mass*g*np.cos(th) - spring_const*(l - initial_length)

def get_mth2d(th, thd, l, ld):
    return -mass*g*np.sin(th)-mu*l*thd - th*get_ml2d(th, l) - 2*mass*thd*ld

def get_ngamma(gamma):
    return np.array([gamma[1]/mass, get_mth2d(gamma[0], gamma[1]/mass, gamma[2], gamma[3]/mass), gamma[3]/mass, get_ml2d(gamma[0], gamma[2])])

def encode(gam, param, time):
    out = ""
    for i in gam:
        if i < 0:
            out += str(i) + "_"
        else:
            out += str(i) + "_"
    
    out += "K" + str(param[0]) + "_"
    out += "M" + str(param[1]) + "_"
    out += "L" + str(param[2]) + "_"
    out += "U" + str(param[3]) + "_"
    out += "T" + str(time)
    
    return out


gamma = np.array([0.3, 2., 1., 1.])
initial_gamma = gamma

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
    #print(f"t={t*dt:.3}: {gamma[0]:.2}, {gamma[1]:.2}, {gamma[2]:.2}, {gamma[3]:.2}")
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

name = encode(initial_gamma, parameters, time_elapsed)

f = f"spring-pendulum/animations/anim_{name}.mp4"
writermp4 = anm.FFMpegWriter(fps=FPS) 
anim.save(f, writer=writermp4)
print(name)



