#E4: Escribir un programa que calcule la suma de todos los números entre 1 y un número ingresado por teclado.
num = int(input("ingrese,un numero: "))
suma= 0
while num > 0 :
    suma= suma + num
    num = num-1
    print(suma)