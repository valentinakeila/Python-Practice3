class TipoDocumento():
    def __init__(self, tipoDocumento: str) -> None:
        self.__tipoDocumento = tipoDocumento


    @property
    def tipoDocumento(self):
        return self.__tipoDocumento
    
    