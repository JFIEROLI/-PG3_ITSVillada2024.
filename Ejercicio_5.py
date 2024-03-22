def es_capicua(palabra):
    """
    Determina si una palabra es un palíndromo o no.

    Args:
    palabra (str): Palabra a verificar.

    Returns:
    bool: True si la palabra es un palíndromo, False en caso contrario.
    """
    palabra_limpia = "".join(c.lower() for c in palabra if c.isalnum())
    return palabra_limpia == palabra_limpia[::-1]

def pedir_palabras():
    """
    Solicita al usuario que ingrese una lista de palabras.

    Returns:
    list: Lista de palabras ingresadas por el usuario.
    """
    palabras = []
    while True:
        palabra = input("Ingresa una palabra o presiona Enter para terminar: ")
        if palabra:
            palabras.append(palabra)
        else:
            break
    return palabras

# Pedir al usuario que ingrese una lista de palabras
palabras = pedir_palabras()

# Imprimir si cada palabra es un palíndromo o no
for palabra in palabras:
    if es_capicua(palabra):
        print(f"{palabra} es un palíndromo.")
    else:
        print(f"{palabra} no es un palíndromo.")