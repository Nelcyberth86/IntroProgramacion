#tabl de multiplicar
def tablaM(numI):
    for i in range(1,11):
        print(numI,"x" , i , "=", numI*i)

num = int(input(input("ingrese: ")))
tablaM(num)
