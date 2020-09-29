horas_trabajadas = int(input( "ingrese_cantidad_de_horas_trabajadas: ") )
monto_a_pagar_por_horas_trabajadas = int(input("ingrese_monto_a_pagar_por_horas_trabajadas: "))
pago_del_empleado = horas_trabajadas * monto_a_pagar_por_horas_trabajadas
total = "monto_a_pagar: " + str(pago_del_empleado)
print(total)