from datetime import date


class Localidad:
    def __init__(self, nombre,codigo_postal):
        self.__nombre=nombre
        self.__codigo_postal=codigo_postal
    
    def __str__(self) -> str:
        return self.__nombre
    
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
    
    @property
    def codigo_postal(self):
        return self.__codigo_postal
    
    @codigo_postal.setter
    def codigo_postal(self,newCodigo):
        self.__codigo_postal=newCodigo
