#Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que
#python tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un
#muy buen ejercicio
def cadena(oracion):
    long=0
    for i in (oracion):
        long=long + 1
    print("la lista ingresada tiene",long,"de longitud")
    return long
pl=(input("ingrese la frase : "))
cadena(pl)