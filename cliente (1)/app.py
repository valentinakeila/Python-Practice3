from cliente import Cliente
from pais import Pais
from provincias import *
from localidad import*
from datos import *



lista_cliente=[]

while True:
    opcion=int(input(f"""
        1- Registrar cliente
        2- Buscar cliente
        Selecciona una opcion: """))
    
    if opcion==1:
        nombre_apellido=input("Ingrese nombre y apellido: ")
        print("---Lista de paises:---")
        for pais in paises:
            print(pais)
        pais=Pais(input("Ingrese pais: "), )
        provincia=Provincia(input("Ingrese la provincia: "))
        pais.add_provincia(provincia)
        localidad=Localidad(input("Ingrese localidad: "), int(input("ingrese codigo postal: ")))
        provincia.add_localidad(localidad)
        direccion=input("ingrese direccion: ")
        nro_cliente= len(lista_cliente)+1
        lista_cliente.append(Cliente(nombre_apellido, nro_cliente, direccion, pais))
    elif opcion==2:
        cliente_buscado=int(input("Ingrese nro de cliente a buscar: "))
        for cliente in lista_cliente:
            if cliente_buscado==cliente.nro_cliente:
                print("Encontrado")
                bandera=True
                break
            else:
                print("cliente no encontrado.")
                bandera=False
        if bandera==True:
            
            opcion2=int(input(f"""
                      1- Modificar direccion.
                      2- Eliminar cliente.
                      3- Reactivar cliente.
                      4- Estado cliente.        
                      Seleccione una opcion:   """))
        if opcion2==1:
            nuevaLocalidad=input("Ingrese nueva localidad: ")
            provincia.nombre=nuevaLocalidad
            nuevaDireccion=input("ingrese nueva direccion: ")
            cliente.direccion=nuevaDireccion

        elif opcion2==2:
            cliente.eliminar_cliente()
        elif opcion2==3:
            cliente.reactivar_cliente()
        elif opcion2==4:
            print(f"""{cliente}
                 provincia: {provincia} 
                 localidad: {localidad}""")
                
        
            
    else:
        break
