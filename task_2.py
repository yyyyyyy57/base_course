import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

t = np.linspace(0, 12*np.pi, 1000)

def circle_move(vx0, vy0, time):
    x0 = vx0 * time
    y0 = vy0 * time
    x = x0 * np.cos(t) - y0 * np.sin(t)
    y = y0 * np.cos(t) + y0 * np.sin(t)
    return x, y

fig, ax = plt.subplots()
ball, = plt.plot([], [], '-', color='b', label='Ball')

def animate(i):
    ball.set_data(circle_move(vx0=0.01, vy0=0.01, time=i))
    

edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani = FuncAnimation(fig, animate, frames=100, interval=30)
ani.save('animation_4.gif', writer='pillow')