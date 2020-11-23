#Diseñar un programa que almacene en  un vector llamado FACT, el factorial de los primeros 20 números naturales.
# FACT = {1!, 2!, 3!, … 20!} . Debe diseñar una función que calcule el factorial de un número, por lo tanto,
#esta función tiene un parámetro y DEVUELVE (o retorna) un valor.
def factorial(n):
    FACT = []
    factorial = 1
    for i in range(1,n):
        factorial = factorial * i
        FACT.append(factorial)
    print(FACT)
numero=int(input("Ingrese un numero por favor: "))

num=factorial(numero)
