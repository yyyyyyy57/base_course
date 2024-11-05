import numpy as np

array = []
for i in range(9):
    array.append(int(input()))
print(array)

b = int(input())
c = int(input())

slice1 = array[:c]
slice2 = array[c:]

slice1.append(b)
print(slice1 + slice2)