name = 'Vlasov Vladislav'

name1 = name.upper()
name2 = name.lower()

list1 = [ord(symbol) for symbol in name1]
print(list1)

list2 = [ord(symbol) for symbol in name2]
print(list2)

max_num = max(max(list1), max(list2))
print('max:', max_num)

min_num = min(min(list1), min(list2))
print('min:', min_num)