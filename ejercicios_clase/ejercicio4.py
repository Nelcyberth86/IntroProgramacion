import math
puntoAx=int(input("ingrese punto a en x: "))
puntoAy=int(input("ingrese punto a en y: "))
puntoBy=int(input("ingrese punto b en y: "))
puntoCx=int(input("ingrese punto c en x: "))
puntoBx=puntoAx
puntoCy=puntoAy
base= puntoCx - puntoAx
altura= puntoBy-puntoAy
hipotenusa=math.sqrt(base**2 + altura**2)
area= base * altura / 2
perimetro= base + altura +hipotenusa
print("el perimetro del triangulo rectangulo es. " , perimetro)
print("el area del triangulo rectangulo es. " , area)
