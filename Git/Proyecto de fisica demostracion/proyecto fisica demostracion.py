import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
from tkinter import *

def medidor_de_pixeles(ventana):
	horizontal1 = Frame(ventana,bg="red",width=700,height=1).place(x=0,y=590)
	horizontal2 = Frame(ventana,bg="red",width=700,height=1).place(x=0,y=615)
	vertical1 = Frame(ventana,bg="red",width=1,height=700).place(x=290,y=0)
	vertical2 = Frame(ventana,bg="red",width=1,height=700).place(x=486,y=0)

def start_curve(a=1,t=13,anima="ON",contador=0,presionado="vacio",vectores=60):
	x,y = determinar_resolucion()
	x,y = centrar_ejes(x,y)
	ventana = Tk()
	ventana.title("Fisica interactiva") 
	ventana.resizable(0,0) # impide que se expanda la ventana
	ventana.geometry("%dx%d+%d+%d" % (900,700,x,y))
	#------------------------------------------------------------------

	principal_frame = Frame(ventana,width=900,height=100).place(x=0,y=0)
	botones_frame = Frame(ventana,width=250,height=600).place(x=0,y=100)
	grafico_frame = Frame(ventana,width=650,height=600).place(x=250,y=100)

	#------------------------------------------------------------------------------

	Button(principal_frame,text="<<",font=(200),command=lambda:salir_viviani(ventana)).place(x=10,y=50)
	Label(principal_frame,text="Curva de viviani",font=(50)).place(x=400,y=50)
	Label(principal_frame,text="Animacion",font=(50)).place(x=710,y=50)
	Button(principal_frame,text="ON",command=lambda:recuperar(ventana,entry_a,entry_t,"ON",contador,presionado,entry_vectores)).place(x=830,y=50)
	Button(principal_frame,text="OFF",command=lambda:recuperar(ventana,entry_a,entry_t,"OFF",contador,presionado,entry_vectores)).place(x=860,y=50)



	Button(botones_frame,text="Posicion",width=27,height=2,command=lambda:recuperar(ventana,entry_a,entry_t,anima,contador,"Posicion",entry_vectores)).place(x=30,y=110)
	Button(botones_frame,text="Velocidad",width=27,height=2,command=lambda:recuperar(ventana,entry_a,entry_t,anima,contador,"Velocidad",entry_vectores)).place(x=30,y=170)
	Button(botones_frame,text="Velocidad media",width=27,height=2,command=lambda:recuperar(ventana,entry_a,entry_t,anima,contador,"Velocidad media",entry_vectores)).place(x=30,y=230)
	Button(botones_frame,text="Aceleracion",width=27,height=2,command=lambda:recuperar(ventana,entry_a,entry_t,anima,contador,"Aceleracion",entry_vectores)).place(x=30,y=290)
	Button(botones_frame,text="Aceleracion media",width=27,height=2,command=lambda:recuperar(ventana,entry_a,entry_t,anima,contador,"Aceleracion media",entry_vectores)).place(x=30,y=350)
	Button(botones_frame,text="Curvatura",width=27,height=2,command=lambda:recuperar(ventana,entry_a,entry_t,anima,contador,"Curvatura",entry_vectores)).place(x=30,y=410)
	Button(botones_frame,text="Radio de curvatura",width=27,height=2,command=lambda:recuperar(ventana,entry_a,entry_t,anima,contador,"Radio de curvatura",entry_vectores)).place(x=30,y=470)
	Button(botones_frame,text="Torsion",width=27,height=2,command=lambda:recuperar(ventana,entry_a,entry_t,anima,contador,"Torsion",entry_vectores)).place(x=30,y=530)
	Button(botones_frame,text="Radio de torsion",width=27,height=2,command=lambda:recuperar(ventana,entry_a,entry_t,anima,contador,"Radion de torsion",entry_vectores)).place(x=30,y=590)
	Button(botones_frame,text="Longitud de arco",width=27,height=2,command=lambda:recuperar(ventana,entry_a,entry_t,anima,contador,"Longitud",entry_vectores)).place(x=30,y=650)

	entry_a = StringVar()
	entry_a.set("")
	entry_t = StringVar()
	entry_t.set("")
	entry_vectores = StringVar()
	entry_vectores.set("")

	if contador != 0:
		entry_a.set(a)
		entry_t.set(t)
		entry_vectores.set(vectores)
		a,t,vectores = evitar_errores(a,t,vectores)

	Label(grafico_frame,text="a=",font=(1)).place(x=260,y=590)
	Entry(grafico_frame,textvariable=entry_a,width=27,justify="center").place(x=290,y=590)
	Label(grafico_frame,text="t=",font=(1)).place(x=496,y=590)
	Entry(grafico_frame,textvariable=entry_t,width=27,justify="center").place(x=516,y=590)

	Button(grafico_frame,text="Graficar",command=lambda:recuperar(ventana,entry_a,entry_t,anima,contador,presionado,entry_vectores)).place(x=742,y=590)

	if presionado != "vacio":
		Label(grafico_frame,text=presionado).place(x=260,y=675)
		resultado = operacion(presionado,a,t)
		Label(grafico_frame,text=resultado).place(x=450,y=675)

	Label(grafico_frame,text="V",font=(1)).place(x=690,y=630)
	Entry(grafico_frame,textvariable=entry_vectores,width=27,justify="center").place(x=720,y=630)


	fig = plt.figure()
	canvas = FigureCanvasTkAgg(fig,ventana)
	canvas.get_tk_widget().place(x=255,y=100)
	canvas._tkcanvas.place(x=255,y=100)
	grafico = Axes3D(fig) 
	grafico.set_xlabel('X') 
	grafico.set_ylabel('Y') 
	grafico.set_zlabel('Z')

	if t == 0:
		t = np.linspace(-0.1, t,vectores)
	else:

		t = np.linspace(0, t,vectores)

	if presionado == "Posicion":
		x = a * (1 + np.cos(t))
		y = a * np.sin(t)
		z = 2 * a * np.sin(t/2)
	elif presionado == "Velocidad":
		x = a * (- np.sin(t))
		y = a * np.cos(t)
		z = a * np.cos(t/2)
		
	elif presionado == "Aceleracion":
		x = -a * np.cos(t)
		y = a * (- np.sin(t))
		z = (-(a * np.sin(t/2)))/2
		
	elif presionado == "Velocidad media":
		x = (a * (-1 + np.cos(t)))/t
		y = (a * np.sin(t))/t
		z = (2 * a * np.sin(t/2))/t
		
	elif presionado == "Aceleracion media":
		x = (-a * np.sin(t))/t
		y = (a * (np.cos(t) - 1))/t
		z = (a * (np.cos(t/2) - 1))/t
		
	else:
		x = a * (1 + np.cos(t))
		y = a * np.sin(t)
		z = 2 * a * np.sin(t/2)
	ms = 1000/vectores
	# Las siguientes dos lineas estan para dar el conjunto de cordenada a la animacion
	eje = [x,y,z]
	ejes = np.array(eje)
	if anima == "ON":
		linea, = grafico.plot(x, y, z, 'm', label="Curva de Viviani", lw=1)
		# figura,funcion,fargs:(datos,linea dibujada),FPS,ms,blit
		animacion = animation.FuncAnimation(fig, muerte_a_omar, fargs=(ejes, linea),frames=vectores,interval=ms, blit=False)
		#animacion = animation.FuncAnimation(fig, muerte_a_omar, fargs=(ejes, linea),frames=60,interval=16.6, blit=False,repeat=False)
	else:
		linea, = grafico.plot(x, y, z, 'm', label="Curva de Viviani", lw=1)

	#medidor_de_pixeles(ventana)
	ventana.mainloop()

def determinar_resolucion():
	pantalla = Tk()
	ancho = pantalla.winfo_screenwidth()
	alto = pantalla.winfo_screenheight()
	pantalla.destroy()
	return ancho,alto

def centrar_ejes(x,y):
	x = (x / 2) - 450
	if y <= 768:
		y = 0
	else:
		y = (y / 2) - 350
	return x,y

def salir_viviani(ventana):
    ventana.quit()
    ventana.destroy()


def recuperar(ventana,entry_a,entry_t,anima,contador,presionado,entry_vectores):
	entry_a.set(entry_a.get())
	entry_t.set(entry_t.get())
	entry_vectores.set(entry_vectores.get())
	a = str(entry_a.get())
	t = str(entry_t.get())
	vectores = str(entry_vectores.get())
	contador = contador + 1
	salir_viviani(ventana)
	start_curve(a,t,anima,contador,presionado,vectores)

def muerte_a_omar(num, ejes, linea):
    linea.set_data(ejes[:2, :num])
    linea.set_3d_properties(ejes[2, :num])

def evitar_errores(a,t,vectores):
	if a == "":
		a = 1
	else:
		if "," in a or "." in a:
			a = a.replace(",",".")
			a = float(a)
		else:
			a = int(a)
	if t == "":
		t = 13
	else:
		if "," in t or "." in t:
			t = t.replace(",",".")
			t = float(t)
		else:
			t = int(t)
	if vectores == "":
		vectores = 60
	else:
		if int(vectores) <= 60:
			vectores = 60
		else:
			vectores = int(vectores)
	return a,t,vectores

def operacion(presionado,a,t):
	if presionado == "Posicion":
		x = str(a * (1 + np.cos(t)))
		y = str(a * np.sin(t))
		z = str(2 * a * np.sin(t/2))
		cordenada = "(" + x + " , " + y + " , "+ z + ")"
	elif presionado == "Velocidad":
		x = str(a * (- np.sin(t)))
		y = str(a * np.cos(t))
		z = "0"
		cordenada = "(" + x + " , " + y + " , "+ z + ")"
	elif presionado == "Aceleracion":
		x = str(-a * np.cos(t))
		y = str(a * (- np.sin(t)))
		z = "0"
		cordenada = "(" + x + " , " + y + " , "+ z + ")"
	else:
		cordenada = "Estamos trabajando para ello"
	return cordenada


_name_ = "_main_"
if _name_ == "_main_":
	 start_curve()
