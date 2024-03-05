class Cliente():

    def __init__(self,nombre: str,apellido: str,nro_documento: str,nro_comunidad: int = None):
         self.__nombre = nombre
         self.__apellido = apellido
         self.__nro_documento = nro_documento
         self.__nro_comunidad = nro_comunidad


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
    def nro_documento(self):
        return self.__nro_documento

    @nro_documento.setter
    def n(self, valor):
        self.__nro_documento = valor

    @property
    def nro_comunidad(self):
        return self.__nro_comunidad

    @nro_comunidad.setter
    def n(self, valor):
        self.__nro_comunidad = valor



         
          
         