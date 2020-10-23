#Definir una función que tome como argumento dos números y devuelva el mayor de ellos.
#(Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es
#un muy buen ejercicio.
def Nma_Nme(num1,num2):

    if num2>num1:
        print("es el numero mayor", num2)
    elif num1>num2:
        print("es el numero mayor", num1)

num1=int(input("ingrese numero: "))
num2=int(input("ingrese numero: "))

Nma_Nme(num1,num2)