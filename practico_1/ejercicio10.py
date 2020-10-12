#Desassollo un programa que permita  ingresar los tiempos de viaje de los tramos y entregue como resultado el tiempo total del viaje
tramo_1 = int(input("ingrese duracion de primer, tramo: "))
tramo_2 = int(input("ingrese duracion de segundo tramo: "))
tramo_3 = int(input("ingrese duracion de tercero tramo: "))
tramo_4 = int(input("ingrese duracion de cuarto tramo: "))
duracion_tramo = tramo_1 +tramo_2 +tramo_3 +tramo_4
minutos = duracion_tramo
horas = minutos// 60
minutos_resto = minutos % 60
print(f"la duracion fue de {horas}hrs:{minutos_resto}min")




