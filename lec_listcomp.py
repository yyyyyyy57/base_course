symbols = 'Python'
symbol_codes = [ord(symbol) for symbol in symbols]
print(symbol_codes) #list

symbols = 'snake'
symbol_codes = (ord(symbol) for symbol in symbols)
print(symbol_codes) #генератор

