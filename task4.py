import numpy as np

N = 10
M = 5

trigonometry_array = np.zeros((N, M))

for i in range(N):
    for j in range(M):
        trigonometry_array[i, j] = np.sin(i*N)
        if trigonometry_array[i, j] < 0:
            trigonometry_array[i, j] = 0

print(trigonometry_array)