





if __name__ == "__main__":
    print("star")
    x = {"a","b","c","d"}
    X = {'a', 'b', 'c', 'd'}
    R = {('a', 'b'), ('b', 'c'),('c', 'a'), ('a', 'a'),('b', 'b'), ('c', 'c'),('b', 'a'), ('c', 'b'), ('c', 'd'), ('d', 'c'),('a', 'c'), ('d', 'a'), ('a', 'd'), ('d', 'd')}
    print(x)
    for a in x:
        for b in x:
            print("b: ",b,"     a: ",a, "en: ", X)
    producto_cartesiano = lambda X: {(a, b) for a in X for b in X}
    G = producto_cartesiano(X)

    print(G)