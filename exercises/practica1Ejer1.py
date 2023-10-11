from datetime import date

"""
Requerimientos:
Codificar todos los atributos privados con @property.
Para crear (instanciar) un usuario:
Se ingresa el user_name y email .Se asigna en fecha_alta la fecha del día y estado True.
Luego se le solicita al usuario que ingrese su contraseña.
Una vez creado el usuario al mismo no se le puede cambiar el user_name(sólo lectura).
Luego de creado el usuario, se pueden ingresar los demás datos del usuario.
Al dar de baja el usuario, el mismo no se elimina, si no que su estado cambia a False y se le
asigna en fecha_baja la fecha del día.
Al validar las credenciales, se retorna verdadero si el usuario y pass ingresado coincide con el
user_name y password el usuario; en caso contrario se retorna False.

Utilizar los siguientes imports y funciones/métodos.
from datetime import date
x = date.today()

"""

class Usuario:
    
    def __init__(self, usuarioValor: str ,emailValor: str, passValor: str):
        self.__user_name = usuarioValor #__ pq es privada
        self.__email = emailValor
        self.__estado = True
        self.__password = passValor
        self.__nombre = ""
        self.__apellido = ""
        self.__fecha_alta = date.today()
        self.__fecha_baja = None
    
    def validar_credenciales() -> bool:
        print()
        
    def darDeBaja(self):
        self.__estado = False
        self.__fecha_baja = date.today()

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevoNombre: str):
        self.__nombre = nuevoNombre

    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, nuevoContraseña: str):
        self.__password = nuevoContraseña 

    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self, nuevoApellido: str):
        self.__apellido = nuevoApellido

    @property #esto es el getter lo usas para agarrar la variable privada
    def userName(self):
        return self.__user_name
    
    """@userName.setter
    def userName(self, nuevoUserName: str):
        self.__user_name = nuevoUserName""" #lo comentamos al setter porque el ejercicio dice que es solo lectura osea no se puede cambiar

#---------------------------------------------------

nuevo_usuario = Usuario("Valen", "valen@gmail.com", "1234")#estas poniendo nuevo_usuario porque estas instanciando la clase para usarla despues con los prints estas pasando los parametros entre ()
# print(nuevo_usuario.__username) esto no se puede hacer porque es un atributo privado
print(nuevo_usuario.userName) # aca llamas al getter osea userName
"""nuevo_usuario.userName = "Nico" #si le pasas parametros llamas al setter (eso se llama sobrecarga de metodos creo)"""""""""
"""print(nuevo_usuario.userName)""" #si no manda parametros llama al getter

nueva_contraseña = input("Ingrese una contraseña\n") 
nuevo_usuario.password = nueva_contraseña 
print(nuevo_usuario.password)

