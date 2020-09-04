def redondear(n,cantidad_decimales):
    n = redondear(n,cantidad_decimales)
    return n

def obtener_promedio(lista):
    sumatoria = 0
    for i in range(len(lista)):
        sumatoria = sumatoria + lista[i]
    promedio = sumatoria / len(lista)
    promedio = redondear(promedio,1)
    return promedio