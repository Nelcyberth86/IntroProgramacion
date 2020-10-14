#escriba un programa que genere todas laspotencias de 2, desde 0-esimas hasta la ingresada por el usuario
num= int(input("ingrese,numero: "))
for i in range (0,abs(num)+1) :
   if num<0 :
      print(2**-i)
   else:
      print(2**i)


