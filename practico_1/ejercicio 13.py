#desarrolle un programa para estimar el valor de pi usando la siguiente suma infinita
import math
n =int(input("ingrese un numero entero: "))
pi = 0
for i in range(n):
    pi = pi+2 *(-1)**i*3**(1/2 - i)/(2*i + 1)
    print(pi)