def pedir_elementos():
    """
    Solicita al usuario que ingrese los elementos de la lista.

    Returns:
    list: Lista de enteros ingresados por el usuario.
    """
    elementos = []
    while True:
        elemento = input("Ingresa un número entero o presiona Enter para terminar: ")
        if elemento:
            elementos.append(int(elemento))
        else:
            break
    return elementos

def ordenar_lista(numeros):
    """
    Ordena una lista de enteros de mayor a menor.

    Args:
    numeros (list): Lista de enteros a ordenar.

    Returns:
    list: Lista ordenada de mayor a menor.
    """
    return sorted(numeros, reverse=True)

# Pedir al usuario que ingrese los elementos de la lista
elementos = pedir_elementos()

# Ordenar la lista de mayor a menor
elementos_ordenados = ordenar_lista(elementos)

# Imprimir la lista ordenada
print(elementos_ordenados)