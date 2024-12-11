import matplotlib.pyplot as plt
import numpy as np

def asteroid(R=9):
    t = np.arange(-2*np.pi, 2*np.pi, 0.1)

    x = R * np.cos(t)**3
    y = R * np.sin(t)**3

    plt.plot(x, y, ls='-', lw=2)
    plt.axis('equal')
    plt.savefig('fig_3.png')

if __name__ == '__main__':
    asteroid()