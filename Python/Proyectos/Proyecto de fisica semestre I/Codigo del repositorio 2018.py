from tkinter import ttk
import numpy as np
from numpy import *
import math
import matplotlib as mpl
import matplotlib.pyplot as mpl
import matplotlib.pyplot as plt
from matplotlib import collections  as mc
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import math

class Interface:
    def __init__(self):
        # Valores Iniciales
        self.gravedad = 9.8
        self.velocidad_iniciacl = 2
        self.angulo = np.radians(45)
        self.x0 = 0
        self.y0 = 0
        self.velocidad_inicial = 10
        self.angulo = np.radians(2)
        self.x0 = 8
        self.y0 = 7
        self.z0 = 0
        self.window = tk.Tk()
        self.window.title("Fisica")
    def __init__(self):
        self.boton_alcance_horizontal = ttk.Button(self.opciones, text="Alcance Horizontal", width=10, command=lambda: self.boton_alcance_horizontalf())
        self.boton_altura_maxima = ttk.Button(self.opciones, text="Altura Màxima", width=10, command=lambda: self.boton_altura_maximaf())
        self.boton_camino_recorrido = ttk.Button(self.opciones, text="Camino Recorrido", width=10, command=lambda: self.boton_camino_recorridof())
        self.boton_radio_y_centro_de_curvatura_circulo_obsculador = ttk.Button(self.opciones, text="Radio y Centro de Curvatura y Circulo Obsculador", width=10, command=lambda: self.boton_radio_y_centro_de_curvatura_circulo_obsculadorf())
        self.boton_radio_y_centro_de_curvatura_circulo_obsculador = ttk.Button(self.opciones, text="Radio y Centro de Curvatura y Circulo Obsculador", width=10, command=lambda: self.boton_radio_y_centro_de_curvatura_circulo_obsculadorf)
        self.boton_aceleracion_normal_y_tangencial = ttk.Button(self.opciones, text="A. normal y tangencial", width=10, command=lambda: self.boton_aceleracion_normal_y_tangencialf())
        self.boton_vector_normal = ttk.Button(self.opciones, text="Vector normal", width=10,
                                              command=lambda: self.boton_vector_normalf())
        def limpiar_entrada_y0(event):
                self.entrada_posicion_y0.delete(0,'end')

        def limpiar_entrada_angulo(event):
            if self.entrada_angulo_inicial.get() == "Angulo Inicial":
                if self.entrada_angulo_inicial.get() == "Angulo":
                    self.entrada_angulo_inicial.delete(0,'end')

        def limpiar_entrada_Rapidez(event):
            self.deslizador_posicion_y0.bind("<B1-Motion>", f_posicion_y0)
            self.deslizador_posicion_y0.bind("<ButtonRelease-1>", f_posicion_y0)

            self.deslizador_angulo_inicial = ttk.Scale(angulo, variable=angulo_inicial, from_=0, to=89, orient=tk.HORIZONTAL)
            self.deslizador_angulo_inicial = ttk.Scale(angulo, variable=angulo_inicial, from_=0, to=90, orient=tk.HORIZONTAL)
            self.deslizador_angulo_inicial.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
            self.deslizador_angulo_inicial.set(50)
            self.deslizador_angulo_inicial.set(180)
            self.deslizador_angulo_inicial.bind("<B1-Motion>", f_angulo_inicial)

            self.deslizador_Rapidez_inicial = ttk.Scale(Rapidez, variable=Rapidez_inicial, from_=0, to=100, orient=tk.HORIZONTAL)
    def check(v, p):
        aceptar.bind("<Button-1>", copiar_valores)

    def boton_velocidadf(self):
        import matplotlib.pyplot as plt
        import math
        #  inicializa la ventana popup
        master = tk.Tk()
        master.title("Velocidad")
        L1 = tk.Label(Pop_Up, text="Eliga Tiempo a Evaluar")
        E1 = tk.Entry(Pop_Up, bd=5)
        E1.pack()
        L1.pack()
        label = tk.Label(Pop_Up)
        label.pack()

        button = ttk.Button(Pop_Up, text='Evaluar', width=10, command=Pop_Up.destroy)

        button.pack(side=tk.BOTTOM)

        def seno(Grado):
            # funcion para calcualar el seno de un angulo
         def alcance_max(self):
            return alc

            # generamiento de la grafica

        def GraficarFuncion(self):

            self.tiempo_dato = entrada_tiempo.get()

    def boton_altura_maximaf(self):
        result = result + y0 # lo sumar la posicion incicial del eje y
        final = round(result,5)
        def copiar_valores(event):
            master.destroy()

        master = tk.Tk()
        master.title("Altura Maxima")

        # Crea un frame contenedor para la izquierda y la derecha
        frame_arriba = ttk.Frame(master)
        frame_abajo = ttk.Frame(master)
        frame_aceptar = ttk.Frame(master)
        frame_arriba.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)
        frame_abajo.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)
        frame_aceptar.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Crea las titulos de la entrada de datos
        aceptar = ttk.Button(frame_aceptar, text="ACEPTAR")
        tiempo_init = ttk.Label(frame_arriba, text="Altura maxima: ")
        tiempo_init_x = ttk.Entry(frame_arriba, state='readonly', justify='center')
        tiempo_init.pack(side=tk.TOP)
        tiempo_init_x.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        tiempo_init_x.configure(state='normal')
        tiempo_init_x.delete(0, 'end')
        tiempo_init_x.insert(0, final)
        tiempo_init_x.configure(state='readonly')
        aceptar.pack(fill=tk.BOTH, expand=1)
        aceptar.bind("<Button-1>", copiar_valores)
        master.mainloop()

    def boton_camino_recorridof(self):
        pass

    def boton_radio_y_centro_de_curvatura_circulo_obsculadorf(self):
        # DATOS DE PRUEBA
            self.tiempo_datos[0] = entrada_tiempo.get()
            ang=np.pi/3
            g = 10
            t = 1
            v0=150
            x0=10
            x=0
            master.destroy()

        ##################
        # ECUACIONES
        # Metodo para validar la entrada de datos (Solo Numeros por ahora)
    def check(v, p):
        if p.isdigit():
            return True
        elif p is "":
            return True
        else:
            return False

        curvatura_pos = (np.abs(-g/(np.power(v0*np.cos(ang),2)))/(np.power(1+np.power(np.tan(ang)-g/np.power(v0*np.cos(ang),2)*(x-x0),2),3/2)))
        curvatura_t = (np.abs(-(g)/np.power(v0*np.cos(ang),2))/np.power(1+np.power(np.tan(ang)-(g/v0*np.cos(ang)*t),2),3/2))
        r_curvatura_pos = ((np.power(1+np.power(np.tan(ang)-g/(np.power(v0*np.cos(ang),2)*(x-x0)),2),3/2))/(np.abs(-g/np.power(v0*np.cos(ang),2))))
        r_curvatura_t = ((np.power(1+np.power(np.tan(ang)-g/v0*np.tan(ang)*t,2),3/2))/(np.abs(-g/np.power(v0*np.cos(ang),2))))
        centro_cuvatura_x=x-(((np.tan(ang)-(g/np.power(v0*np.cos(ang),2))*(x-x0))*(1+np.power(np.tan(ang)-(g/np.power(v0*np.cos(ang)*(x-x0),2)),2)))/(-g/np.power(v0*np.cos(ang),2)))
        #centro_curvatura_y=
        print("Curvatura en tiempo X: "+str(curvatura_t))
        print("Curvatura en posicion: "+str(curvatura_pos))
        print("Radio en posicion: "+str(r_curvatura_pos))
        print("Radio en tiempo X:"+str(r_curvatura_t))
        print("Centro de curvatura pos x:" +str(centro_cuvatura_x))
        # Datos Iniciales

        ##################

        # TEST DRAW #
        #  inicializa la ventana popup
        master = tk.Tk()
        master.title("Fisica")
        master.title("Posicion")
        # Crea un frame contenedor para la izquierda y la derecha
        frame_arriba = ttk.Frame(master)
        frame_centro = ttk.Frame(master)
    def boton_radio_y_centro_de_curvatura_circulo_obsculadorf(self):
        tiempo = ttk.Label(frame_abajo, text="Tiempo: ")
        tiempo_init = ttk.Label(frame_arriba, text="Intervalo de tiempo")
        tiempo_init_x = ttk.Entry(frame_arriba, state='readonly', justify='center')
        tiempo_init_y = ttk.Entry(frame_arriba, state='readonly')
        tiempo_init_y = ttk.Entry(frame_arriba, state='readonly', justify='center')
        tiempo_init.pack(side=tk.TOP)
        tiempo_init_x.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        tiempo_init_y.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
    def boton_radio_y_centro_de_curvatura_circulo_obsculadorf(self):
        aceptar = ttk.Button(frame_aceptar, text="ACEPTAR")
        aceptar.pack(fill=tk.BOTH, expand=1)
        aceptar.bind("<Button-1>", copiar_valores)


        #posible desplazamiento con
        pass

    #def boton_aceleracion_normal_y_tangencialf(self):
    def boton_alcance_horizontalf(self):
        pass

    def boton_altura_maximaf(self):
        pass
    def boton_camino_recorridof(self):
        pass

    @property
    def boton_radio_y_centro_de_curvatura_circulo_obsculadorf(self):
        def check(v, p):
            if p.isdigit():
                return True
            elif p is "":
                return True
            else:
                return False
        def time_impact(self):
            t = ((self.velocidad_inicial * sin(self.angulo)) / (self.gravedad)) + ((1 / self.gravedad) * (
            sqrt(((self.velocidad_inicial * sin(self.angulo)) ** 2) + (2 * self.y0 * self.gravedad))))
            return round(t,2)
        def validarIntervaloTiempo(valor):
            return (valor>0 &valor<=time_impact(self))
        """def radioButtons():
            print(v.get())
            return v.get()
        """
        def copiarTiempo(event):
            self.tiempo_datos[0] = tiempoUsuarioEntry.get()
            popup.destroy()

        # DATOS DE PRUEBA

        ang=np.pi/3 # REEMPLAZAR POR self.angulo_inicial ?
        g = 10  # Constante
        t = 1   # Este parametro se toma desde la ventana generada
        v0=150  # REEMPLAZAR POR self.velocidad_inicial ?
        x0=10   # ---------^
        y0=20   #
        x=0     # Este parametro se toma desde la ventana generada
        y=0     # ---------^

        ##################
        # ECUACIONES

        curvatura_pos = (np.abs(-g/(np.power(v0*np.cos(ang),2)))/(np.power(1+np.power(np.tan(ang)-g/np.power(v0*np.cos(ang),2)*(x-x0),2),3/2)))
        curvatura_t = (np.abs(-(g)/np.power(v0*np.cos(ang),2))/np.power(1+np.power(np.tan(ang)-(g/v0*np.cos(ang)*t),2),3/2))
        r_curvatura_pos = ((np.power(1+np.power(np.tan(ang)-g/(np.power(v0*np.cos(ang),2)*(x-x0)),2),3/2))/(np.abs(-g/np.power(v0*np.cos(ang),2))))
        r_curvatura_t = ((np.power(1+np.power(np.tan(ang)-g/v0*np.tan(ang)*t,2),3/2))/(np.abs(-g/np.power(v0*np.cos(ang),2))))
        centro_curvatura_x=x-(((np.tan(ang)-(g/np.power(v0*np.cos(ang),2))*(x-x0))*(1+np.power(np.tan(ang)-(g/np.power(v0*np.cos(ang)*(x-x0),2)),2)))/(-g/np.power(v0*np.cos(ang),2)))
        #centro_curvatura_y=
        centro_curvatura_xt= x0+v0*cos(ang)*t + (((1+tan(ang)-(g/v0*cos(ang))*t)*(1+np.power(tan(ang)- (g/v0*cos(ang))*t,2))) / (g/np.power(v0*cos(ang),2)))
        centro_curvatura_yt=y0+v0*sin(ang)*t-(1+np.power(tan(ang)-(g/v0*cos(ang))*t,2)*np.power(v0*cos(ang),2)/g)

        """
        print("Curvatura en tiempo X: "+str(curvatura_t))
        print("Curvatura en posicion: "+str(curvatura_pos))
        print("Radio en posicion: "+str(r_curvatura_pos))
        print("Radio en tiempo X:"+str(r_curvatura_t))
        print("Centro de curvatura pos x:" +str(centro_curvatura_x))
        print("Centro de curvatura X en T1:" + str(centro_curvatura_xt))
        print("Centro de curvatura Y en T1" + str(centro_curvatura_yt))
        """
        ##################

        # Crear POPUP NUEVO #

        popup = tk.Tk()
        popup.title("Radio y centro de curvatura")
        frame_top = ttk.Frame(popup)
        frame_mid = ttk.Frame(popup)
        frame_bot = ttk.Frame(popup)
        frame_top.pack(side=tk.TOP,fill=tk.BOTH,expand=True, padx=5, pady=5)
        frame_mid.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)
        frame_bot.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)
        validacion_tiempo = (frame_bot.register(check), '%v', '%P')
        intervaloLabel = ttk.Label(frame_top, text="Intervalo de tiempo").pack(side=tk.TOP,expand=True)
        tiempoInicioEntry = ttk.Entry(frame_top, justify='center')
        tiempoFinalEntry = ttk.Entry(frame_top, justify='center')
        tiempoLabel = ttk.Label(frame_bot, text="Tiempo: ").pack(side=tk.LEFT,fill=tk.BOTH, expand=True, padx=5, pady=5)
        tiempoInicioEntry.insert(0,"0")
        tiempoInicioEntry.configure(state='readonly')
        tiempoInicioEntry.pack(side=tk.LEFT,expand=True,padx=5,pady=5)
        tiempoFinalEntry.insert(0,time_impact(self))
        tiempoFinalEntry.configure(state='readonly')
        tiempoFinalEntry.pack(side=tk.LEFT,expand=True,padx=5,pady=5)
        tiempoUsuarioEntry = ttk.Entry(frame_bot,validate="key",validatecommand=validacion_tiempo)
        tiempoUsuarioEntry.pack(side=tk.LEFT,expand=True)
        botonAceptar = ttk.Button(frame_bot,text="Aceptar")
        botonAceptar.pack(side=tk.BOTTOM,expand=1,fill=tk.BOTH)
        botonAceptar.bind("<Button-1>",copiarTiempo)




        """
        ########## RADIO BUTTONS
        v = tk.IntVar()
        radioB1 = tk.Radiobutton(popup, text="Tiempo", variable=v, value=1, command=radioButtons())
        radioB2 = tk.Radiobutton(popup, text="Posicion", variable=v, value=2, command=radioButtons())
        ## PACK RADIOB
        radioB1.pack(side=tk.TOP, fill=tk.BOTH, expand=False, padx=5 , pady=5)
        radioB2.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=False, padx=5, pady=5)
        #tiempo = ttk.Label(frame_top)
        ########################
        """
        pass

    def boton_aceleracion_normal_y_tangencialf(self):
        # Ecuaciones para el calculo de la aceleracion normal y tangencial

        # Ecuacion aceleracion tangencial
        def a_tangencial(self):
            at = (((((self.velocidad_inicial * (cos(self.angulo)))) ** 2) + (
                    (((self.velocidad_inicial * (sin(self.angulo)))))
                    - self.gravedad * time_impact(self)) ** 2) / (
                          (sqrt(self.velocidad_inicial * cos(self.velocidad_inicial)) ** 2) +
                          (self.velocidad_inicial * sin(self.angulo) - (self.gravedad * time_impact(self)))))
            print(at)
            return at

        # Ecuacion aceleracion normal
        def a_normal(self):
            an = ((((self.velocidad_inicial * sin(self.angulo)) - (self.gravedad * time_impact(self))) / (
                    1 + (tan(self.angulo)
                         - ((self.gravedad) / self.velocidad_inicial * cos(self.angulo) * time_impact(
                        self)))) ** 3)) / abs((self.gravedad) /
                                              (self.velocidad_inicial * cos(self.angulo)) ** 2)
            print(an)
            return an

        # Pop up
        Pop_Up = tk.Tk()
        Pop_Up.title("Tiempo")
        Pop_Up.minsize(400, 300)

    def boton_vector_normalf(self):

        velocidad = int(self.entrada_Rapidez_inicial.get())
        angulo_inicial = int(self.entrada_angulo_inicial.get())
        nose=(self.gravedad*int(self.entrada_posicion_y0.get())/math.pow(velocidad,2))
        tiempo_maximov1=(velocidad/self.gravedad)*((math.sin(math.radians(angulo_inicial)))+math.sqrt(math.pow(math.sin(math.radians(angulo_inicial)),2)+2*nose))
        tiempo_maximo=tiempo_maximov1
        print (tiempo_maximov1)

        label = tk.Label(Pop_Up)
        label.pack()

        # Crea un cuadro que contiene los datos

        # Organiza los datos
        separador = ttk.Separator(Pop_Up, orient="horizontal")
        separador.pack(side=tk.TOP, expand=False, fill=tk.X)

        # Tiempo Impacto
        def time_impact(self):
            t = ((self.velocidad_inicial * sin(self.angulo)) / (2 * self.gravedad)) + ((1 / self.gravedad) * (
                sqrt(((self.velocidad_inicial * sin(self.angulo)) ** 2) + (2 * self.y0 * self.gravedad))))
            print(t)
            return t

            # Coordenada X

        def cord_x(self, t):
            x = self.x0 + ((self.velocidad_inicial * cos(self.angulo)) * t)
            return x

            # # Coordenada Y

        def cord_y(self, t):
            y = self.y0 + (((self.velocidad_inicial * (cos(self.angulo))) * t) - ((self.gravedad / 2) * (t ** 2)))
            return y

            # Altura máxima gráfica

        def altura_max(self):
            r = self.y0 + (((self.velocidad_inicial * (sin(self.angulo))) ** 2) / (self.gravedad))
            return r

            # Alcance maximo gráfica

        def alcance_max(self):
            alc = self.x0 + ((self.velocidad_inicial * sin(2 * self.angulo)) / (self.gravedad)) + \
                  ((self.velocidad_inicial * cos(self.angulo)) /
                   (self.gravedad)) * sqrt(
                ((self.velocidad_inicial * sin(self.angulo)) ** 2) + 2 * self.y0 * self.gravedad)
            return alc

        time_usuario = 1  # Tiempo ingresado(arreglar)

        # Grafica del tiempo ingresado
        time = np.arange(0, time_usuario, 0.01)
        x = cord_x(self, time)
        y = cord_y(self, time)

        # Grafica completa lanzamiento
        time_complete = np.arange(0, time_impact(self) + 4, 0.01)
        x2 = cord_x(self, time_complete)
        y2 = cord_y(self, time_complete)

        # Punto de posicion a medir
        x3 = cord_x(self, time_usuario)
        y3 = cord_y(self, time_usuario)

        # Detalles gráfica
        mpl.title("Aceleracion normal y tangencial")
        mpl.xlim(0, alcance_max(self) + self.x0)
        mpl.ylim(0, altura_max(self) + self.y0)
        mpl.xlabel("Distancia")
        mpl.ylabel("Altura")

        # Generación curvas
        mpl.plot(self.x0, self.y0, "k-o")  # Posición inicial
        mpl.plot(x, y, "y-")  # Curva
        mpl.plot(x2, y2, "k--")  # Lanzamiento
        # mpl.plot(x3, y3, "r-o")  # Punto ingresado  #Punto rojo de altura maxima
        mpl.grid()  # Cuadriculacion del grafico

        # Generación de las flechas para aceleración normal y tangencial
        # >>>>Genera bien las flechas y texto, pero tira un warning. Falta arreglar<<<<
        ax = mpl.axes()
        ax1 = mpl.axes()
        ax.text(15.4, 10.8, 'an', fontsize=9)  # Texto aceleracion normal
        ax.arrow(x3, y3, 0, -4, head_width=0.5, head_length=1, fc='k', ec='k')  # Flecha de aceleracion normal
        ax.text(18.7, 13.7, 'at', fontsize=9)  # Texto aceleracion tangencial
        ax1.arrow(x3, y3, 5, 0, head_width=0.5, head_length=1, fc='k', ec='k')  # Flecha de aceleracion tangencial

        # Muestra el grafico
        mpl.plot()
        mpl.show()
        pass

    def boton_vector_normalf(self):
        Pop_Up = tk.Tk()
        Pop_Up.title("Rango Tiempo")
        Pop_Up.minsize(400, 300)
        L1 = tk.Label(Pop_Up, text="Eliga Tiempo a Evaluar")
        E1 = tk.Entry(Pop_Up, bd=5)
        E1.pack()
        posicion = ttk.Frame(L1)
        posicion.pack(side=tk.LEFT, expand=True, padx=5, pady=5)
        E1 = ttk.Entry(posicion, justify=tk.CENTER)
        E1.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        E1.insert(tk.END, "5")
        L1.pack()
        label = tk.Label(Pop_Up)
        label.pack()
        frame_arriba = ttk.Frame(Pop_Up)
        hola = round(tiempo_maximov1,2)
        strhola= str(hola)
        inter = "Intervalo de tiempo= [0, "
        suma=inter+strhola+"]"

        frame_arriba.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=5, pady=5)
        tiempo_init = ttk.Label(frame_arriba, text=suma)
        tiempo_init.pack(side=tk.TOP)
        tiempo_init_x = ttk.Entry(frame_arriba, state='readonly', justify='center')
        tiempo_init_x.insert(0, "0")
        button = ttk.Button(Pop_Up, text='Evaluar', width=10, command=Pop_Up.destroy)

        button.pack(side=tk.BOTTOM)



        #  inicializa la ventana popup
        tiempofinal= 20
        xo = int(self.entrada_posicion_x0.get())
        yo = int(self.entrada_posicion_y0.get())
        vxo = velocidad * math.cos(math.radians(angulo_inicial))
        vyo = velocidad * math.sin(math.radians(angulo_inicial))
        plt.title("Vector Normal")
        plt.xlabel("-X-")
        plt.ylabel("-Y-")
        x = np.arange(0, tiempo_maximo, 0.001)
        x1 = 3
        h = math.sin(math.radians(int(angulo_inicial)))
        j = math.cos(math.radians(int(angulo_inicial)))
        vxo = 15
        vyo = 90
        angulo_inicial =self.entrada_angulo_inicial.get()
        mpl.title("Vector Normal")
        mpl.xlabel("-X-")
        mpl.ylabel("-Y-")
        x = np.arange(0, tiempofinal, 0.001)
        print(E1.get())
        x1 = 5
        h = math.sin(math.degrees(angulo_inicial))
        j = math.cos(math.degrees(angulo_inicial))
        print (h)
        x1=2
        y = yo + vyo * x + (1 / 2) * -9.8 * x ** 2
        z = xo + vxo * x + (1 / 2) * 0 * x ** 2
        y1 = yo + vyo * x1 + (1 / 2) * -9.8 * x1 ** 2
        z1 = xo + vxo * x1 + (1 / 2) * 0 * x1 ** 2


        vector_velocidadx= (vxo*x1)
        vector_velocidady = (vyo * h-(9.8*x1))
        plt.plot(z, y,"-")
        plt.plot(vector_velocidadx+z1, vector_velocidady+y1, "-o")
        plt.plot((vector_velocidady+z1), (vector_velocidadx), "-o")
        plt.plot(z1, y1, "-o")
        plt.show()

        mpl.plot(z, y,"-")
        mpl.plot(vector_velocidadx+z1, vector_velocidady+y1, "-o")
        mpl.plot((vector_velocidady+z1), (vector_velocidadx), "-o")
        mpl.plot(z1, y1, "-o")
        mpl.show()
        pass
    def actualizar_grafico(self,ecuacion_x,ecuacion_y):
        self.figura.clear() # Refresca el gráfico