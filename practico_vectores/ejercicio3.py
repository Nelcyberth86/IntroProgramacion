#Crea un array de números de un tamaño pasado por teclado, el array contendrá números aleatorios entre 1 y 300 y
# mostrar aquellos números que acaben en un dígito que nosotros le indiquemos por teclado (debes controlar que se
# introduce un numero correcto), estos deben guardarse en un nuevo array
import random
def tamaño ( n,a ):
    array=[]
    d=1
    for i in range(0,n):
        num=random.randint(0,300)
        array.append(num)
    for p in array:
        o=p%10
        if o == a:
            print(f"se encontro el numero ",p, "con la terminacion" ,a)


num2=int(input("introduce el tamaño de tu vector: "))
num3=int(input("que numero desean encontrar: "))
numf= tamaño(num2,num3)


