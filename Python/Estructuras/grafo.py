from cola import *
from pila import *

class grafo:
    vertices = None
    aristas = None
    adyacentes = None

    def __init__(self,vertices):
        self.vertices = vertices
        self.vertices = []
        for u,v in vertices:
            if u not in self.vertices:
                self.vertices.append(u)
            if v not in self.vertices:
                self.vertices.append(v)
        self.vertices.sort()

    def obtener_adyacentes(self):
        self.adyacentes = {}
        for i in self.vertices:
            adyacentes_i = []
            for u,v in self.vertices:
                if i == u:
                    adyacentes_i.append(v)
                if i == v:
                    adyacentes_i.append(u)
            self.adyacentes.update({i:adyacentes_i})

    def busqueda_profundidad(self,inicio):
        if inicio not in self.vertices:
            return None
        if self.adyacentes == None:
            self.obtener_adyacentes()
        una_pila = pila()
        una_pila.apilar(inicio)
        visitados = []
        ruta = []
        while una_pila.esta_vacia() != True:
            vertice = una_pila.desapilar()
            for i in self.adyacentes[vertice]:
                if i not in visitados:
                    visitados.append(i)
                    una_pila.apilar(i)
                    ruta.append((vertice,i))
        return ruta

    def busqueda_anchura(self,inicio):
        if inicio not in self.vertices:
            return None
        if self.adyacentes == None:
            self.obtener_adyacentes()
        una_cola = cola()
        una_cola.encolar(inicio)
        visitados = []
        ruta = []
        while una_cola.esta_vacia() != True:
            vertice = una_cola.desencolar()
            for i in self.adyacentes[vertice]:
                if i not in visitados:
                    visitados.append(i)
                    una_cola.encolar(i)
                    ruta.append((vertice, i))
        return ruta

    def busqueda_full_combinacion(self,inicio):
        if inicio not in self.vertices:
            return None
        if self.adyacentes == None:
            self.obtener_adyacentes()
        una_pila = pila()
        una_pila.apilar(inicio)
        while una_pila.esta_vacia() != True:
            cima = una_pila.obtener_cima()
            for i in self.adyacentes[cima]:
