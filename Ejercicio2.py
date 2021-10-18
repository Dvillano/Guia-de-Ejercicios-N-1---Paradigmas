#Escribir una clase en python que convierta un número romano en un número entero (del 1 al 10)

class NumeroEntero():
    def __init__(self, numeroRomano):
        self.numeroRomano = numeroRomano

    def convertir(numeroRomano):
        if (numeroRomano == "I"):
            return 1
        elif (numeroRomano == "II"):
            return 2
        elif (numeroRomano == "III"):
            return 3 
        elif (numeroRomano == "IV"):
            return 4
        elif (numeroRomano == "V"):
            return 5
        elif (numeroRomano == "VI"):
            return 6
        elif (numeroRomano == "VII"):
            return 7
        elif (numeroRomano == "VIII"):
            return 8
        elif (numeroRomano == "IX"):
            return 9
        elif (numeroRomano == "X"):
            return 10 


            

n = input("Ingrese numero romano del 1 al 10: ")
print("Numero entero: ", NumeroEntero.convertir(n.upper()))

