#• E3: Leer el radio de un círculo por teclado y mostrar el área y perímetro del círculo en pantalla.
import math

radio= int(input("ingrese, el numero del radio de un circulo: "))
area= math.pi * radio**2
perimetro= 2* math.pi * radio
mensaje= f"la area del circulo es igual a: {area}. el perimetro del circulo es igual a: {perimetro}"
print(mensaje)