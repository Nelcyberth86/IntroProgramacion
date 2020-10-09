dividendo= int(input("ingrese numero: "))
divisor = int(input("ingrese numero: "))
cociente = dividendo // divisor
resto = dividendo % divisor
if resto == 0 :
    print(f"la divisones exacta ")
    print(f"cociente: {cociente}")
    print(f"resto:{resto}")
else:
    print(f"la divison no es exacta")
    print(f"cociente : {cociente}")
    print(f"resto:{resto}")