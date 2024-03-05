from datos import *

def menu(): 
    return "\n1 - Pagina principal\n2 - Nueva Lista de lectura\n3 - Ver listas de lectura\n4 - Salir\n"

def nueva_lista():
    print("Creando una lista de Lectura ...")
    nombre = input("Ingrese el nombre de la lista: ")
    codigo = int(input("Ingrese el código de la lista: "))
    lista = ListaLectura(nombre, codigo)

    print("Seleccione al menos un libro para crear la lista...")
    for i,libro in enumerate(libros,1):
        print(f"{i} - {libro.nombre}")

    index_libro = int(input("Seleccione el libro: "))
    l = libros[index_libro-1]

    lista.add_libro(l)
    listas.append(lista)

    print("Se creo la lista exitosamente...")

while True:
    print(menu())
    opt = input("Ingrese la opcion seleccionada: ")
    if opt == "1":
        for libro in sorted(libros, key=lambda x: x.nombre):
            print(libro)
        continue
    if opt == "2":
        nueva_lista()
        continue
    if opt == "3":
        for lista in listas:
            if lista.cantidad_libros:
                print(lista)
        continue
    if opt == "4":
        print("Gracias por utilizar nuestro sistema.")
        break
    else:
        print("Error, Ingrese una opcion valida...")