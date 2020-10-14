#• E1: Escribir un programa que pida al usuario ingresar un número positivo, mientras el número ingresado no sea positivo, mostrar un
#mensaje de error y pedir al usuario que vuela a ingresar un número.
num1 = int(input("ingrese, un numero positivo: "))
while num1 < 0:
    print("error")
    num1=int (input("ingrese,un numero nuevo: "))
