#E3: Escribir un programa que permita al usuario votar por dos posibles partidos políticos, A o B. Leer el partido por el que vota el
#usuario por teclado y mostrar el mensaje „Usted ha votado por <partido>“. En caso de que el usuario ingrese una valor incorrecto,
#mostrar el mensaje „Voto inválido“.

voto = input("ingrese su voto: ")
if voto == "mesa" :
    print(f"votaste por:  {voto}")
elif voto == "papi camacho":
    print(f"votaste por : {voto}")
else:
    print("voto nulo")
