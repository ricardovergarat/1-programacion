
def esta_vacia(pila):
    if pila == []:
        return True
    return False

def apilar(pila,elemento):
    pila.append(elemento)
    # la sima es el de derecha
    return pila

def desapilar(pila):
    if esta_vacia(pila) == True:
        return []
    return pila[0:len(pila) - 1]

def invertir_cola(pila):
    return pila[::-1]

def concatenar_cola(pila_1,pila_2):
    return pila_1 + pila_2

if __name__ == "__main__":
    # aqui las pruebas
    p = [2,4,7,1,452]
    p = apilar(p,76)
    print(p)
    p = desapilar(p)
    print(p)