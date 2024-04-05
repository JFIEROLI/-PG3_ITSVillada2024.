class Operaciones:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.realizar_operaciones()

    def realizar_operaciones(self):
        suma = self.sumar()
        resta = self.restar()
        multiplicacion = self.multiplicar()
        division = self.dividir()

        print("Suma:", suma)
        print("Resta:", resta)
        print("Multiplicación:", multiplicacion)
        print("División:", division)

    def sumar(self):
        return self.num1 + self.num2

    def restar(self):
        return self.num1 - self.num2

    def multiplicar(self):
        return self.num1 * self.num2

    def dividir(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "No se puede dividir entre cero"


def main():
    num1 = int(input("Ingrese el primer número entero: "))
    num2 = int(input("Ingrese el segundo número entero: "))

    operaciones = Operaciones(num1, num2)

if __name__ == "__main__":
    main()
