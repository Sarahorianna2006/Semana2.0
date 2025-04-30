#Clasificar edades
edad = int(input("Ingresa la edad que tienes: "))

if edad >= 1 and edad < 12:
    print("Eres un niño")
elif edad >= 12 and edad <= 17:
    print("Eres un adolescente")
elif edad >= 18 and edad <= 59:
    print("Eres un adulto")
elif edad >= 60:
    print("Eres un adulto mayor")

else:
    print("Edad no valida")
    