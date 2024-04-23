def division_numeros():
    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            
            resultado = num1 / num2
            print("La división de", num1, "entre", num2, "es:", resultado)
            break  # Salir del bucle si la división fue exitosa
        except ValueError:
            print("Error: Por favor, ingrese números válidos.")
        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero. Por favor, ingrese otro número.")

division_numeros()