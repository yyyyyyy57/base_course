name = 'Garanina Ksenia Sergeevna'

codes1 = [ord(symbol) for symbol in name.upper()]
print(codes1)
codes2 = [ord(symbol) for symbol in name.lower()]
print(codes2)

print('sum1:', sum(codes1))
print('sum2:', sum(codes2))