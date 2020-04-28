
def esta_vacia(lista):
    if lista == []:
        return True
    return False

def agregar_elemento(lista,elemento,indice):
    lista.insert(indice,elemento)
    # si pone un indice que aun n oexiste cambia el ultimo elemento
    return lista

def agregar_elemento_final(lista,elemento):
    return lista.append(elemento)

def quitar_elemento(lista,indice):
    lista.pop(indice)
    return lista

def quitar_ultimo_elemento(lista):
    return lista[0:len(lista) - 1]

def invertir_lista(lista):
    return lista[::-1]

def concatenar_lista(lista_1,lista_2):
    return lista_1 + lista_2

if __name__ == "__main__":
    l = [2,4,6,8,10]
    l = agregar_elemento(l,33,8)
    print(l)
    l = quitar_ultimo_elemento(l)
    print(l)