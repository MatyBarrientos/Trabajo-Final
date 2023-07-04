###Gestion de control. Segunda version.
from paquete_funciones.funciones_principales import obtener_stock, listado_productos, ingreso_producto, busqueda_codigo, busqueda_nombre, busqueda_marca, modificar_producto, borrar_producto_id, impresionGeneral
from paquete_funciones.funciones_auxiliares import obtener_entero, limpiar_pantalla
    
print("""\nBienvenido al Sistema de gestión y Control de stock""")

stock = obtener_stock()

while True:
    print("""\nSeleccione su Opción.
          
          1 - Ver listado de stock.
          2 - Ingresar producto.
          3 - Borrar producto.
          4 - Busqueda.
          5 - Modificar datos del producto.
          6 - Salir. 
           """)

    opcion = obtener_entero("Ingrese su opción: ","Tiene que ser un valor númerico: ")

    if opcion == 1:
        limpiar_pantalla() 
        print("""Opcion 1
Listado de los productos en el inventario.\n""")   
        listado_productos(stock) 
         
    elif opcion == 2:
        limpiar_pantalla() 
        print("""Opcion 2
Ingreso de un nuevo producto dentro del stock.\n""")
        ingreso_producto(stock)
        
    elif opcion == 3:
        limpiar_pantalla()
        print("""Opcion 3
Eliminar un artículo del Stock.\n""")
        borrar_producto_id(stock)
        
    elif opcion == 4:
        limpiar_pantalla()   
        print("""Opcion 4.\n""")

        while True:
            print("""\nSub-menú busquedas
                  
1 - Buscar productos por código.

2 - Buscar productos por nombre.

3 - Buscar productos por marca.

4 - Salir.\n""")
            opcion_sub=obtener_entero("Ingrese su opción de busqueda: ","Tiene que ser un valor númerico: ")
            if opcion_sub == 1:
                busqueda_codigo(stock)
            elif opcion_sub == 2:
                busqueda_nombre(stock)
            elif opcion_sub == 3:
                busqueda_marca(stock)
            elif opcion_sub == 4:
                print("\nVuelta al menú principal.")
                break
            else:
                print("""\nOpcion incorrecta
Vuelta al submenú.""")

    elif opcion == 5:
        limpiar_pantalla()
        print("""Opcion 5
Modificar producto.\n""")
        modificar_producto(stock)
                           
    elif opcion == 6:
        limpiar_pantalla()
        print("""\nOpcion 6
Saludos.
Adios!!!!!!!!!!!""")
        break
    elif opcion ==10:
        limpiar_pantalla()
        print("""Fuera del menú visible.
muestra como es el diccionario que contiene diccionario""")
        impresionGeneral(stock)   
        
    else:
        print("""Opcion Incorrecta
Vuelta al menú""")
        
        
