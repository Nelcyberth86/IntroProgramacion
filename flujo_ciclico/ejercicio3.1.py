#E3: Escribir un programa que muestre todos los múltiplos de 3 o 5 que se encuentran entre 15 y 80
for num in range(15,81) :
    if num%5 ==0 or num%3 == 0 :
        print(num)