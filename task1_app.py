a = int(input('введите a: ')) # ax^2 + bx + c = 0
b = int(input('введите b: '))
c = int(input('введите c: '))

d = b**2 - 4*a*c

if d < 0:
    print('нет корней')
elif d > 0:
    print('два корня')
    k = (d ** (1/2) - b) / 2
    l = (-1 * d ** (1/2) - b) / 2
    print(f'корни: {k}, {l}')
elif d == 0:
    print('один корень')
    k = 0 - b/2
    print(f'корень: {k}')