#E2: Leer dos números enteros por teclado y mostrar el mayor de los
#dos por pantalla
num1 = int(input("ingrese,numero: "))
num2 = int(input("ingrese; numero : "))
if num1 < num2 :
    print(f"{num1} es menor a {num2}")
elif num1 == num2 :
    print(f"{num1} es igual {num2}")
else:
    print( f"{num1} es mayor que {num2}")