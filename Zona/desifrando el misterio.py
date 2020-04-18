import math

def evaluar_numero(n):
    resultado = (n * n) + ((n + 1) * (n + 1))
    return resultado

def es_primo(n):
    if n <= 1:
        return False # el 1 y numeros menores no son primos
    else:
        antecesor = n - 1
        while antecesor != 1:
            resto = n % antecesor
            if resto == 0:
                return False # esto implcia que existe un multiplo, es dicr NO es primo
            antecesor = antecesor - 1
        return True # implica que no tuvo ningun multiplo, es decir es primo


def generar_primos(n):
    cantidad_elementos = 0
    primos = []
    x = 0
    while cantidad_elementos != n:
        n_es_primo = es_primo(x)
        if n_es_primo == True:
            primos.append(x)
            cantidad_elementos = cantidad_elementos + 1

        #print("x es: ", x, "      ", n_es_primo,"    cantidad:",cantidad_elementos   )
        x = x + 1
    print(primos)

def algoritmo(n):
    cantidad_primos = 0
    numero_infinito = 1
    registro = []
    while cantidad_primos <= n:
        evaluado = evaluar_numero(numero_infinito)
        evaluado_es_primo = es_primo(evaluado)
        if evaluado_es_primo == True:
            registro.append(evaluado)
            cantidad_primos = cantidad_primos + 1
        numero_infinito = numero_infinito + 1
    print(registro)


if __name__ == "__main__":
    print("star")
    #generar_primos(85)
    algoritmo(85)

