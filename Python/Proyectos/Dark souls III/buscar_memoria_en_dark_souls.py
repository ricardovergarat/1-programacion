def abrir_archivo(nombre):
    archivo = open(nombre)
    datos = archivo.readlines()
    datos = quitar_enter(datos)
    archivo.close()
    return datos

def quitar_enter(lista):
    for i in range(len(lista)):
        lista[i] = lista[i].replace("\n","")
    return lista

def separar_nombre_y_memoria(lista):
    for i in range(len(datos)):
        lista[i] = [ datos[i][0:8],datos[i][9:len(datos[i])] ]
    return lista

def quitar_espacio_incesesario(lista):
    for i in range(len(lista)):
        while lista[i][1][len(lista[i][1]) - 1] == " ": # si el ultimo caracter es " " regresamos hasta el penultimo caracter
            lista[i][1] = lista[i][1][0: len(lista[i][1]) - 1]
    return lista

def pedir_busqueda():
    entrada = input("Ingrese el nombre del objeto a buscar ")
    entrada = entrada.lower()
    return entrada

def buscar_objeto(lista,nombre):
    for i in range(len(lista)):
        if nombre == lista[i][1].lower():
            busqueda = "La memoria de " + nombre.upper() + " es: " + lista[i][0]
            return busqueda
    return "No se encontro el objeto: " + nombre.upper()

if __name__ == "__main__":
    datos = abrir_archivo("memoria_dark_souls.txt")
    datos = separar_nombre_y_memoria(datos)
    datos = quitar_espacio_incesesario(datos)
    nombre = pedir_busqueda()
    resultado = buscar_objeto(datos,nombre)
    print(resultado)