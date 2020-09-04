def redondear(n,cantidad_decimales):
    redondeo = round(n,cantidad_decimales)
    return redondeo

def obtener_nota(nota,porcentaje):
    porcentaje_real = porcentaje / 100
    decimas = nota * porcentaje_real
    return decimas

def obtener_promedio(lista):
    sumatoria = 0
    for i in range(len(lista)):
        sumatoria = sumatoria + lista[i]
    promedio = sumatoria / len(lista)
    promedio = redondear(promedio,1)
    return promedio

def obtener_promedio_final(notas,porcentajes):
    sumatoria = 0
    for i in range(len(notas)):
        decimas = obtener_nota(notas[i],porcentajes[i])
        sumatoria = sumatoria + decimas
    sumatoria = redondear(sumatoria,1)
    return sumatoria

if __name__ == "__main__":
    taller = [6.4,5.2,4.5]
    promedio_taller = obtener_promedio(taller)
    print(promedio_taller)
    parciales = [4.6,3.2,4.3,5.7]
    promedio_notas = obtener_promedio(parciales)
    print(promedio_notas)
