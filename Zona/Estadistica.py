def tabla(datos,cantidad):
    print("dato     cantidad     f     facum       p      pcaum")
    total = obtener_total(cantidad)
    f_acumulado = 0
    p_acumulado = 0
    for i in range(len(datos)):
        f = frecuencia(total,cantidad[i])
        print(datos[i],"    ",cantidad[i],"     ",f,"   ",f + f_acumulado,"     ",int(f * 100),"%   ",int((f + f_acumulado) * 100),"%")
        f_acumulado = f + f_acumulado

def obtener_total(lista):
    sumatoria = 0
    for i in range(len(lista)):
        sumatoria = sumatoria + lista[i]
    return sumatoria

def redondear(numero,cantidad_de_decimales):
    numero = round(numero, cantidad_de_decimales)
    return numero

def frecuencia(total,cantidad):
    frecuencia_dato = cantidad / total
    frecuencia_dato = redondear(frecuencia_dato,1)
    return frecuencia_dato

if __name__ == "__main__":
    datos = ["]0,10[","]10,20[","]20,30["]
    cantidad = [45,23,97]
    tabla(datos,cantidad)