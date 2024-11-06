import numpy as np

def area(figure, *args):
    if figure == 'circle':
        a = np.pi * args[0]**2
    if figure == 'triangle':
        a = args[0] * args[1] / 2
    if figure == 'rectangle':
        a = args[0] * args[1]
    return a

print(area('rectangle', 6, 10))