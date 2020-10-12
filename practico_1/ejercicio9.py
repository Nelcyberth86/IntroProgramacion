# escriba un programa que simula una calculadora basica, este puede realizar operacion de suma,reta,multiplicacion y division
num = int(input("ingrese numero: "))
num1 = int(input("ingrese, numero: "))
suma = num + num1
resta = num - num1 or str("-")
multiplicacion = num * num1 or str("*")
division = num / num1 or str(" / ")
operador= str(input("ingrese la operacion que desea, tener: "))
a= suma
b=resta
c= multiplicacion
d = division

if operador == c:
    print(f"la multiplicacion de {num} por {num1}  es {multiplicacion}")
elif operador \
        == d:
    print(f"la division de {num} y {num1} es {division} ")
elif operador== a:
    print(suma)
elif operador == b:
    print(f"la resta de {num} y {num1} es {resta} ")



