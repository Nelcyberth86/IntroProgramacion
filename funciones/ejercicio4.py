
def letra(vocal):
    if vocal == "a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal == "u":
        print(vocal,"es una vocal")
    elif vocal!="a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal == "u":
        print("letra minuscula!")
    else:
        print(vocal,"no es una vocal")

letra1= str(input("ingrese letra en minuscula porfavor: "))
letra(letra1)