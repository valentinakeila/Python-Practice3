class Usuario():
    def __init__(self, nombre: str, apellido: str, email: str, contrasenia: str):
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._contrasenia = contrasenia

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, nuevo_apellido):
        self._apellido = nuevo_apellido

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, nuevo_email):
        self._email = nuevo_email

    @property
    def contrasenia(self):
        return self._contrasenia

    @contrasenia.setter
    def contrasenia(self, nueva_contrasenia):
        self._contrasenia = nueva_contrasenia


    def __str__(self):
        return "Nombre: " + self._nombre + " Apellido: " + self._apellido + " Email: " + self._email + " Contraseña: " + self._contrasenia

    def validar_credenciales(self, email: str, contrasenia: str):
        if self._email == email and self._contrasenia == contrasenia:
            return True, "Credenciales correctas"
        return False, "Credenciales incorrectas"
