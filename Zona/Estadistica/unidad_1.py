def obtener_promedio(lista):
    sumatoria = 0
    for i in range(len(lista)):
        sumatoria = sumatoria + lista[i]
    return sumatoria / len(lista)

def obtener_desviacion_estantar(lista,n):
    promedio = obtener_promedio(lista)
    sumatoria = 0
    for i in range(len(lista)):
        sumatoria = sumatoria + ( (lista[i] - promedio) * (lista[i] - promedio) )
    if n == 1:
        return sumatoria / len(lista)
    return sumatoria / (len(lista) - 1)