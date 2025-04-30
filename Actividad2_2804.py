#Función para acortar texto con puntos suspensivos

def acortar_texto(texto, max_longitud):
    if len(texto) <= max_longitud:
      return texto
    else:
      return texto[:max_longitud - 3] + "..."