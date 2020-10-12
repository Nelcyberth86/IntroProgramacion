#desarolle un programa que muestre la palabra mas corta hasta la mas larga
from operator import itemgetter
n_plbs = int(input("indique cuantas palabras ingresara: "))
for i in range(1,n_plbs+1):
    palabras = len(str(input(f"ingrese palabras:  ")))
    print(palabras)
print(f"la palabra mas larga es la que muestra el numero mayor y la mas corta la que muestra el numero menor ")





