import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 1000)
y = x // 1

plt.plot(x, y)
plt.savefig('task_4_app.png')