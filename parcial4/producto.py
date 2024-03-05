from random import randint


class Producto:
    def __init__(self, nombre: str, precio: float):
        self.__nombre = nombre
        self.__precio = precio
        self.__codigo = randint(1000000000, 9999999999)

    def __str__(self):
        return f"\n{self.__codigo} : {self.__nombre} - ${self.__precio}"

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio):
        self.__precio = nuevo_precio

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, nuevo_codigo):
        self.__codigo = nuevo_codigo

""" producto = Producto("Polystation 2002", 200)
print(producto)
 """