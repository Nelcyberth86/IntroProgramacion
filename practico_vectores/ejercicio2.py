#Diseñar un programa que lea como entrada dos vectores de tamaño 5 y devuelva el vector suma.
#Ejemplo: si tenemos los vectores V1 = (a1, a2, …, a5) y V2 = (b1, b2, …, b5) el vector suma se define como el vector obtenido
#de sumar componente a componente: V1 + V2 = (a1+ b1, a2+ b2, …, a5+ b5).
#import array as np
num1=input("ingrese un caracter:")
num2=input("ingrese un caracter:")


v1 = [num1]*5
v2 = [num2]*5
suma = []

for i in range(len(v1)):
    suma.append(v1[i] + v2[i])

print(suma)