from datetime import date

class Autor():

    def __init__(self, nombre:str, apellido:str, fecha_nacimiento:date) -> None:
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fecha_nacimiento = fecha_nacimiento

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre) -> None:
        self.__nombre = nuevo_nombre

    @property
    def fecha_nacimiento(self) -> date:
        return self.__fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, nuevo_fecha_nacimiento) -> None:
        self.__fecha_nacimiento = nuevo_fecha_nacimiento

    @property
    def apellido(self) -> str:
        return self.__apellido

    @apellido.setter
    def apellido(self, nuevo_apellido) -> None:
        self.__apellido = nuevo_apellido

    @property
    def nombre_completo(self) -> str:
        return f"{self.__apellido}, {self.__nombre}"


    def __str__(self) -> str:
        return f"{self.apellido}, {self.nombre}"
