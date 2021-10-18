#Crear clase calculador que sirva para hacer sumas y restas
# Les pasamos dos valores y los suma

class Calculadora():

    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def sumar(numero1, numero2):
        resultado = numero1 + numero2
        print(resultado)

    def restar(numero1, numero2):
        resultado = numero1 - numero2
        print(resultado)


n1 = int(input("Ingrese primer numero: "))
n2 = int(input("Ingrese segundo numero: "))
operacion = input("Ingrese operacion a realizar: ")

if (operacion == "suma"):
    Calculadora.sumar(n1, n2)
elif (operacion == "resta"):
    Calculadora.restar(n1, n2)



