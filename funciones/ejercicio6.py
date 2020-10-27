# Definir una función es_palindromo() que reconoce palíndromos (es decir, palabras que
#tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.
def palindromo(palabra):
    tam = len(palabra)
    aux= tam -1
    contador = 0

    for i in range(0,tam):
        if (palabra[i] == palabra[aux]):
            contador = contador + 1
        aux=aux-1

    if (contador == tam):
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")


palabra = input("Ingrese una palabra: ")
palindromo(palabra)
