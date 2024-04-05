class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_nombre(self):
        print("Nombre:", self.nombre)

# Definir dos objetos de la clase Persona
persona1 = Persona("FIEROLI")
persona2 = Persona("VILLADA")

# Mostrar el contenido del nombre de cada persona
persona1.mostrar_nombre()
persona2.mostrar_nombre()
