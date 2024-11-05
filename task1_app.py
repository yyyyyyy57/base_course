import numpy as np

n = int(input())
m = int(input())

arr = []
arr2 = []
arr3 =[]

for i in range(n):
    a = []
    for j in range(m):
        a.append(int(input()))
    arr.append(a)

for i in range(n):
    a = []
    for j in range(m):
        a.append(int(input()))
    arr2.append(a)

arr3 = np.maximum(arr, arr2)

print(arr)
print(arr2)
print(arr3)