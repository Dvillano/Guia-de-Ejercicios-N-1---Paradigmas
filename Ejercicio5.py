# Escribir una clase en python que revierta una cadena de palabras
# Entrada: "Mi Diario Python"
# Salida: "Python Diario Mi"

class Palabra():

    def __init__(self, palabra):
        self.palabra = palabra

    def invertir(palabra):
        palabra = palabra.split(' ')
        palabraInversa = ' '.join(reversed(palabra))
        return palabraInversa


print(Palabra.invertir("Mi Diario de Python"))