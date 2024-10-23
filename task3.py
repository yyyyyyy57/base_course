import numpy as np
import constants as co

x0 = 0
v0 = 20
y0 = 0

d = 45
r = np.radians(d)

v0x = v0 * np.cos(r)
v0y = v0 * np.sin(r)

t = np.linspace(0, 5, 51)

x = x0 + v0x * t
y = y0 + v0y * t - 0.5 * co.g * (t**2)

res = np.column_stack((t, x, y))
print(res)          