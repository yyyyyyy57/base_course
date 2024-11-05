import numpy as np

arr = []
arr2 = []
arr3 =[]

for i in range(3):
    a = []
    for j in range(3):
        a.append(int(input()))
    arr.append(a)

for i in range(3):
    a = []
    for j in range(3):
        a.append(int(input()))
    arr2.append(a)

for i in range(3):
    a = []
    for j in range(3):
        a.append(np.max(arr[i][j], arr2[i][j]))
    arr3.append(a)

print(arr)
print(arr2)
print(arr3)