num1 = int(input("ingrese numero: "))
num2 = int(input("ingrese, numero: "))
suma = "suma" or "+"
resta = "resta" or "-"
multiplicacion = "multiplicacion" or "*"
division= "division" or "/"
operacion = str(input("operacion, que decea realizar: "))
if operacion== suma or "+":
    resultado= num2 + num1
    print(resultado)
elif operacion == resta or "-":
    resultado = num1 - num2
    print(resultado)
elif operacion == multiplicacion or "*":
    resultado = num1 *num2
    print(resultado)
elif operacion == division or "/":
    resultado = num1 / num2
    print(resultado)
