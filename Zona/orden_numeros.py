
def ordenar(lista):
    ordenado = False
    while ordenado != True:
        x = 0
        while x != len(lista) - 1:
            if lista[x] > lista[x + 1]:
                respaldo = lista[x + 1]
                lista[x + 1] = lista[x]
                lista[x] = respaldo
            x = x +1
        ordenado = esta_ordenada(lista)
    return lista


def esta_ordenada(lista):
    x = 0
    while x != len(lista) - 1:
        if lista[x] > lista[x + 1]:
            return False
        x = x + 1
    return True


if __name__ == "__main__":
    print("starts")
    n = [32,534,35453,3123,4,13,65,9999,3123]
    print(n)
    n = ordenar(n)
    print(n)

