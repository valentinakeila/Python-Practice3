from cliente import Cliente
from producto import Producto
from datetime import date
from descuento import Descuento
from compra import Compra

#inicializo lista vacía
compras = []

#genero 2 clientes
cliente1 = Cliente("Juan", "Perez", "37514256", 333)
cliente2 = Cliente("Marta", "Sanchez", "42514785")

#genero productos
productos = [
    Producto("Cerveza Weisse PATAGONIA Botella 730 Cc", float(970.98)),
    Producto("Vino Blanco Dulce TORO Ttb 1 Ltr", float(660.30)),
    Producto("Vermouth MARTINI Extra Dry Botella 995 Cc", float(2258.00))
]

#genero compras
compras.append(Compra(cliente1))
compras.append(Compra(cliente2))

#agrego productos da las compras
compras[0].add_producto(productos[0])
compras[0].add_producto(productos[0])
compras[0].add_producto(productos[0])
compras[0].add_producto(productos[0])
compras[0].add_producto(productos[0])
compras[0].add_producto(productos[0])

compras[1].add_producto(productos[1])
compras[1].add_producto(productos[1])
compras[1].add_producto(productos[2])

#facturar compras
compras[0].facturar_compra()
compras[1].facturar_compra()