#desarolle un programa que muestre la palabra mas corta hasta la mas larga
from operator import itemgetter
n_plbs = int(input("indique cuantas palabras ingresara: "))
palabra_mas_larga = ""
palabra_mas_corta = ""
for i in range(1,n_plbs+1):
    palabra_actual = input(f"ingrese palabras:  ")
    if len(palabra_actual) >= len(palabra_mas_larga) :
        palabra_mas_larga= palabra_actual
    if len(palabra_mas_corta) <=len(palabra_mas_larga):
        palabra_mas_corta = palabra_actual
print(f"palabra mas larga es {palabra_mas_larga} y la palabra mas corta es {palabra_mas_corta}")






