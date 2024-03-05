from datetime import date
from tag import Tag
from usuario import Usuario

class Video():

    def __init__(self, nombre:str, usuario: Usuario) -> str:
        self.__nombre = nombre
        self.__fecha_publicacion = date.today()
        self.__palabras_claves = []
        self.__usuario = usuario

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre) -> None:
        self.__nombre = nuevo_nombre

    @property
    def usuario(self) -> Usuario:
        return self.__usuario

    @property
    def fecha_publicacion(self) -> str:
        return f"{self.__fecha_publicacion.day}/{self.__fecha_publicacion.month}/{self.__fecha_publicacion.year}"

    @property
    def palabras_claves(self) -> list:
        return self.__palabras_claves

    def add_tag(self, tag: Tag) -> None:
        self.__palabras_claves.append(tag)

    def remove_tag(self, tag: Tag) -> None:
        self.__palabras_claves.remove(tag)

    def __str__(self) -> str: 
        return f"{self.nombre} [ Autor: {self.usuario.nombre} - Publicado: {self.fecha_publicacion} ]"
