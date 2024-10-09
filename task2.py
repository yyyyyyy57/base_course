b = int(input('введите первый член: '))
q = int(input('введите знаменатель: '))
n = int(input('введите количество членов: '))

for i in range(1, n+1):
    num = b * q ** (i-1)
    print(num)