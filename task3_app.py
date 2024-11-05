import numpy as np

n = int(input())
m = int(input())

array = np.random.randint(0, 100, (n, m))
print(array)

for i in range(m):
    s = []
    for j in range(n):
        a = array[j, i]
        s.append(a)
    print(max(s))
    