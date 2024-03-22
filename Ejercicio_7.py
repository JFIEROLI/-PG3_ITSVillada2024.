def es_numero_step(numero):
    numero_str = str(numero)  # Convertir el número a cadena de caracteres
    for i in range(len(numero_str) - 1):
        if abs(int(numero_str[i]) - int(numero_str[i + 1])) != 1:
            return False
    return True

while True:
    numero_usuario = input("Ingrese un número para verificar si es un número step (o 'salir' para terminar): ")

    if numero_usuario.lower() == 'salir':
        print("¡Hasta luego!")
        break

    if numero_usuario.isdigit():
        numero_usuario = int(numero_usuario)
        if es_numero_step(numero_usuario):
            print("El número", numero_usuario, "es un número step.")
        else:
            print("El número", numero_usuario, "no es un número step.")
    else:
        print("Por favor, ingrese un número válido.")
