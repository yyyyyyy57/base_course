import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

def my_func(a):
    sum = 0
    count = 0
    for i in a:
        sum += i
        count += 1
    d = sum/count
    return d

print(my_func(arr))