#• E8: Escribir un programa que lea del teclado un monto a invertir, el interés anual y el número de años a invertir
monto = int(input("ingrese, monto : "))
interes = int(input("ingrese, el interes : "))
años = int(input("ingrese, el numero de años : "))

ganancia_neta = int(monto) *int(1 + interes) ** int(años)
print(ganancia_neta)


