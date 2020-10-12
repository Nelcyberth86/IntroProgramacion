#escriba un programa que reciba como entrada la estatura,peso y la edad de una persona y le entregue su condicion de riesgo
estatura = float(input("ingrese su estatura en m:"))
peso = int(input("ingrese su peso en kg: "))
edad = int(input("ingrese su edad: "))
imc= peso / estatura
if edad < 45  and imc < 22.0 :
    print("usted tiene bajas condiciones de riesgo a enfermedades coronarias ")
elif edad >= 45 and imc < 22.0 :
    print("usted puede llegar a tener  condiciones de riesgo altas a enfermedades coronarias, debe de cuidarse ")
elif edad < 45 and imc >= 22.0 :
    print("usted puede llegar a tener  condiciones de riesgo altas a enfermedades coronarias, debe de cuidarse ")
elif edad >= 45 and imc >= 22.0 :
    print("usted tiene condiciones de riesgo altas a enfermedades coronarias, valla a un doctor")