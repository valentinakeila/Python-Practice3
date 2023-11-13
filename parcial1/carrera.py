from datetime import date
from titulo import Titulo

class Carrera():

    def __init__(self, nombre: str, fecha_comienzo: date) -> None:
        self.__nombre = nombre
        self.__fecha_comienzo = fecha_comienzo
        self.__titulos_grado_requerido = []

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        self.__nombre = valor


    @property
    def fecha_comienzo(self):
        return f"{self.__fecha_comienzo.month}/{self.__fecha_comienzo.year}"
    
    @fecha_comienzo.setter
    def fecha_comienzo(self, valor: date) -> None:
        self.__fecha_comienzo = valor

    @property
    def titulos_grado_requerido(self) -> list:
        return self.__titulos_grado_requerido

    @property
    def cantidad_titulos_requeridos(self) -> str:
        return len(self.titulos_grado_requerido)
    
    def __str__(self) -> str:
        return f"{self.nombre} Comienzo: {self.fecha_comienzo} TR: [ {self.cantidad_titulos_requeridos} ]"
    
    def add_titulo_requerido(self, titulo: Titulo) -> None:
        self.__titulos_grado_requerido.append(titulo)

    def remove_titulo_requerido(self, titulo: Titulo) -> None:
        self.__titulos_grado_requerido.remove(titulo)