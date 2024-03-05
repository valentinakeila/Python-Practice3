from video import Video

class ListaReproduccion():

    __prox_num = int(0)

    def __init__(self, nombre:str) -> None:
        self.__videos:list(Video) = []
        self.__nombre = nombre
        self.__nro = ListaReproduccion.get_prox_num()

    @property
    def nro(self) -> str:
        return self.__nro

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre) -> None:
        self.__nombre = nuevo_nombre

    @property
    def videos(self) -> list:
        return self.__videos

    @property
    def cantidad_videos(self) -> int:
        return len(self.videos)

    @classmethod
    def get_prox_num(cls) -> int:
        cls.__prox_num += 1
        return cls.__prox_num

    def __str__(self) -> str:
        return f"{self.nombre} [{self.cantidad_videos}]"

    def add_video(self, video: Video) -> None:
        self.__videos.append(video)

    def remove_video(self, video: Video) -> None:
        self.__videos.remove(video)
        
