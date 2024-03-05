from datos import *

def menu(): 
    return "\n1 - Nueva Compra\n2 - Resumen Compras\n3 - Salir\n"

def menu_compra():
    return "\n1 - Agregar Producto\n2 - Finalizar Compra\n"



while True:
    print(menu())
    opt = input("Ingrese la opcion seleccionada: ")
    opt2 = 0
    if opt == "1":
            nombreCliente = input("Ingrese su nombre")
            apellidoCliente = input("Ingrese su apellido")
            dniCliente = input("Ingrese su dni")
            compra = (Cliente(nombreCliente,apellidoCliente,dniCliente))
            while opt != 2: 
                
                
                print(menu_compra())   
                opt2 = input("Ingrese una opcion: ")
                if opt2 == "1":
                    contador_opcion = 0
                    
                    for i in productos:
                        print(f"{contador_opcion + 1} - {i} ")
                        contador_opcion = contador_opcion + 1
                    producto_elegido = input("Ingrese el producto que desea agregar a su carrito")
                    producto_elegido = int(producto_elegido) - 1
                    compra.add_producto(productos[producto_elegido])
                elif opt2 == "2" :
                    ""
                else:
                    print("Error, Ingrese una opcion valida...")



                      
            
    elif opt == "2":
        pass
    elif opt == "3":
        print("Gracias por utilizar nuestro sistema.")
        break
    else:
        print("Error, Ingrese una opcion valida...")