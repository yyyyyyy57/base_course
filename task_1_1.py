import matplotlib.pyplot as plt
import numpy as np

def cycloid(R=3):
    t = np.arange(-5*np.pi, 5*np.pi, 0.1)

    x = R * (t - np.sin(t))
    y = R * (1 - np.cos(t))

    plt.plot(x, y, ls='-', lw=2)
    plt.axis('equal')
    plt.savefig('fig_2.png')

if __name__ == '__main__':
    cycloid()