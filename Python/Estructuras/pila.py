class pila:
    la_pila = None

    def __init__(self):
        self.la_pila = []

    def apilar(self,nuevo_elemento):
        self.la_pila.append(nuevo_elemento)

    def desapilar(self):
        if self.la_pila == []:
            return None
        else:
            ultimo_indice = len(self.la_pila) - 1
            cima = self.la_pila[ultimo_indice]
            self.la_pila.pop(ultimo_indice)
            return cima

    def obtener_largo(self):
        if self.la_pila == None:
            return 0
        return len(self.la_pila)

    def obtener_cima(self):
        if self.la_pila == None:
            return None
        ultimo_indice = self.obtener_largo() - 1
        return self.la_pila[ultimo_indice]

    def esta_vacia(self):
        if self.la_pila == []:
            return True
        return False