import datetime
from producto import Producto
from descuento import Descuento
from cliente import Cliente
class Compra():
    def __init__(self, cliente: Cliente):
        self.__cliente = cliente
        self.__fecha_hora = datetime.datetime.now()
        self.__cantidad_productos = 0
        self.__monto_total = 0
        self.__compra_facturada = False
        self.__monto_facturado = 0
        self.__productos = []

    @property
    def cliente(self):
        return self.__cliente

    @property
    def fecha_hora(self):
        return self.__fecha_hora

    @property
    def cantidad_productos(self):
        return self.__cantidad_productos

    @cantidad_productos.setter
    def cantidad_productos(self, cantidad):
        self.__cantidad_productos = cantidad

    @property
    def monto_total(self):
        return self.__monto_total

    @monto_total.setter
    def monto_total(self, monto):
        self.__monto_total = monto

    @property
    def compra_facturada(self):
        return self.__compra_facturada

    @compra_facturada.setter
    def compra_facturada(self, facturada):
        self.__compra_facturada = facturada

    @property
    def monto_facturado(self):
        return self.__monto_facturado

    @monto_facturado.setter
    def monto_facturado(self, monto):
        self.__monto_facturado = monto

    @property
    def productos(self):
        return self.__productos

    @productos.setter
    def productos(self, lista_productos):
        self.__productos = lista_productos


    def __str__(self):
        return f"Cliente: {self.__cliente} Fecha de la compra: {self.__fecha_hora} Cantidad de productos: {self.__cantidad_productos} Monto a total pagar: {self.__monto_total} Monto con descuento aplicado: {self.__monto_facturado} Productos: {self.__productos}"

    def add_producto(self,producto: Producto):
        self.__productos.append(producto)
        self.__cantidad_productos = len(self.productos)
    
    def remove_producto(self,producto: Producto):
        self.productos.remove(producto)

    def facturar_compra(self):
        for i in range(0,len(self.__productos)):
            self.__monto_total = self.__monto_total + self.__productos[i].precio
        if self.__cliente.nro_comunidad != None:
            self.__monto_facturado = Descuento.pago_con_comunidad(self.__monto_total)
            self.__compra_facturada = True
            print(f"Monto total: ${self.__monto_total}\nMonto con descuento de comunidad: ${self.__monto_facturado}")
        else:
            print(f"Monto a pagar: ${self.__monto_total}")
        

""" compra = Compra(Cliente("El nico","El cataldi","44064311"))
compra.productos = [Producto("Vermouth MARTINI Extra Dry Botella 995 Cc", float(2258.00))]
compra.cantidad_productos = 1
compra.facturar_compra()
 """