import numpy as np
import constants as co

h = 100
a = 45
b = 35

v = ((co.g * h * np.tan(b)**2) / (2 * np.cos(a)**2 * (1 - np.tan(a) * np.tan(b))))**(1/2)
print(v)

T = 200
e = 300

N = (2/np.pi**(1/2)) * (co.plank/(co.k * T)**(3/2)) * co.eiler**((-1)*co.eiler/co.k/T) * co.eiler**(T/2)
print(N)