#E6: Escribir un programa que determine si un año es bisiesto (tiene
#366 días). Para ser bisiesto debe ser divisible entre 4 no se ser
#divisible entre 100, excepto que también sea divisible entre 400.
año = int(input("ingrese el año; "))
if (año%4==0 and año%100 != 0)or año%400==0:
    print("el año es bisiesto")
else:
    print("el año no es bisiesto")