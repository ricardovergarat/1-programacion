import numpy as np
from numpy import *
from sympy import *
from math import pi
t = Symbol("t")
x =  t**2 
derivada = diff(x,t)
print(derivada)



derivada = derivada.subs(t,pi/2)
print(derivada)

vectores = np.linspace(0, 100,60)
print(vectores)


#derivado = ecuacion.diff(t)
#print(derivado)
#der2 = ecuacion.diff(t,2)
#print(der2)
#derm = - np.sin(t)
#print(derm)
#x = Symbol("x")
#ec = 2* x**3
#derivada = ec.diff(x)
#print(derivada) 