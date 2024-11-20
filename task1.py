import random

n = 3

arr1, arr2, arr3 = [random.randint(0, 100) for _ in range(n)], [random.randint(0, 100) for _ in range(n)], [random.randint(0, 100) for _ in range(n)]
print(arr1, arr2, arr3)

max_num = max(max(arr1), max(arr2), max(arr3))
arr_sum = sum(arr1) + sum(arr2) + sum(arr3)

print('наибольший элемент:', max_num)
print('суммa всех элементов:', arr_sum)
