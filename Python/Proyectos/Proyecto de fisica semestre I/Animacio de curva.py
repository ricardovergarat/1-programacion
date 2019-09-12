from matplotlib import pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation

def muerte_a_omar(num, ejes, linea):
    linea.set_data(ejes[:2, :num])
    linea.set_3d_properties(ejes[2, :num])

# Creamos una figura
fig = plt.figure()
# Establecemos que es una figira de tipo 3D
grafico = fig.gca( projection='3d')
# Titulo del grafico
grafico.set_title("Curva Viviani")
# limites del grafico
grafico.set_xlim3d([0, 2.0]) # el eje x entre 0 y 2 (se uso corchete por la cantidad de datos)
grafico.set_xlabel('X') # lo que se esta escrito en el eje x
grafico.set_ylim3d([-1.0, 2.0]) # el eje y entre -1 y 2 (se uso corchete por la cantidad de datos)
grafico.set_ylabel('Y') # lo que se esta escrito en el eje y
grafico.set_zlim3d([-2.0, 2.0]) # el eje z entre -2 y 2 (se uso corchete por la cantidad de datos)
grafico.set_zlabel('Z') # lo que se esta escrito en el eje z
# El valor recuperado
a = 1
# Los valores de T
t = np.linspace(-4, 4*np.pi,70)
# Ejes
x = a * (1 + np.cos(t))
y = a * np.sin(t)
z = 2 * a * np.sin(t/2)
eje = [x,y,z]
# agregadmos la lista en un array para dibujar la linea
ejes = np.array(eje)
linea, = grafico.plot(ejes[0, 0:1], ejes[1, 0:1], ejes[2, 0:1], 'm', label="Curva de Viviani", lw=5)
# figura,funcion,fargs:(datos,linea dibujada),FPS,ms,blit
animacion = animation.FuncAnimation(fig, muerte_a_omar, fargs=(ejes, linea),frames=15,interval=200, blit=False)
# mostrar el grafico
plt.show()

