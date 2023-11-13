from datetime import date
import secrets
class Libro():
    def __init__(self, nombre: str, autor, fecha_lanzamiento: date ) -> None:
        self.__nombre = nombre
        self.__autor = "Unknown"
        self.__fecha_lanzamiento = fecha_lanzamiento
        self.__isbn = self.generar_isbn()


    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, valor):
        self.__autor = valor

    @property
    def fecha_lanzamiento(self):
        return self.__fecha_lanzamiento

    @fecha_lanzamiento.setter
    def fecha_lanzamiento(self, valor):
        self.__fecha_lanzamiento = valor

    @property
    def isbn(self):
        return self.__isbn


    def generar_isbn(self):
        isbn = 4
        return secrets.token_urlsafe(isbn)