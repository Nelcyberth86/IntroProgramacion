#desarrolle un programa que entregue la seduencia de collatz de un numero entero
n = int(input("ingrese un numero entero: "))
valor = int(float(n))
asterisco= "*"
while valor > 1 :
    if valor % 2 == 0:
        valor = valor / 2
        valor=int(float(valor))
        print(valor)

    else:
        valor = (valor * 3) + 1
        valor = int(float(valor))
        print(valor)





