from datetime import date
from provincias import Provincia

class Pais:
    def __init__(self,nombre):
        self.__nombre=nombre
        self.__provincias=[]

    def __str__(self) -> str:
        return self.__nombre
    


    def add_provincia(self,provincia:Provincia):
        self.__provincias.append(provincia)


    def remove_provincia(self,provincia:Provincia):
        self.__provincias.remove(provincia)

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nuevoNombre):
        self.__nombre=nuevoNombre

    @property
    def fecha_alta(self):
        return self.__fecha_alta
    
    @property
    def codigo(self):
        return self.__codigo