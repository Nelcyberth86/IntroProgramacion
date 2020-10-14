#E4: Debido a la actual escasez de agua, la empresa COSAALT ha decidido penalizar el consumo excesivo de agua incrementando el
#precio según la cantidad consumida.
monto_de_pago = int(input("ingrese, consumo de agua m3: "))
if monto_de_pago < int(100) :
    monto= int(monto_de_pago * 1)
    print(f"usted tiene que pagar {monto}")
elif monto_de_pago > 100 and monto_de_pago > 499:
    monto2= float(monto_de_pago * 1.20)
elif monto_de_pago > 500 and monto_de_pago > 999:
    monto3= float(monto_de_pago * 1.50)
    print(f"usted tiene que cancelar {monto3}")
elif monto_de_pago > 1000:
    monto4= int(monto_de_pago * 2)
    print(f"usted tiene que cancelar {monto4}")
