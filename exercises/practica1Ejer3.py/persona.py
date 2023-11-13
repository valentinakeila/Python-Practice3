import abc
from abc import ABC, abstractmethod
from datetime import *
from libro import *

class Persona(ABC):
    def __init__(self, nombre: str, apellido: str, fecha_nacimiento: date, edad: int, nro_documento: int ) -> None:
      self._nombre = nombre
      self._apellido = apellido
      self._fecha_nacimiento = fecha_nacimiento
      self._edad = edad
      self._nro_documento = nro_documento

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
    def fecha_nacimiento(self):
        return self._fecha_nacimiento

    @fecha_nacimiento.setter
    def fecha_nacimiento(self, valor):
        self._fecha_nacimiento = valor

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        self._edad = valor

    @property
    def nro_documento(self):
        return self._nro_documento

    @nro_documento.setter
    def nro_documento(self, valor):
        self._nro_documento = valor
    
   


  