from datetime import datetime
from precio import *
class Estadia:
    def __init__(self, patente: str):
        self.__fecha = datetime.today()
        self.__nro_patente = patente
        self.__hro_entrada = datetime.now().hour
        self.__hro_salida = 0
        self.__cantHoras = None
        self.__estado = "ACTIVO"
        self.__pagado = False
    
    def __str__(self):
        return f"Patente: {self.__nro_patente} Fecha: {self.__fecha} Hora de Entrada: {self.__hro_entrada} / Hora de Salida: {self.__hro_salida} Cantidad de Horas: {self.__cantHoras} Estado: {self.__estado} Pagado: {self.__pagado}"
    
    def registrar_salida(self):
        self.__hro_salida = datetime.now().hour
        self.__cantHoras = self.__hro_salida - self.__hro_entrada


    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, valor):
        self.__fecha = valor

    @property
    def nro_patente(self):
        return self.__nro_patente

    @nro_patente.setter
    def nro_patente(self, valor):
        self.__nro_patente = valor

    @property
    def hro_entrada(self):
        return self.__hro_entrada

    @hro_entrada.setter
    def hro_entrada(self, valor):
        self.__hro_entrada = valor

    @property
    def hro_salida(self):
        return self.__hro_salida

    @hro_salida.setter
    def hro_salida(self, valor):
        self.__hro_salida = valor

    @property
    def cantHoras(self):
        return self.__cantHoras

    @cantHoras.setter
    def cantHoras(self, valor):
        self.__cantHoras = valor

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, valor):
        self.__estado = valor

    @property
    def pagado(self):
        return self.__pagado

    @pagado.setter
    def pagado(self, valor):
        self.__pagado = valor
    

estadias = []
bandera_patente_repetida = False

precio = Precio(input("Ingrese el precio de la hora"))

opcion = 0
while opcion != 3:
    print("Menú:")
    print("1. Ingresar Estadia")
    print("2. Finalizar Estadia")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        patente = input("Ingrese el numero de patente")
        for i in estadias:
            if patente == i.patente:
                bandera_patente_repetida = True
                break
        if bandera_patente_repetida == False:
            estadia = Estadia(patente)
            estadias.append(estadia)
        else:
            print("La patente ya esta registrada")
    elif opcion == "2":
        bandera_patente_encontrada = False
        indice_estadia = 0
        patente = input("Ingrese el numero de patente")
        for i in estadias:
            indice_estadia = indice_estadia + 1
            if patente == i.nro_patente:
                bandera_patente_encontrada = True
                break
        if bandera_patente_encontrada == True:
            indice_estadia = indice_estadia - 1
            estadias[indice_estadia].registrar_salida
            print("El precio a pagar es" + precio.calcular_importe(estadias[indice_estadia].cantHoras))

    elif opcion == "3":
        print("Saliendo del programa.")
        break
    else:
        print("Opcion no valida")

    