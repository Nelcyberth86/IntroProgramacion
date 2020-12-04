def algoritmo(n,rangof):
    naturales = []
    par = []
    suma1 = 0
    impar = []
    suma2 = 0
    for a in range(num1, num2 - 1, - 1):
        naturales.append(a)
        if a % 2:
            impar.append(a)
            suma1 = suma1 + a
        else:
            par.append(a)
            suma2 = suma2 + a
    print(naturales)
    print(f"Lista impar:", impar)
    print(f"Suma:", suma1)
    print(f"Lista par: ", par)
    print(f"Suma: ", suma2)

num1=int(input("Introduzca un rango inicial: "))
num2=int(input("Introduzca un rango final: "))
algoritmo(num1,num2)

