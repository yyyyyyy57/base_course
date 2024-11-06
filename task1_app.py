x = 2
y = 4

def power(a, n):
    s = 1
    for i in range(n):
        s *= a
    return s

print(power(x, y))