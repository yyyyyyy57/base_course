year = int(input('enter a year: '))

if year % 400 == 0:
    print('this year is leap')
elif year % 100 == 0:
    print("this year isn't leap")
elif year % 4 == 0:
    print('this year is leap')
else:
    print("this year isn't leap")