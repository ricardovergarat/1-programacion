
def esta_vacia(cola):
    if cola == []:
        return True
    return False

def encolar(cola,elemento):
    return cola.append(elemento)

def desencolar(cola):
    if esta_vacia(cola) == True:
        return []
    return cola[1:len(cola)]

def invertir_cola(cola):
    return cola[::-1]

def concatenar_cola(cola_1,cola_2):
    return cola_1 + cola_2

if __name__ == "__main__":
    c = [1,2,3,4,5,6]
    print(c[0:4])
    c = desencolar(c)
    print(c)