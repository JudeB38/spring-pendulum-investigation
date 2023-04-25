import numpy as np
import matplotlib.pyplot as plt

spring_const = 50
mass = 4
initial_length = 1
mu = 1
g = 9.81

def get_ml2d(th, l):
    return mass*g*np.cos(th) - spring_const*(l - initial_length)

def get_mth2d(th, thd, l, ld):
    return -mass*g*np.sin(th)-mu*l*thd - th*get_ml2d(th, l) - 2*mass*thd*ld

def get_ngamma(gamma):
    return np.array([gamma[1]/mass, get_mth2d(gamma[0], gamma[1]/mass, gamma[2], gamma[3]/mass), gamma[3]/mass, get_ml2d(gamma[0], gamma[2])])

gamma = np.array([0.3, 2., 1., -1.])

dt = 0.001
max_t = 10
t = 0
A=[]
L=[]
P_x, P_y = [], []
while t <= max_t:
    print(f"{gamma[0]:.2}, {gamma[1]:.2}, {gamma[2]:.2}, {gamma[3]:.2}")
    gamma += dt*get_ngamma(gamma)
    
    
    #A.append(gamma[0])
    #L.append(gamma[2])
    P_x.append(gamma[2]*np.sin(gamma[0]))
    P_y.append(-1*gamma[2]*np.cos(gamma[0]))
    t += dt


plt.scatter([0], [0])
plt.plot(P_x, P_y)
plt.xlim(left=-1, right=1)
plt.ylim(top=0.1, bottom=-5)
#plt.plot(A)
#plt.show()
#plt.plot(L)
plt.show()


