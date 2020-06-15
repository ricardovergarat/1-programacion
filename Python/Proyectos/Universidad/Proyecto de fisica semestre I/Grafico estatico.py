import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a = 1
t = np.linspace(-4, 4*np.pi, 100)
x = a * (1 + np.cos(t))
y = a * np.sin(t)
z = 2 * a * np.sin(t/2)
print(z)

fig = plt.figure()
ax = fig.gca( projection='3d')

ax.plot(x, y, z, label="Curva de Viviani", lw=5)
plt.show()

