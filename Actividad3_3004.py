#Tabla de multiplicar con while
while True:
    try:
        numeros=int(input("ingrese un numero a multiplicar: "))
        numero = 1
        while numero <= 10:
            print(f"{numeros} x {numero} = {numeros * numero}")
            numero += 1
    except ValueError:
        print("ingrese un numero valido: ")