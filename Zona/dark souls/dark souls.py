
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

def encontrar(lista,buscador):
    for i in range(len(lista)):
        x = lista[i].find(buscador)
        if x != -1:
            return i

def recuperar_niveles_poder(lista,indice):
    print("entro")
    x = indice
    y = x + 7
    niveles_poder = []
    while x != y:
        if x == indice:
            separado = lista[x].split("=")
        else:
            separado = lista[x].split("---")
        print("separado es:",separado)
        poder = float(separado[1])
        poder = int(poder) * 1000
        niveles_poder.append(poder)
        x = x + 1
    return niveles_poder

def obtener_tabla_individual():
    tabla = []
    for i in range(4):
        if i == 0:
            casilla = [0,i]
            casilla = str(casilla)
            casilla = casilla.replace(" ","")
            tabla.append(casilla)
        else:
            casilla = [0,i]
            inversa = casilla[::-1]
            casilla = str(casilla)
            casilla = casilla.replace(" ","")
            inversa = str(inversa)
            inversa = inversa.replace(" ","")
            tabla.append(casilla)
            tabla.append(inversa)
    return tabla

def obtener_suma_tabla_individual(tabla_vacia,niveles_poder):
    for i in range(len(tabla_vacia)):
        if i == 0:
            numero_convertido = convertir_nuumero_a_string(niveles_poder[i])
            tabla_vacia[i] = tabla_vacia[i] + " = " + numero_convertido
        else:
            poder_sumado = convertir_nuumero_a_string(niveles_poder[0] + niveles_poder[i])
            poder_arma = convertir_nuumero_a_string(niveles_poder[i])
            tabla_vacia[i] = tabla_vacia[i] + " = " + poder_sumado + " --- " + poder_arma
    return tabla_vacia

def obtener_tabla_sumatoria_poder():
    todas_las_combinaciones = []
    for i in range(3):
        for j in range(3):
            combinacion = [i + 1,j + 1]
            string_combinacion = str(combinacion)
            string_combinacion = string_combinacion.replace(" ","")
            todas_las_combinaciones.append(string_combinacion)
    return todas_las_combinaciones

def obtener_tabla_sumada(tabla_comvinacion,niveles_de_poder):
    for i in range(len(tabla_comvinacion)):
        cordenada = tabla_comvinacion[i].replace("[","")
        cordenada = cordenada.replace("]","")
        cordenada = cordenada.split(",")
        x = int(cordenada[0])
        y = int(cordenada[1])
        x = x * 2
        y = 1 + (2*(y -1))
        total = niveles_de_poder[0] + niveles_de_poder[x] + niveles_de_poder[y]
        total = convertir_nuumero_a_string(total)
        tabla_comvinacion[i] = tabla_comvinacion[i] + " = " + total
    return tabla_comvinacion

def convertir_nuumero_a_string(n):
    cantidad = len(str(n))
    cantidad_puntos = int(cantidad / 3) # 3 por que cada 3 numeros hay un punto en un numero
    resto = cantidad % 3
    if resto == 0:
        cantidad_puntos = cantidad_puntos - 1
    numero_descompuesto = list(str(n))
    indice = (cantidad - (cantidad_puntos * 3)) - 1
    for i in range(cantidad_puntos):
        numero_descompuesto[indice] = numero_descompuesto[indice] + "."
        indice = indice + 3 # mas 3 por que como dijimos cada 3 numeros se agrega un punto en los nuemros
    numero_compuesto = ""
    for i in range(len(numero_descompuesto)):
        numero_compuesto = numero_compuesto + numero_descompuesto[i]
    return numero_compuesto

def ordenar_poder(lista):
    niveles = []
    for i in range(len(lista)):
        x = lista[i].split(" ")
        n = float(x[2])
        n = int(n) * 1000
        niveles.append(n)
    ordenado = False
    while ordenado != True:
        x = 0
        while x != len(niveles) - 1:
            if niveles[x] > niveles[x + 1]:
                respaldo = niveles[x + 1]
                niveles[x + 1] = niveles[x]
                niveles[x] = respaldo
                respaldo_lista_2 = lista[x + 1]
                lista[x + 1] = lista[x]
                lista[x] = respaldo_lista_2
            x = x + 1
        ordenado = esta_ordenada(niveles)
    return lista

def esta_ordenada(lista):
    x = 0
    while x != len(lista) - 1:
        if lista[x] > lista[x + 1]:
            return False
        x = x + 1
    return True

def remplazar_indices(a,b,lista_original,lista_a_remplazar):
    x = 0
    while a <= b:
        lista_original[a] = lista_a_remplazar[x]
        x = x + 1
        a = a + 1
    return lista_original

def auto_completar(lista):
    datos_completados = []
    for i in range(len(lista)):
        print(lista[i])
        indice_busqueda = encontrar(lista[i], "[0,0]")
        print(indice_busqueda)
        niveles_poder_armas = recuperar_niveles_poder(lista[i], indice_busqueda)
        tabla_individual = obtener_tabla_individual()
        tabla_individual = obtener_suma_tabla_individual(tabla_individual, niveles_poder_armas)
        tabla_comvinacion = obtener_tabla_sumatoria_poder()
        tabla_comvinacion = obtener_tabla_sumada(tabla_comvinacion, niveles_poder_armas)
        tabla_comvinacion = ordenar_poder(tabla_comvinacion)
        lista[i] = remplazar_indices(indice_busqueda, indice_busqueda + 6, lista[i], tabla_individual)
        indice_busqueda = encontrar(lista[i], "[1,1]")
        lista[i] = remplazar_indices(indice_busqueda, indice_busqueda + 8, lista[i], tabla_comvinacion)
        datos_completados.append(lista[i])
    return datos_completados

def escribir_varios_archivos(nombres_archivos,lista):
    for i in range(len(lista)):
        escribir_archivo(nombres_archivos[i],lista[i])


def escribir_archivo(nombre,lista):
    archivo = open(nombre,"w")
    for i in range(len(lista)):
        archivo.write(lista[i] + "\n")
    archivo.close()



if __name__ == "__main__":
    nombres_archivos = ["Cleopatra.txt","Drake.txt","Estarossa.txt","Ganicus.txt","King.txt","Leonidas.txt","Odin.txt"]
    contenido_archivos = abrir_varios_archivos(nombres_archivos)
    contenido_archivos = auto_completar(contenido_archivos)
    print(contenido_archivos)
    escribir_varios_archivos(nombres_archivos,contenido_archivos)
    #print(L)


