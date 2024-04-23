def mostrar_nombre_mes():
    meses = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')
    while True:
        try:
            numero_mes = int(input("Ingrese el número de mes (1-12): "))
            if 1 <= numero_mes <= 12:
                nombre_mes = meses[numero_mes - 1]
                print("El mes correspondiente al número", numero_mes, "es:", nombre_mes.capitalize())
                break  # Salir del bucle si la operación fue exitosa
            else:
                print("Error: El número de mes debe estar entre 1 y 12.")
        except IndexError:
            print("Error: El número de mes está fuera de rango. Por favor, ingrese un número entre 1 y 12.")
        except ValueError:
            print("Error: Por favor, ingrese un número válido.")

mostrar_nombre_mes()