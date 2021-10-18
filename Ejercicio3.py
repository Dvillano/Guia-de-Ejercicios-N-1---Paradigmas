#Escribir una clase en python que obtenga todos los posibles subconjuntos únicos de un conjunto de números enteros distintos.
# Entrada: [4, 5, 6]
# Salida: [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]

class Conjunto:
    
    def __init__(self, conjunto):
            self.conjunto = conjunto

    def subconjunto(numeros):
        if numeros == []:
            return [[]]
        else:
            x = Conjunto.subconjunto(numeros[1:])
            return x + [[numeros[0]] + y for y in x]
 
print(Conjunto.subconjunto([4,5,6]))


