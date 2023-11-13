from datetime import *
from aspirante import Aspirante
from carrera import Carrera

class Inscripcion():
    prox_num = int(0)

        
    def __init__(self, aspirante: Aspirante, carrera: Carrera) -> None:
        self.__aspirante = aspirante
        self.__carrera = carrera
        self.__fecha_inscripcion = date.today()
        self.__inscripcion_activa = True
        self.__nro = Inscripcion.get_prox_num()

    @property
    def aspirante(self) -> object:
        return self.__aspirante
    
    @property
    def carrera(self) -> object:
        return self.__carrera

    @property
    def fecha_inscripcion(self) -> date:
        return self.__fecha_inscripcion

    @property
    def inscripcion_activa(self) -> bool:
        return self.__inscripcion_activa

    @inscripcion_activa.setter
    def inscripcion_activa(self, nuevo_estado:bool) -> None:
        self.__inscripcion_activa = nuevo_estado

    @property
    def nro(self) -> int:
        return self.__nro

    @classmethod
    def get_prox_num(cls) -> int:
        cls.prox_num += 1
        return cls.prox_num

    def __str__(self) -> str:
        return f"Inscripción número {self.nro}, Aspirante: {self.aspirante.nombre} {self.aspirante.apellido}, Carrera: {self.carrera.nombre}"