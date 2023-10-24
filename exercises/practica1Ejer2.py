""""Adaptar el código anterior para respetar el siguiente diagrama en UML. Aplican los
requerimientos del ejercicio 1.
"""
import abc
from abc import ABC, abstractmethod

from datetime import *

class Persona(ABC): #en las clases abstractas se pasa abc y se importa el modulo abc significa abstract class

    def __init__(self,nombreValor: str,apellidoValor: str,edadValor: int,anio_nacimiento: int,mes_nacimiento: int, dia_nacimiento: int):
       self._nombre = nombreValor
       self._apellido = apellidoValor
       self._edad = edadValor
       self._fecha_nacimiento = datetime(anio_nacimiento,mes_nacimiento,dia_nacimiento)

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,valor):
        self._nombre = valor

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, valor):
        self._apellido = valor

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        self._edad = valor

    @property
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, anio_nacimiento: int,mes_nacimiento: int, dia_nacimiento: int):
        self._fecha_nacimiento = datetime(anio_nacimiento,mes_nacimiento,dia_nacimiento)

    
class Usuario(Persona):

    def __init__(self, nombreValor: str, apellidoValor: str, edadValor: int, anio_nacimiento: int, mes_nacimiento: int, dia_nacimiento: int,user_name: str,email: str,password: str):
        super().__init__(nombreValor, apellidoValor, edadValor, anio_nacimiento, mes_nacimiento, dia_nacimiento)
        self.__username = user_name
        self.__estado = True
        self.__email = email
        self.__password = password
        self.__fecha_alta = date.today()
        self.__fecha_baja = None

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, nuevo_username):
        self.__username = nuevo_username

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, nuevo_estado):
        self.__estado = nuevo_estado

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, nuevo_email):
        self.__email = nuevo_email

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, nueva_password):
        self.__password = nueva_password

    @property
    def fecha_alta(self):
        return self.__fecha_alta

    @property
    def fecha_baja(self):
        return self.__fecha_baja

    @fecha_baja.setter
    def fecha_baja(self, nueva_fecha_baja):
        self.__fecha_baja = nueva_fecha_baja
    
    def validar_credenciales(self,usuario: str, password: str):
        login_correcto = False
        if usuario == self.username and password == self.password:
            login_correcto = True
        print(login_correcto)
    
primer_usuario = Usuario("Nico","Cataldi",21,2002,3,20,"ElNico","mimail@mio.com","12346")

primer_usuario.validar_credenciales("ElNico","12346")

