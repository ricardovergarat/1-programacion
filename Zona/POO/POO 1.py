class auto():
    # atributos
    largo_chasis = 0
    ancho_chasis = 0
    ruedas = 4
    aranque = False
    # metodos
    def acelerar(self):
        self.aranque = True

    def mostrar_auto(self):
        print("largo chasis: ",self.largo_chasis)
        print("ancho chasis: ",self.ancho_chasis)
        print("Nuemreo de ruendas: ",self.ruedas)
        print("Aranque: ",self.aranque)

if __name__ == "__main__":
    print("stars")
    un_auto = auto()
    un_auto.mostrar_auto()
    un_auto.acelerar()
    un_auto.mostrar_auto()