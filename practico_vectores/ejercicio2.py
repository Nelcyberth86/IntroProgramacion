#Diseñar un programa que lea como entrada dos vectores de tamaño 5 y devuelva el vector suma.
#Ejemplo: si tenemos los vectores V1 = (a1, a2, …, a5) y V2 = (b1, b2, …, b5) el vector suma se define como el vector obtenido
#de sumar componente a componente: V1 + V2 = (a1+ b1, a2+ b2, …, a5+ b5).
#import array as np

v1 = []
v2 = []
suma = []

print("llene el primer vector")
for i in range(0,5):
    num1 = int(input("ingrese un caracter: "))
    v1.append(num1)

print("llene el segundo vector")
for i in range(0, 5):
    num2 = int(input("ingrese un caracter:"))
    v2.append(num2)
suma=[]
print("suma de los vectores")
for i in range(0,5):
    num=v1[i]+v2[i]
    suma.append(num)
print(v1)
print(v2)
print(suma)



