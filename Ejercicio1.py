# Escribir una clase en python que convierta un número entero a número romano (del 1 al 10)

class NumeroRomano():
    def __init__(self, numeroEntero):
        self.numeroEntero = numeroEntero

    def convertir(numeroEntero):
        if (numeroEntero == 1):
            return "I"
        elif (numeroEntero == 2):
            return "II"
        elif (numeroEntero == 3):
            return "III"
        elif (numeroEntero == 4):
            return "IV"
        elif (numeroEntero == 5):
            return "V"
        elif (numeroEntero == 6):
            return "VI"
        elif (numeroEntero == 7):
            return "VII"
        elif (numeroEntero == 8):
            return "VIII"
        elif (numeroEntero == 9):
            return "IX"
        elif (numeroEntero == 10):
            return "X"
  

n = int(input("Ingrese numero entero del 1 al 10: "))
print("Numero en romano: ", NumeroRomano.convertir(n))

