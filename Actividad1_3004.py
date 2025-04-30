#Adivina el número
#importamos libreria
import random


numero_secreto = random.randint(1,100)
"""print(numero_secreto)"""


intentos = 0

while True:
    try:
        numero_usuario = int(input("adivina el numero secreto: "))
        intentos += 1 
        if numero_usuario == numero_secreto:
         print(f"adivinaste el numero secreto en {intentos} intentos")
         break
        elif numero_usuario < numero_secreto:
         print("el numero secreto es mayor. Intenta nuevamente")
        else:
         print("el numero secreto es menor. Intenta nuevamente")
    except ValueError:
      print("ingrese un numero valido")