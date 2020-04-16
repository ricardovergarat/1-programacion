
def abrir_varios_archivos(lista):
    datos_todos_los_archivos = []
    for i in range(len(lista)):
        try:
            print(lista[i])
            datos_archivos = abrir_archivo(lista[i])
            #mostrar_lista(datos_archivos)
            datos_todos_los_archivos.append(datos_archivos)
        except:
            datos_todos_los_archivos.append(["error"])
    return datos_todos_los_archivos

def abrir_archivo(nombre):
    archivo = open(nombre)
    lineas = archivo.readlines()
    lineas = quitar_enter(lineas)
    return lineas

def quitar_enter(lista):
    for i in range(len(lista)):
        lista[i] = lista[i].replace("\n","")
    return lista

def mostrar_lista(lista):
    for i in range(len(lista)):
        print(lista[i],"            ",i)



if __name__ == "__main__":
    x = ["Cleopatra.txt","Drake.txt","Estarossa.txt","Ganicus.txt","King.txt","Leonidas.txt","Odin.txt","asdasd.txt"]
    L = abrir_varios_archivos(x)
    #abrir_archivo("Odin.txt")