class cola:
    la_cola = None

    def __init__(self):
        self.la_cola = []

    def encolar(self,nuevo_elemento):
        self.la_cola.append(nuevo_elemento)

    def desencolar(self):
        if self.la_cola == []:
            return None
        else:
            cabeza = self.la_cola[0]
            self.la_cola.pop(0)
            return cabeza

    def esta_vacia(self):
        if self.la_cola == []:
            return True
        return False