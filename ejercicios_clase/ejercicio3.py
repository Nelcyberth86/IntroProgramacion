#desarollar un logaritno que solicite,tamaño en x y y para dimensionar un rectangulo ocuadrado,posteriormente
# solicutar un conjunto,etc
tamañox= int(input("ingrese tamaño en x: "))
tamañoy= int(input("ingrese tamaño en y: "))
ingresarcirculo=5
diametro=[]
print("radio de circulos")
multi=1

while ingresarcirculo != 0:
    ingresarcirculo = int(input("ingrese los radios de un circulo: "))
    if ingresarcirculo !=0:
     multi = multi * ingresarcirculo
    diametro.append(ingresarcirculo)


if tamañox == tamañoy:
    area=tamañoy**2
    print(area)
else:
    area= tamañox * tamañoy
    print(area)

print(diametro)
print(multi)

if area > multi:
    print("aun puedes colocar mas circulos")

else:
    print("acabo")






