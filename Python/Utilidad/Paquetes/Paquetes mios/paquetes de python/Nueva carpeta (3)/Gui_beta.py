import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
from tkinter import *


def start_curve(a=1,t=4*np.pi):
	ventana = Tk()
	ventana.title("Fisica interactiva")
	ventana.resizable(0,0)
	ventana.geometry("900x900")
	# FRAMES
	principal_frame = Frame(ventana,bg="purple",width=900,height=100).place(x=0,y=0)
	botones_frame = Frame(ventana,bg="blue",width=250,height=800).place(x=0,y=100)
	grafico_frame = Frame(ventana,bg="green",width=650,height=800).place(x=250,y=100)
	# ------------------------------- 1111111111111-------------------
	# titulo
	Label(principal_frame,text="Curva de viviani",font=(50)).place(x=400,y=50)
	# boton de salida
	Button(principal_frame,text="<",font=(50),command=lambda:salir_viviani(ventana)).place(x=50,y=50)
	# ------------------------------- 1111111111111-------------------
	# ------------------------------- 2222222222222-------------------
	# botones
	# Se utilizo ancho 27 y altura 2 por que 27 se aproxima a 200p y 2 por que son exactamente 40p
	# se hiso una division de 400p / 11 (por que son 11 espacio vacios) y se aproximo a 36p (es decir 36p de espacio entre botones)
	# como el boton ocupa 40p y 36p de espacio entre botones cada boton tendra 76p de distancia (40+36=76)
	Button(botones_frame,text="Posicion",width=27,height=2,cursor="pirate").place(x=50,y=136) 
	Button(botones_frame,text="Velocidad",width=27,height=2,cursor="pirate").place(x=50,y=212)
	Button(botones_frame,text="Velocidad media",width=27,height=2,cursor="pirate").place(x=50,y=288)
	Button(botones_frame,text="Aceleracion",width=27,height=2,cursor="pirate").place(x=50,y=364)
	Button(botones_frame,text="Aceleracion media",width=27,height=2,cursor="pirate").place(x=50,y=440)
	Button(botones_frame,text="Curvatura",width=27,height=2,cursor="pirate").place(x=50,y=516)
	Button(botones_frame,text="Radio de curvatura",width=27,height=2,cursor="pirate").place(x=50,y=592)
	Button(botones_frame,text="Torsion",width=27,height=2,cursor="pirate").place(x=50,y=668)
	Button(botones_frame,text="Radio de torsion",width=27,height=2,cursor="pirate").place(x=50,y=744)
	Button(botones_frame,text="Longitud de arco",width=27,height=2,cursor="pirate").place(x=50,y=823)
	# ------------------------------- 2222222222222-------------------
	# ------------------------------- 3333333333333-------------------
	# Los input
	# se puso 32 y no 27 como en los anteriores debido a que entry no trabaja con las mismas proporciones
	# se usaron 83p de distancia entre los input
	# como mide aproximadamente 200p entonces entre cada input existen 283p entre los entry
	# el mensaje que esta al lado esta a 30p del entry
	entry_a = StringVar()
	entry_a.set("")
	entry_t = StringVar()
	entry_t.set("")
	if t != 4*np.pi:
		entry_t.set(str(t))
	if a != 1:
		entry_a.set(str(a))
	Entry(grafico_frame,textvariable=entry_a,width=32,justify="center").place(x=333,y=823) # justify centrara el "texto" escrito
	Label(grafico_frame,text="a=",font=(35)).place(x=303,y=823)
	Entry(grafico_frame,textvariable=entry_t,width=27,justify="center").place(x=616,y=823)
	Label(grafico_frame,text="t=",font=(35)).place(x=589,y=823)
	Button(grafico_frame,text="Graficar",command=lambda:recuperar(ventana,entry_a,entry_t)).place(x=800,y=823)
	# implementar grafico

	fig = plt.figure()
	canvas = FigureCanvasTkAgg(fig,ventana)
	canvas.get_tk_widget().place(x=255.,y=212)
	canvas._tkcanvas.place(x=255.,y=212)
	grafico = Axes3D(fig)
	grafico.set_xlim3d([0, 2.0]) # el eje x entre 0 y 2 (se uso corchete por la cantidad de datos)
	grafico.set_xlabel('X') # lo que se esta escrito en el eje x
	grafico.set_ylim3d([-1.0, 2.0]) # el eje y entre -1 y 2 (se uso corchete por la cantidad de datos)
	grafico.set_ylabel('Y') # lo que se esta escrito en el eje y
	grafico.set_zlim3d([-2.0, 2.0]) # el eje z entre -2 y 2 (se uso corchete por la cantidad de datos)
	grafico.set_zlabel('Z')
	t = np.linspace(-4, t,70)
	x = a * (1 + np.cos(t))
	y = a * np.sin(t)
	z = 2 * a * np.sin(t/2)
	eje = [x,y,z]
	ejes = np.array(eje)
	linea, = grafico.plot(ejes[0, 0:1], ejes[1, 0:1], ejes[2, 0:1], 'm', label="Curva de Viviani", lw=4)
	# figura,funcion,fargs:(datos,linea dibujada),FPS,ms,blit
	animacion = animation.FuncAnimation(fig, muerte_a_omar, fargs=(ejes, linea),frames=60,interval=16.6, blit=False)

	
	# ------------------------------- 3333333333333-------------------
	# medidor en pixeles
	#horizontal1 = Frame(ventana,bg="red",width=900,height=1).place(x=0,y=212)
	#horizontal2 = Frame(ventana,bg="red",width=900,height=1).place(x=0,y=252)
	#vertical1 = Frame(ventana,bg="red",width=1,height=900).place(x=280,y=0)
	#vertical1 = Frame(ventana,bg="red",width=1,height=900).place(x=800,y=0)

	ventana.mainloop()

def salir_viviani(ventana):
    ventana.quit()
    ventana.destroy()

def recuperar(ventana,entry_a,entry_t):
	entry_a.set(entry_a.get())
	#print(entry_a.get())
	entry_t.set(entry_t.get())
	#print(entry_t.get())
	a = int(entry_a.get())
	t = int(entry_t.get())
	salir_viviani(ventana)
	start_curve(a,t)



def muerte_a_omar(num, ejes, linea):
    linea.set_data(ejes[:2, :num])
    linea.set_3d_properties(ejes[2, :num])

_name_ = "_main_"
if _name_ == "_main_":
	 start_curve()