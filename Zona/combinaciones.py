def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def mostrar(lista):
    for i in range(lista):
        print(lista[i])

if __name__ == "__main__":
    print("hola mundo")
    x = factorial(9)
    print(x)
    a = ("a","b","c")
    print(a[0])