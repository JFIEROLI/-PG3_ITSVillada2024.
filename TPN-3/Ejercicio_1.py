def suma_enteros():
    while True:
        try:
            num1 = int(input("Ingrese el primer número entero: "))
            num2 = int(input("Ingrese el segundo número entero: "))
            
            suma = num1 + num2
            print("La suma de", num1, "y", num2, "es:", suma)
            
            seguir = input("¿Desea seguir sumando valores? (s/n): ")
            if seguir.lower() != 's':
                break
        except ValueError:
            print("Error: Por favor, ingrese solo números enteros.")

suma_enteros()