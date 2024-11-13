names = ['john', 'david', 'maria', 'anna']
ages = [16, 25, 19, 15]
is_teenager = [True, False, True, True]

users = list(zip(names, ages, is_teenager))
print(users)

print('user age:', dict(zip(names, ages)))