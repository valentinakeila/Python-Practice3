class Titulo():

    def __init__ (self, nombre: str, universidad: str) -> None:
        self.__nombre = nombre
        self.__universidad = universidad

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        self.__nombre = valor

    @property
    def universidad(self) -> str:
        return self.__universidad

    @universidad.setter
    def universidad(self, valor: str) -> None:
        self.__universidad = valor

    def __str__(self) -> str:
        return f"Titulo: {self.nombre} expedido por {self.universidad}"