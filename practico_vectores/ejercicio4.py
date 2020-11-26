#Crea una aplicación que pida un numero por teclado y después comprobaremos si el numero introducido es capicua,
# es decir, que se lee igual sin importar la dirección. Por ejemplo, si introducimos 30303 es capicua,
# si introducimos 30430 no es capicua. Piensa como puedes dar la vuelta al número.Una forma es dividiendolo entre 10 y
# sacando unidad por unidad. Otra es pasarlo a String y revisar posición por posición.


num=int(input("ingrese un numero: "))
num1=str(num)[::-1]
if str(num)==num1:
    print("es capicua", num)
else:
    print("no es capicua")


