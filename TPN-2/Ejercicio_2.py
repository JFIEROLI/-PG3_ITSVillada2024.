class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir_datos(self):
        print("Nombre:", self.nombre)
        print("Nota:", self.nota)

    def verificar_regularidad(self, nota_minima=6):
        if self.nota >= nota_minima:
            print(f"{self.nombre} está regular.")
        else:
            print(f"{self.nombre} no está regular.")

# Definir dos objetos de la clase Alumno
alumno1 = Alumno("JOAQUIN", 7)
alumno2 = Alumno("BENICIO", 5)

# Imprimir los datos de cada alumno y verificar su regularidad
alumno1.imprimir_datos()
alumno1.verificar_regularidad()
print()
alumno2.imprimir_datos()
alumno2.verificar_regularidad()
