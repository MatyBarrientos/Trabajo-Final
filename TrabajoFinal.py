###Gestion de control. Segunda version.
from paquete_funciones.modulo_funciones import obtener_stock,ingreso_producto, busqueda_producto, modificar_producto, listado_productos,impresionGenral,busqueda_nombre,borrar_producto_id
    
print("""Bienvenido al Sistema de gestión y Control de stock""")

stock = obtener_stock()

while True:
    print("""Seleccione su Opción.
          
          1 - Ver listado de stock.
          2 - Ingresar producto.
          3 - Borrar producto.
          4 - Buscar producto por código.
          5 - Buscar producto por nombre.
          6 - Modificar datos del producto.
          7 - Salir.
           """)
    while True:
        try:
            opcion = int(input("Ingrese su opción: "))
            break
        except:
            print("Tiene que ser un valor númerico: ")
    if opcion == 1: 
        print("""\nOpcion 1
Listado de los productos en el inventario.""")   
        listado_productos(stock) 
         
    elif opcion == 2: 
        print("""\nOpcion 2
Ingreso de un nuevo producto dentro del stock""")
        ingreso_producto(stock)
        
    elif opcion == 3:
        print("""\nOpcion 3
Eliminar un artículo del Stock.""")
        borrar_producto_id(stock)
        
    elif opcion == 4:   
        print("""\nOpcion 4
Buscaremos un artículo por código en el stock.""")
        busqueda_producto(stock)

    elif opcion == 5:
        print("""\nOpcion 5
Buscaremos un artículo por nombre en el stock.""")  
        busqueda_nombre(stock)
  
    elif opcion == 6:
        print("""\nOpcion 6
Modificar producto.""")
        modificar_producto(stock)
                           
    elif opcion == 7:
        print("""\nOpcion 7
Saludos.
Adios!!!!!!!!!!!""")
        break
        
    elif(opcion==10):
        impresionGenral(stock)
        
    else:
        print("""Opcion Incorrecta
Vuelta al menú""")
        
        
