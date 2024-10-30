import numpy as np
import constants as co

x_0 = 0
v_0 = 20
y_0 = 0

d = 45
r = np.radians(d)

vx_0 = v_0 * np.cos(r)
vy_0 = v_0 * np.sin(r)

t = np.linspace(0, 5, 51)

x = x_0 + vx_0 * t
y = y_0 + vy_0 * t - 0.5 * co.g * (t**2)

coord = np.column_stack((t, x, y))
print(coord)   