#efinir una función generar_n_caracteres() que tome un entero n y devuelva el caracter
#multiplicado por n. Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
def generar_n_caracteres(n,a):
    m= n * a
    print(m)
n=int(input("ingrese numero entero:"))
a=input("ingrese un carácter: ")
generar_n_caracteres(n,a)