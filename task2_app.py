print('введите стороны треугольника')
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

if a + b <= c or a + c <= b or b + c <= a:
    print('такого треугольника не существует')
else:
    print('треугольник существует')
    if a == b or b == c or a == c:
        print('треугольник равнобедренный')
    elif a == b == c:
        print('треугольник равносторонний')
    else:
        print('треугольник разносторонний')
