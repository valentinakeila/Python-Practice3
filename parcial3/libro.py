from datetime import date
from genero import Genero
from autor import Autor

class Libro():

    def __init__(self, nombre:str, autor: Autor = None) -> None:
        self.__nombre = nombre
        self.__fecha_publicacion = date.today()
        self.__generos_libro = []
        self.__autor = autor

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre) -> None:
        self.__nombre = nuevo_nombre

    @property
    def autor(self) -> Autor:
        return self.__autor

    @property
    def fecha_publicacion(self) -> str:
        return f"{self.__fecha_publicacion.day}/{self.__fecha_publicacion.month}/{self.__fecha_publicacion.year}"

    @property
    def generos_libro(self) -> list:
        return self.__generos_libro

    def add_genero(self, genero: Genero) -> None:
        self.__generos_libro.append(genero)

    def remove_genero(self, genero: Genero) -> None:
        self.__generos_libro.remove(genero)

    def __str__(self) -> str: 
        return f"{self.nombre} [ Autor: {self.autor.nombre_completo if self.autor else 'unknow'} - Publicado: {self.fecha_publicacion} ]"
