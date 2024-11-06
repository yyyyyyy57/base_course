import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

def multip(a):
    s = 1
    for i in a:
        s *= i
    return s

print(multip(arr))