import numpy as np

n = 11
a = 0
b = 50

def func(start, end, num):
    x = np.linspace(start, end, num)
    y = x**2
    print(x)
    print(y)

print(func(a, b, n))