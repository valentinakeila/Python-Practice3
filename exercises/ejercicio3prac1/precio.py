class Precio:
    def __init__(self, precio: float):
        self.__precio = precio
    
    def calcular_importe(self,cant_horas: int):
        return cant_horas * self.__precio

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self,valor):
        self.__precio = valor