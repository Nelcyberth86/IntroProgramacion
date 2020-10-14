#desarrolle un programa que grafique los largos de la secuencia de collatz de los numeros enteros positivos ,menores ingresado por el usuario
n = int(input("ingrese un numero entero: "))
valor = int(float(n))
asterisco= "*"
while valor > 1 :
    if valor % 2 == 0:
        valor = valor / 2
        valor=int(float(valor))

    else:
        valor = (valor * 3) + 1
        valor = int(float(valor))

    print("*" * valor)
