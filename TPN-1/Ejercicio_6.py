def contar_vocales(frase):
    """
    Cuenta las vocales en una frase.

    Args:
    frase (str): Frase a analizar.

    Returns:
    int: Número de vocales en la frase.
    """
    vocales = 'aeiouáéíóú'
    frase = frase.lower()
    return sum(1 for letra in frase if letra in vocales)

def pedir_frase():
    """
    Solicita al usuario que ingrese una frase.

    Returns:
    str: Frase ingresada por el usuario.
    """
    frase = input('Ingresa una frase: ')
    return frase

# Pedir al usuario que ingrese una frase
frase = pedir_frase()

# Imprimir la cantidad de vocales en la frase
cantidad_vocales = contar_vocales(frase)
print(f'La frase tiene {cantidad_vocales} vocales.')