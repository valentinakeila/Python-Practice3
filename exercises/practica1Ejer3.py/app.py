from usuario import *
from libro import *
from datetime import date

libros = [Libro("El Principito","Antoine de Saint-Exupéry",date(1943,4,6)),
Libro("Juan Salvador Gaviota","Richard Bach",date(1970,1,1))]

administrador = Usuario('admin','admin',date(2023,6,20), 23, 100000, 'admin', 'admin')
administrador.administrador = True

usuario1 = Usuario("Nicolas", "cataldi",date(2002,3,20),21, 140000, "nico", "ninini" )
usuario2 = Usuario("Valentina", "Garrido", date(2009, 1, 1), 12, 789012, "valen", "valenlamejor")
usuario3 = Usuario("Geraldine", "Mendiola", date(2023, 1, 1), 0, 345678, "ger", "geri")

# Agregar instancias a la lista de usuarios
usuarios = [usuario1, usuario2, usuario3, administrador]


def menu_principal():
    print("1 - Ingresar como usuario")
    print("2 - Ingresar como administrador")
    print("3 - Ver libros del usuario...")
    print("4 - Ver usuario del libro...")
    print("5 - Salir")

def menu_administrador():
    print("1 - Nuevo usuario")
    print("2 - Nuevo libro")
    print("3 - Cerrar sesión")
def menu_usuario():
    print("1 - Agregar libro a mi coleccion")
    print("2 - Quitar libro de mi coleccion")
    print("3 - Cerrar sesión")

while True:
    menu_principal()
    opt = input("Ingrese una opción")
    if opt == "1":
        ingresoUsuario()
        pass
    if opt == "2":
        ingresoAdministrador()
        pass
    if opt == "3":
        pass
    if opt == "4":
        pass
    if opt == "5":
        print("Saludos!.")
        break


    def ingresoUsuario():
        print("Ingrese sus credenciales")
        ingresoUsuario = input("User:" )
        credencial_contrasenia = input("Contraseña: ")
        usuario_indice= 0

        for i in usuarios: 
           if ingresoUsuario == i.user_name and credencial_contrasenia == i.contraseña:
            resultado_login = True
            break
           else: usuario_indice = usuario_indice + 1 # Se encontro el usuario
        
           
        if resultado_login == False:
            print("Datos incorrectos")
        else: 
            menu_usuario()
            while True:
                menu_principal()
                opt = input("Ingrese una opción")
                if opt == "1":
                    contador_libros = 0

                    for i in range(0,len(libros)):
                        contador_libros = contador_libros + 1
                        print(contador_libros + " " + i.nombre) #el nombre de la clase
                
                    libroElegido = int(input("Ingrese una opción"))
                    usuarios[usuario_indice].agregar_libro(libros[libroElegido - 1])

                    pass
                if opt == "2":
                      contador_libros = 0

                      for i in range(0,len(usuarios[usuario_indice].mis_libros)):
                        contador_libros = contador_libros + 1
                        print(contador_libros + " " + i.nombre) #el nombre de la clase
                
                        libroEliminado = int(input("Ingrese una opción"))
                        usuarios[usuario_indice].quitar_libro(libros[libroEliminado - 1])
                        pass
                if opt == "3":
                    print("Saludos!.")
                    break


    def ingresoAdministrador():
        print("Ingrese sus credenciales")
        ingresoUsuario = input("User:" )
        credencial_contrasenia = input("Contraseña: ")
        usuario_indice= 0

        for i in usuarios: 
           if ingresoUsuario == i.user_name and credencial_contrasenia == i.contraseña:
            resultado_login = True
            break
           else: usuario_indice = usuario_indice + 1 # Se encontro el usuario
        
           
        if resultado_login == False:
            print("Datos incorrectos")


            
