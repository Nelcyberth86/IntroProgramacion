p1 = str(input("ingrese, palabra: "))
p2 = str(input("ingrese,palabra: "))
n_1 = len(p1)
n_2 = len(p2)
contador = abs(n_2 - n_1)
if n_1 > n_2:
    print(f"la palabra {p1} tiene {contador} letras mas que {p2} ")
elif n_1 < n_2 :
    print(f"la palabra {p2} tiene {contador} letras mas que {p1}")