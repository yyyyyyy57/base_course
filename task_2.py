import matplotlib.pyplot as plt
import numpy as np

a = -50
b = 50
n = 1000

def plotter(start, end, num, k=1):

    x = np.linspace(start, end, num)
    y = k/x

    plt.plot(x, y)
    plt.savefig('task_2.png')

print(plotter(a, b, n))