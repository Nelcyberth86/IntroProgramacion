# escribe un programa que entregue todos los divisores del numero entero ingresado
num=int(input("ingrese,numero: "))
for i in range(1,num+1):
    if num % i == 0:
        print(i)
