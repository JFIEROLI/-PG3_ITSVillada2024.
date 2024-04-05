class Persona:
    def __init__(self):
        self.nombre = ""
        self.edad = 0

    def cargar_datos(self):
        self.nombre = input("Ingrese el nombre: ")
        self.edad = int(input("Ingrese la edad: "))

    def imprimir_datos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)


class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.sueldo = 0

    def cargar_datos(self):
        super().cargar_datos()
        self.sueldo = float(input("Ingrese el sueldo: "))

    def imprimir_datos(self):
        super().imprimir_datos()
        print("Sueldo:", self.sueldo)

    def pagar_impuestos(self):
        if self.sueldo > 3000:
            print("Debe pagar impuestos.")
        else:
            print("No debe pagar impuestos.")


# Bloque principal del programa
def main():
    # Crear objeto de la clase Persona
    persona = Persona()
    print("Ingrese los datos de la persona:")
    persona.cargar_datos()
    print("\nDatos de la persona:")
    persona.imprimir_datos()

    # Crear objeto de la clase Empleado
    empleado = Empleado()
    print("\nIngrese los datos del empleado:")
    empleado.cargar_datos()
    print("\nDatos del empleado:")
    empleado.imprimir_datos()
    empleado.pagar_impuestos()


if __name__ == "__main__":
    main()
