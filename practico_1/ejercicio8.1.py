numero_1 = int(input("Escriba un número entero positivo: "))
numero_2 = int(input("Escriba un número entero positivo: "))
suma = 0
for i in range(numero_1+1, numero_2):
        suma = suma + i
print(f"La suma desde {numero_1} hasta {numero_2} es {suma}")
