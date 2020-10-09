entero1= int(input("ingrese, un numero entero: "))
entero2 = int(input("ingrese un numero entero: "))
variable= 0
for i in range(abs(entero1+1),abs(entero2)):
    variable = variable + i
print(f"la suma entre ellos es {variable}")


