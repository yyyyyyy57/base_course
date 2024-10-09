a = int(input('enter number a: '))
b = int(input('enter number b: '))

if b == 0:
    print('NO GOD PLEASE NO!!')
elif a % b == 0:
    print('a delitsya na b. a / b =', a / b)
else:
    print('a ne delitsya na b. a / b =', a / b)
    print('ostatok raven', a // b)