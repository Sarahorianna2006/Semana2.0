#Sumar solo numeros impares
numeros = [1,100]
for numero in numeros:
    if numero % 2 != 0:
        continue
    print(f"numero: {numero}")





    
"""try:
    numero = int(input("ingrese un numero: "))
    suma_impares = 0
    for i in range(1, numero + 1):
        if i % 2 != 0:
            suma_impares += i
            print("la suma de los numeros impares entre 1 y {numero} es: {suma_impares}")
except ValueError:
 print("ingrese un numero valido")"""