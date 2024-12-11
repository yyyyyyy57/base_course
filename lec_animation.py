import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()                            # создание пространства и подпространства для анимации
anim_object, = plt.plot([], [], '-', lw=2)          # объект анимации

x, y = [], []                                       # координаты объекта анимации
parameter = np.linspace(0, 2*np.pi, 100)

ax.set_xlim(0, 2*np.pi)                             # пределы изменения переменной
ax.set_ylim(-1, 1)

def update(frame):                                  # функция подстановки параметра в объект анимации 
    x.append(frame)
    y.append(np.sin(frame))

    anim_object.set_data(x, y)                      # передача координат объекту анимации

    return anim_object
 
ani = FuncAnimation(fig,                          # вызов простраства для анимации
                    update,                       # вызов функции подстановки координат
                    frames=parameter,             # интервал значений
                    interval=50)                  # интервал между кадрами

ani.save('animation_1.gif', writer='pillow')