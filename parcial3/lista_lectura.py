from datetime import date
from libro import Libro

class ListaLectura():

    __codigos = set()

    def __init__(self, nombre:str, codigo: int) -> None:
        self.__nombre = nombre
        self.__codigo = self.__validar_codigo(codigo)
        self.__libros = []

    @property
    def codigo(self) -> int:
        return self.__codigo

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre) -> None:
        self.__nombre = nuevo_nombre

    @property
    def libros(self) -> list:
        return self.__libros

    @property
    def cantidad_libros(self) -> int:
        return len(self.__libros)

    def add_libro(self, libro: Libro) -> None:
        self.__libros.append(libro)

    def remove_libro(self, libro: Libro) -> None:
        self.__libros.remove(libro)

    def __str__(self) -> str: 
        return f"{self.codigo} | {self.nombre} [ {self.cantidad_libros} ]"

    @classmethod
    def __validar_codigo(cls, codigo) -> int:
        if codigo in cls.__codigos:
            raise Exception("El codigo está repetido")
        cls.__codigos.add(codigo)
        return codigo
