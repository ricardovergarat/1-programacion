class mapa():
    matrix = []

    def __init__(self,x,y):
        self.matrix = []
        for i in range(y):
            fila = []
            for i in range(x):
                fila.append("-")
            self.matrix.append(fila)

    def mostrar_mapa(self):
        for i in range(len(self.matrix)):
            self.mostrar_fila(len(self.matrix[i]),i)

    def mostrar_fila(self,largo,numero_fila):
        string_fila = ""
        for i in range(largo):
            string_fila = string_fila +  self.matrix[numero_fila][i]
        print(string_fila)

    def agregar_objeto(self,tamaño,x,y,caracter):
        x = x - 1
        y = y - 1
        for i in range(tamaño):
            for j in range(tamaño):
                self.matrix[i + y][j + x] = caracter
