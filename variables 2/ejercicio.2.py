#• E2: Leer dos números enteros por teclado, dividendo y divisor, y mostrar el resto de la división en pantalla.
dividendo = int(input("ingresa, numero dividendo: "))
divisor= int(input("ingresa; numero divisor: "))
resto =( dividendo/divisor )
mensaje = f"El resto obtenido al dividir {dividendo} entre {divisor} es {round(resto),2} "
print(mensaje)