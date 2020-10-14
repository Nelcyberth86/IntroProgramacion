#escriba un programa que reciba como entrada dos numeros y los muestre ordenados de menor a mayor
num1 = int(input("ingrese, numero : "))
num2 = int(input("ingrese, numero : "))
x = min(num1, num2)
y = max(num2, num1)
print(f"los numero ordenados son: {x},{y}")


n1 = int(input("ingrese,numero: "))
n2 = int(input("ingrese, numero "))
n3 = int(input("ingrese,numero "))
if n1<n2 or n1<n3:
    inicio = n1
    if n2> n3 :
        mayor = n2
        medio = n3
    else:
        mayor = n3
        medio = n2
elif n2<n1 or n2<n3:
    inicio = n2
    if n1 < n3 :
        mayor = n3
        medio = n1
    else:
        medio = n3
        mayor = n2
elif n3 < n2 or n3 < n1:
    inicio = n3
    if n2<n1 :
        mayor = n1
        medio = n2
    else:
        medio = n1
        mayor = n2
print(f"{inicio} , {medio} , {mayor}")

