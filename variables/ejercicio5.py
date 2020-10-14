#E5: Escribir un programa que pregunte al usuario por el número dehoras trabajadas y la paga por hora. Después mostrar en la pantalla elmonto a pagar al trabajador
horas_trabajadas = int(input( "ingrese_cantidad_de_horas_trabajadas: ") )
monto_a_pagar_por_horas_trabajadas = int(input("ingrese_monto_a_pagar_por_horas_trabajadas: "))
pago_del_empleado = horas_trabajadas * monto_a_pagar_por_horas_trabajadas
total = "monto_a_pagar: " + str(pago_del_empleado)
print(total)