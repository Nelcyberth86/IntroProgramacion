def tablaM(numI):
    for i in range(1, 11):
        print(numI, "x", i, "=", numI * i)
        i= i+1

print("tabla del 1 al 10")
numa=1
for i in range(0, 10):
   # print("tabla de multiplicar de",i)
    #tablaM(i)
   if numa > 0:
       numa = i + 1
   print("tabla de multiplicar de", numa)
   tablaM(numa)