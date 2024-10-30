import numpy as np

N = 10
M = 5

trigonometry_array = np.zeros((N, M))

for i in range(N):
    for j in range(M):
        trigonometry_array[i, j] = np.sin(i*N + j*M + 1)
        if trigonometry_array[i, j] < 0:
            trigonometry_array[i, j] = 0

a = trigonometry_array[::, 0]
b = trigonometry_array[::, 1]
c = trigonometry_array[::, 2]
d = trigonometry_array[::, 3]
e = trigonometry_array[::, 4]

tr_array2 = np.column_stack((a, c, b, d, e))
print(tr_array2)