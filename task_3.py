import matplotlib.pyplot as plt
import numpy as np

st = -100
en = 100
n = 100

def plotter(start, end, num, a=70, b=50):

    x = np.linspace(start, end, num)
    y = np.linspace(start, end, num)

    X, Y = np.meshgrid(x, y)

    fxy = X**2/a**2 + Y**2/b**2

    plt.contour(X, Y, fxy, levels=[1])
    plt.axis('equal')
    plt.savefig('task_3.png')

if __name__ == '__main__':
    plotter(st, en, n)