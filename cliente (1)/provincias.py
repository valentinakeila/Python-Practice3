from datetime import date
from localidad import Localidad



class Provincia:
    def __init__(self, nombre):
        self.__nombre=nombre
        self.__localidades=[]
    
    def __str__(self) -> str:
        return self.__nombre
    
    def remove_localidad(self, localidad:Localidad):
        self.__localidades.remove(localidad)

    def add_localidad(self, localidad:Localidad):
        self.__localidades.append(localidad)


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

       