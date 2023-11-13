from datetime import date
from pais import *


class Cliente:
    def __init__(self, nombre_apellido:str, nro_cliente:int, direccion:str,pais:Pais, fecha_alta:date=date.today()) -> None:
        self.__nombre_apellido=nombre_apellido
        self.__nro_cliente=nro_cliente
        self.__direccion=direccion
        self.__fecha_baja=None
        self.__fecha_alta=fecha_alta
        self.__pais=pais

    def __str__(self) -> str:
       return f""" 
        Nombre y Apellido: {self.__nombre_apellido}
        Nro Cliente: {self.__nro_cliente}
        Direccion: {self.__direccion} - {self.__pais}
        
        """
    
    def eliminar_cliente(self):
        self.__fecha_baja=date.today()


    def reactivar_cliente(self):
        self.__fecha_baja=None

    def __get_nro_cliente(self):
        pass

    


    @property
    def nro_cliente(self):
        return self.__nro_cliente
    @property
    def direccion(self):
        return self.__direccion
    @direccion.setter
    def direccion(self, nuevaDireccion):
        self.__direccion=nuevaDireccion

    


