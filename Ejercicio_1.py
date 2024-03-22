def encontrar_indice(lst, elemento):
    
    try:
        return lst.index(elemento)
    except ValueError:
        return -1

# Lista pre-construida
mi_lista = [8, 12, 9, 45]

while True:
    # Entrada del usuario
    entrada_usuario = input("Ingresa un número para buscar (o 'q' para salir): ")

    # Salir si el usuario ingresa 'q'
    if entrada_usuario.lower() == 'q':
        break

    # Convertir la entrada a un número entero
    try:
        numero = int(entrada_usuario)
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número válido.")
        continue

    # Encontrar el índice
    indice = encontrar_indice(mi_lista, numero)

    # Imprimir el resultado
    if indice == -1:
        print(f"El número {numero} no se encontró en la lista.")
    else:
        print(f"El número {numero} se encontró en el índice {indice}.")
