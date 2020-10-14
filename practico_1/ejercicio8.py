# escriba un programa que pida al usuario dos numerosenteros yluego entregue la suma de todos los numeros que estan entre
#entre ellos
entero1= int(input("ingrese, un numero entero: "))
entero2 = int(input("ingrese un numero entero: "))
variable= 0
for i in range(abs(entero1+1),abs(entero2)):
    variable = variable + i
print(f"la suma entre ellos es {variable}")


