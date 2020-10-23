#- Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
def n_mayor(num1,num2,nume3):
    if num1>=num2:
        if num1>=nume3:
            print(num1, "es el mayor ")
    elif num2>=num1:
        if num2>=nume3:
            print(num2, "es el mayor ")
    elif nume3 >=num1:
        if nume3 >=num2:
            print(nume3, "es el mayor ")
    elif num2==num1==nume3:
        print("son iguales")

num1=int(input("ingrese numero: "))
num2=int(input("ingrese numero: "))
num3=int(input("ingrese numero: "))

n_mayor(num1,num2,num3)