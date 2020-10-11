diaactual = int(input("ingrese, dia actual : "))
mesactual = int(input("ingrese, mes actual : "))
añoactual = int(input("ingrese, año actual : "))
dianacimiento = int(input("ingrese, dia de nacimiento: "))
mesnacimiento = int(input("ingrese, mes de nacimiento: "))
añonacimiento = int(input("ingrese, año de nacimiento: "))
edad = añoactual - añonacimiento
if dianacimiento<diaactual:
    print(f"usteda tiene {edad}")
else:
    edad= edad-1
    print(f"usted tiene {edad}")



