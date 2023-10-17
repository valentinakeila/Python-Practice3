"""Properties"""


class Article:
    """Re-Escribir el ejercicio anterior utilizando una property en vez de un
    método de instancia.

    Restricciones:
        - Utilizar 3 variables de instancia
        - Utilizar 1 property
        - Utilizar 1 variable de clase
        - Utilizar 1 método de clase
        - No utilizar métodos de instancia
        - No utilizar Dataclasses
        - Utilizar Type Hints en todos los métodos y variables
    """
  #variable de clase
    iva = 0.21
    #constructor
    def __init__(self, nombre: str, costo: float, descuento: float = 0): #valores que ingresa el usuario
        self.nombre = nombre  #ponemos el self para que reconozca que es un atributo del objeto osea que esta dentro de la clase y no es una variable cualquiera 
        self.costo = costo #variable de instancia
        self.descuento = descuento #se puede declara un atributo con un valor fijo sin pedirle al usuario
    
    #property
    @property
    def precio(self) -> float:
        precioDesc = self.costo - self.descuento
        precioIva = precioDesc * (1 + self.iva)
        return round(precioIva, 2)
    
    @classmethod
    def actualizar_iva(cls, nuevo_iva: float):
        cls.iva = nuevo_iva


# NO MODIFICAR - INICIO
# Test parámetro obligatorio
try:
    article = Article()
    assert False, "No se puede instanciar sin nombre ni costo"
except TypeError:
    assert True

try:
    article = Article("Auto")
    assert False, "No se puede instanciar sin costo"
except TypeError:
    assert True

try:
    article = Article(nombre="Auto", costo=1)
    assert True
except TypeError:
    assert False, "El descuento es opcional"

try:
    article = Article(nombre="Auto", costo=1)
    article.precio = 2
    assert False, "No se puede modificar el precio"
except AttributeError:
    assert True


# Test básico
article = Article("Auto", 1)
assert article.nombre == "Auto"
assert article.precio == 1.21


article = Article("Auto", 1, 0.21)
assert article.nombre == "Auto"
assert article.precio == 0.96


# Test palabra clave
article = Article(costo=1, nombre="Auto")
assert article.nombre == "Auto"
assert article.precio == 1.21

article = Article(costo=1, nombre="Auto", descuento=0.21)
assert article.nombre == "Auto"
assert article.precio == 0.96


# Test de método de clase
Article.actualizar_iva(0.25)

article = Article(costo=1, nombre="Auto")
assert article.nombre == "Auto"
assert article.precio == 1.25
# NO MODIFICAR - FIN
