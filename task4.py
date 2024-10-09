n = int(input('введите число: '))
a = 1
b = 1

output = []

for i in range(1, n+1):
    output.append(b)
    a += b
    b = a - b

print(output)