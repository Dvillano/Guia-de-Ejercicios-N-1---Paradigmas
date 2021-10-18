class Humano():

    def __init__(self, edad, nombre, ocupacion):
        self.edad = edad
        self.nombre = nombre
        self.ocupacion = ocupacion

        # Creacion de un nuevo metodo
    def presentar(self):
        presentacion = ("Hola soy {}, mi edad es {} y mi ocupacion es {}") #Mensaje
        print(presentacion.format(self.nombre, self.edad, self.ocupacion)) #Usamos FORMAT

Persona1 = Humano(31, "Pedro", "Desocupado") #Instancia
Persona2 = Humano(28, "Pablo", "Profesor")

# Llamamos al metodo
Persona1.presentar();
Persona2.presentar();

# Ingresando por teclado
nombre = input("Nombre: ")
edad = input("Edad: ")
ocupacion = input("Ocupacion: ")

Persona3 = Humano(edad, nombre, ocupacion)

Persona3.presentar()