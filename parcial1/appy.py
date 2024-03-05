from aspirante import Aspirante
from carrera import Carrera
from titulo import Titulo
from inscripcion import Inscripcion
from datetime import date
from datos import *

def menu(): 
    return "\n1 - Nueva Inscripción\n2 - Ver carreras\n3 - Ver inscripciones\n4 - Salir\n"

def nueva_inscripcion():
    for i, carrera in enumerate(carreras):
        print(f"{i + 1} - Carrera: {carrera.nombre}") #carrera es del for y nombre la clase carrera
    index_carrera = int(input("Seleccione la carrera: "))
    c = carreras[index_carrera-1]

    print("Datos del aspirante...")
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    email = input("Ingrese el email: ")
    nro_telefono = input("Ingrese el numero de telefono: ")
    a = Aspirante(nombre, apellido, email, nro_telefono)

    print("Indicar el titulo de grado del aspirate...")
    for i,titulo in enumerate(titulos,1):
        print(f"{i} - {titulo.nombre}")

    index_titulo = int(input("Seleccione el titulo: "))

    a.add_titulo(titulos[index_titulo-1])
    inscripciones.append(Inscripcion(a, c))

    print("Se registró la inscripción exitosamente...")



while True:
    print(menu())
    opt = input("Ingrese la opción seleccionada: ")
    if opt == "1":
        nueva_inscripcion()
        continue
    if opt == "2":
        carreras_ord_fecha = sorted(carreras, key=lambda x: x.fecha_comienzo)
        for carrera in carreras_ord_fecha:
            print(carrera)
        continue
    if opt == "3":
        for inscripcion in inscripciones:
            if inscripcion.inscripcion_activa:
                print(inscripcion)
       
        continue
    if opt == "4":
        print("Saludos.")
        break
    else:
        print("Ingrese una opcion valida.")