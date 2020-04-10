import time # esto te permite tener aceso a mas herramientas en python, en este caso pausar en programa unos segundos

def pedir_ponderacion(n):
    ponderacion = input("Ingrese la ponderacion " + str(n) + ": ")
    ponderacion = int(ponderacion)
    return ponderacion

def pedir_nota(n):
    nota = input("Ingrese la nota " + str(n) + ": ")
    nota = int(nota)
    return nota

def nota_con_ponderacion(nota,ponderacion):
    decimas = nota * (ponderacion / 100)
    return decimas

if __name__ == "__main__":
    print("inicio del programa")
    x = 0
    promedio = 0
    while x != 3:
        porcentaje = pedir_ponderacion(x + 1)
        nota_ingresada = pedir_nota( x + 1)
        decimas_conseguidas = nota_con_ponderacion(nota_ingresada,porcentaje)
        promedio = promedio + decimas_conseguidas
        x = x + 1
    print("Su nota final es: ",promedio)
    time.sleep(20) # aqui le dimos la orden de pausar 20 segundos el programa