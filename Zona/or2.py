n = [32,534,35453,3123,4,13,65,9999,3123]
print(n)
ordenado = False
while ordenado != True:
    x = 0
    while x != len(lista) - 1:
        if lista[x] > lista[x + 1]:
            respaldo = lista[x + 1]
            lista[x + 1] = lista[x]
            lista[x] = respaldo
        x = x +1
    y = 0
    while y != len(lista) - 1:
        if lista[y] > lista[y + 1]:
            ordenado = False
            break
        else:
            ordenado = True
        y = y + 1
