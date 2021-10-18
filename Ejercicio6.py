# Escribir una clase en python llamada rectángulo que contenga una base y una altura, y que contenga un método que devuelva el área del rectángulo

class Rectangulo():

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(base, altura):
        area = base * altura
        return area

base = float(input("Ingrese base del rectangulo: "))
altura = float(input("Ingrese altura del rectangulo: "))
print("Area del rectangulo: %.2f" % Rectangulo.calcularArea(base, altura))
