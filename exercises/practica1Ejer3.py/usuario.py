from datetime import date
from persona import *
from libro import *

class Usuario(Persona):
    def __init__(self, nombre: str, apellido: str, fecha_nacimiento: date, edad: int, nro_documento: int, user_name: str, contraseña: str) -> None:
        super().__init__(nombre, apellido, fecha_nacimiento, edad, nro_documento)
        self.__user_name = user_name
        self.__estado = True
        self.__administrador = False
        self.__contraseña = contraseña
        self.__fecha_alta = date.today()
        self.__fecha_baja = None
        self.__mis_libros = []


    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, valor):
        self.__estado = valor

    @property
    def administrador(self):
        return self.__administrador

    @administrador.setter
    def administrador(self, valor):
        self.__administrador = valor

    @property
    def contraseña(self):
        return self.__contraseña

    @contraseña.setter
    def contraseña(self, valor):
        self.__contraseña = valor

    @property
    def fecha_baja(self):
        return self.__fecha_baja

    @fecha_baja.setter
    def fecha_baja(self, valor):
        self.__fecha_baja = valor


    @property
    def mis_libros(self):
        return self.__mis_libros

    @mis_libros.setter
    def mis_libros(self, valor):
        self.__mis_libros = valor

    def leyo_libro(self, nombreDelLibro: str):
        for i in range(0,len(self.__mis_libros)):
            if nombreDelLibro == self.__mis_libros[i].nombre:
                return True


    
    def agregar_libro(self, libro: Libro) -> None:
        self.__mis_libros.append(libro)

    def quitar_libro(self, libro: Libro) -> None:
        self.__mis_libros.remove(libro)

    def baja_usuario(self):
        self.__estado = False
        self.__fecha_baja = date.today()

    
    def validar_credenciales(self, usuario: str, contrasenia: str):
        if self._usuario == usuario and self._contrasenia == contrasenia:
            return True, "Credenciales correctas"
        return False, "Credenciales incorrectas"



