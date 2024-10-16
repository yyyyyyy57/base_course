import numpy as np
import constants as cst

h = 100
a = 45
b = 35

v = np.sqrt((cst.g * h * (np.tan(b))**2) / (2 * (np.cos(a)))**2 * (1 - np.tan(b) * np.tan(a)))
print(v)

T = 200
ep = 300

N = (2 / np.sqrt(np.pi)) * (cst.plank / (cst.k * T)**(3/2)) * cst.eiler**(cst.eiler*(-1)/(cst.k*T)) * cst.eiler**(T/2)
print(N)