def es_bisiesto(año):
    """
    Determina si un año dado es bisiesto o no.

    Args:
    año (int): El año a verificar.

    Returns:
    bool: True si el año es bisiesto, False en caso contrario.
    """
    if año % 4 != 0:
        return False
    elif año % 100 != 0:
        return True
    elif año % 400 != 0:
        return False
    else:
        return True

# Obtener la entrada del usuario para el primer año a verificar
primer_año = int(input("Ingresa el primer año: "))

# Verificar si el primer año es bisiesto o no
if es_bisiesto(primer_año):
    print(f"{primer_año} es un año bisiesto.")
else:
    print(f"{primer_año} no es un año bisiesto.")

# Obtener la entrada del usuario para el segundo año a verificar
segundo_año = int(input("Ingresa el segundo año: "))

# Verificar si el segundo año es bisiesto o no
if es_bisiesto(segundo_año):
    print(f"{segundo_año} es un año bisiesto.")
else:
    print(f"{segundo_año} no es un año bisiesto.")
