from titulo import *
class Aspirante():
    def __init__(self, nombre: str, apellido: str, email: str, num_telefono: str) -> None:
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__num_telefono = num_telefono
        self.__titulos = []


    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, valor):
        self.__apellido = valor

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valor):
        self.__email = valor

    @property
    def num_telefono(self):
        return self.__num_telefono

    @num_telefono.setter
    def num_telefono(self, valor):
        self.__num_telefono = valor

    @property
    def titulos(self) -> list:
        return self.__titulos

    def add_titulo(self, titulo: Titulo) -> None:
        self.__titulos.append(titulo)

    def remove_titulo(self, titulo: Titulo) -> None:
        self.__titulos.remove(titulo)

    
    def __str__(self) -> str:
        return f"Nombre: {self.nombre} Apellido: {self.apellido} Email: {self.email} Telefono: {self.num_telefono }"