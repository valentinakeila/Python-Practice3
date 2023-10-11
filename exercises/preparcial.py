""""
Se desea crear un programa que simule el funcionamiento basico de un vehiculo.


-Crear una clase "Vehiculo" con los atributos : marca(Str),ruedas ( Int ),color(Str),enMarcha(Booleano, por defecto False)
-Crear su constructor
-Crear el metodo de instancia arrancar() que permita poner en marcha el vehiculo
-crear el metodo de instancia tipoVehiculo() que devuelva "Automovil" si el vehiculo tiene 4 ruedas y "Motocicleta" si posee 2 ruedas.
-Crear el metodo de instancia mostrar() que muestre por pantalla todos los 4 atributos del vehiculo.


Colocar abajo la comisión y nro de grupo, ademas de los integrantes del grupo ( Nombre y apellido , legajo ).A la hora de hacer el PR colocar nro de grupo y comisión en el titulo del mismo.
Comisión : X
Grupo : X
Integrantes:
-Legajo XXXX,....
-Legajo YYYY,.... 
"""

class Vehiculo:
    
    def __init__(self, marcaValor: str, ruedasValor: int, colorValor: str):
        self.enMarcha = False
        self.marca = marcaValor
        self.ruedas = ruedasValor
        self.color = colorValor
    
    def arrancar(self):
        self.enMarcha = True
        
    
    def tipoVehiculo(self):
        if (self.ruedas == 2):
            print("Motocicleta")
        elif(self.ruedas == 4):
            print("Automovil")
        else:
            print("Error 404 NaN")
            
    def mostrar(self):
        print(f"El número de ruedas del vehículo es: {self.ruedas}")
        if (self.enMarcha == True):
            print("Vehiculo en marcha")
        else:
            print("Vehiculo parado")


miAuto = Vehiculo("Tesla by Elon Musk", 4, "rojo cromado con neon")

miAuto.arrancar()
miAuto.tipoVehiculo()
miAuto.mostrar()
