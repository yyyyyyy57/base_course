g = 9.8

m = 5
h = 20
v = 10

def energy(mass, height, velocity):
    e1 = mass*g*height
    e2 = mass*velocity**2/2
    return e1 + e2

print(energy(m, h, v))