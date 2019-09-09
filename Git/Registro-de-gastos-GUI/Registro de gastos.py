from tkinter import *
import datetime
from screeninfo import get_monitors  
import time

def medidor_de_pixeles(ventana):
	horizontal1 = Frame(ventana,bg="red",width=700,height=1).place(x=0,y=350)
	horizontal2 = Frame(ventana,bg="red",width=700,height=1).place(x=0,y=380)
	vertical1 = Frame(ventana,bg="red",width=1,height=700).place(x=20,y=0)
	vertical2 = Frame(ventana,bg="red",width=1,height=700).place(x=50,y=0)
	

def La_ventana():
	ventana = Tk()
	caracteristicas_ventana(ventana)
	Los_frames(ventana)
	botones(ventana)
	determinar_dia()
	medidor_de_pixeles(ventana)
	ventana.mainloop()

def caracteristicas_ventana(ventana):
	x,y = determinar_resolucion()
	mostrar(x)
	mostrar(y)
	ventana.geometry("%dx%d+%d+%d" % (700,700,(x/2)-350,0)) # El programa se mostrara al centro de la pantalla
	ventana.configure(background='blue')
	ventana.resizable(0,0) # impide que se expanda la ventana

def determinar_resolucion():
	pantalla = Tk()
	ancho = pantalla.winfo_screenwidth()
	alto = pantalla.winfo_screenheight()
	pantalla.destroy()
	return ancho,alto

def Los_frames(ventana):
	Frame_lista = Frame(ventana,bg="purple",width=250,height=500).place(x=400,y=100)
	Frame_botones = Frame(ventana,width=400,height=500).place(x=0,y=100)


def determinar_dia():
	dia = str(time.strftime("%d/%m/%y"))
	print("string: ",dia)


def botones(ventana):
	Button(ventana,text="Salir",font=(50),command=lambda:salir(ventana)).place(x=20,y=30)
	Button(ventana,text="Eliminar").place(x=430,y=630)
	Button(ventana,text="Listo").place(x=530,y=630)
	Button(ventana,text="<<",font=(50)).place(x=20,y=350)
	Button(ventana,text=">>",font=(50)).place(x=350,y=350)
	x = 0
	while x != 10:
		Button(ventana,text=x,font=(50)).place(x=80,y=110 + (50*x))
		Button(ventana,text=x+10,font=(50)).place(x=160,y=110 + (50*x))
		x = x + 1
	#b0 = Button(ventana,text="0",font=(50)).place(x=80,y=100)
	#b1 = Button(ventana,text="1",font=(50)).place(x=80,y=150)
	#b2 = Button(ventana,text="2",font=(50)).place(x=80,y=200)
	#b3 = Button(ventana,text="3",font=(50)).place(x=80,y=250)
	#b4 = Button(ventana,text="4",font=(50)).place(x=80,y=300)
	#b5 = Button(ventana,text="5",font=(50)).place(x=80,y=350)
	#b6 = Button(ventana,text="6",font=(50)).place(x=80,y=400)
	#b7 = Button(ventana,text="7",font=(50)).place(x=80,y=450)
	#b8 = Button(ventana,text="8",font=(50)).place(x=80,y=500)
	#b9 = Button(ventana,text="9",font=(50)).place(x=80,y=550)

def salir(ventana):
    ventana.quit()

def mostrar(x):
	print(x)


_name_ = "_main_"
if _name_ == "_main_":
	La_ventana()