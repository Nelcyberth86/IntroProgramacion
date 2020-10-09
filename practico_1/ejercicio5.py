p1 = str(input("ingrese, palabra: "))
p2 = str(input("ingrese,palabra: "))
n_1 = len(p1)
n_2 = len(p2)
r_s_letras = abs(n_2 - n_1) or abs(n_1-n_2)
if n_1 > n_2:
    print(f"la palabra {p1} tiene {r_s_letras} letras mas que {p2} ")
elif n_1 < n_2 :
    print(f"la palabra {p2} tiene {r_s_letras} letras mas que {p1}")
elif n_1 == n_2 :
    print("las palabras tienen el mismo largo")