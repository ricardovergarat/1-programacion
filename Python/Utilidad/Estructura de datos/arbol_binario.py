import os

class nodo():
    izquierda = None
    centro = None
    derecha = None

    def __init__(self,dato):
        self.centro = dato

    def obtener_izquieda(self):
        return self.izquierda

    def obtener_centro(self):
        return self.centro

    def obtener_derecha(self):
        return self.derecha

    def agregar_izquierda(self,dato):
        self.izquierda = dato

    def agregar_derecha(self,dato):
        self.derecha = dato

    def obtener_expresion(self):
        if (self.izquierda == None) and (self.derecha == None):
            return [self.centro]
        if (self.izquierda != None) and (self.derecha == None):
            return [self.izquierda, self.centro, "_"]
        if (self.izquierda == None) and (self.derecha != None):
            return ["_", self.centro, self.derecha]
        else:
            return [self.obtener_expresion(), self.centro, self.obtener_expresion()]

    def mostrar_arbol(self):
        lista = self.obtener_expresion()
        print(lista)

    def agregar(self,dato):
        if ((self.izquierda != None) and (self.derecha != None)):
            # bajar de nodo
            lado = determinar_lado(self.centro,dato)
            if lado == 0:
                self.izquierda.agregar(dato)
            else:
                self.derecha.agregar(dato)
        else:
            lado = determinar_lado(self.centro,dato)
            if lado == 0:
                if self.izquierda == None:
                    self.agregar_izquierda(nodo(dato))
                else:
                    self.izquierda.agregar(dato)
            else:
                if self.derecha == None:
                    self.agregar_derecha(nodo(dato))
                else:
                    self.derecha.agregar(dato)

def determinar_lado(centro,dato):
    if dato <= centro:
        return 0
    return 1

if __name__ == "__main__":
    os.system("cls")
    arbol = nodo(40)
    arbol.mostrar_arbol()
    b = nodo(35)
    arbol.agregar_izquierda(b)
    arbol.mostrar_arbol()
    a = arbol.obtener_izquieda()
    print(a)