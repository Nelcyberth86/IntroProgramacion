#Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena
#"estoy probando" debería devolver la cadena "odnaborp yotse"
def cadena(oracion):
    long=-1
    for i in (oracion):
        long=long + 1

    for i in range(long,-1,-1):
        print(oracion[i],end="")

pl=(input("ingrese la frase: "))
cadena(pl)
