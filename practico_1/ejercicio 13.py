#desarrolle un programa para estimar el valor de pi usando la siguiente suma infinita
n =int(input("ingrese un numero entero: "))
suma = 0
for num in range(1,n + 1):
    if num % 2 == 0:
        signo = -1
    else:
        signo = 1
    valor_actual = signo /(1 + 2*(valor_actual))
    suma = suma + valor_actual
pi= 4 * suma
print(pi)