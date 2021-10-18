# Escribir una clase en python llamada circulo que contenga un radio, con un
# método que devuelva el área y otro que devuelva el perímetro del circulo.
import math

class Circulo():

    def __init__(self, radio):
        self.radio = radio

    def calcularArea(radio):
        area = math.pi * pow(radio, 2)
        return area
    
    def calcularPerimetro(radio):
        perimetro = 2 * math.pi * radio
        return perimetro

radio = float(input("Ingrese radio del circulo: "))
print("Area: %.2f" % Circulo.calcularArea(radio) )
print("Perimetro: %.2f" % Circulo.calcularPerimetro(radio) )
