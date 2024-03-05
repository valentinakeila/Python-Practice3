from autor import Autor
from libro import Libro
from datetime import date
from genero import Genero
from lista_lectura import ListaLectura

#autor
autor = Autor("Juan", "Foyd", date(2000,1,23))

#videos
libros = [
    Libro("El Principito"),
    Libro("Economia para no Economistas", autor),
    Libro("El Capital", autor)
]

#agrego los generos a los libros
libros[0].add_genero(Genero("Relato"))

libros[1].add_genero(Genero("Economia"))

libros[1].add_genero(Genero("Finanzas"))
libros[2].add_genero(Genero("Clasicos"))

#Genero 2 Listas de lectura
listas = [
    ListaLectura("Favoritos", 3),
    ListaLectura("Economia", 1),
    ListaLectura("Claiscos de siempre", 20)
]

#Agrego libros a la lista de lectura
listas[0].add_libro(libros[0])

listas[1].add_libro(libros[1])
listas[1].add_libro(libros[2])