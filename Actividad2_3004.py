#Menú interactivo simple
while True:
    print("/nMenú:")
    print("1. saludar")
    print("2. decir tu edad")
    print("3. salir")
    opcion = input("ingrese una opción")

    if opcion == "1":
     print("Hola")
    elif opcion == "2":
     try:
        edad = int(input("ingrese su edad"))
        print(f"tu edad es {edad} años.")
     except ValueError:
       print("ingrese una edad valida")
    elif opcion == "3":
     print("adios")
    break
else:
      print("opcion invalida, intente nuevamente")
