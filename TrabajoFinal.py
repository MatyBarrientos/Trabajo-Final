###Gestion de control. Segunda version.
from modulo_funciones import obtener_stock,ingreso_producto, busqueda_producto, modificar_producto, listado_productos,impresionGenral,busqueda_nombre
    
print("""Bienvenido al Sistema de gestión y Control de stock""")

stock = obtener_stock()

while True:
    print("""Seleccione su Opción.
          1 - Ingresar producto.
          2 - Buscar producto por código.
          3 - Buscar producto por nombre.
          4 - Modificar datos del producto.
          5 - Ver listado de stock.
          6 - Salir.
           """)
    while True:
        try:
            opcion = int(input("Ingrese su opción: "))
            break
        except:
            print("Tiene que ser un valor númerico: ")
    
    if opcion == 1: 
        print("""\nOpcion 1
Ingreso de un nuevo producto dentro del stock""")
        ingreso_producto(stock)
     
    elif opcion == 2:   
        print("""\nOpcion 2
Buscaremos un artículo por código en el stock.""")
        busqueda_producto(stock)

    elif opcion == 3:
        print("""\nOpcion 5
Buscaremos un artículo por nombre en el stock.""")  
        busqueda_nombre(stock)
  
    elif opcion == 4:
        print("""\nOpcion 3
Modificar producto.""")
        modificar_producto(stock)
               
    elif opcion == 5: 
        print("""\nOpcion 4
Listado de los productos en el inventario.""")   
        listado_productos(stock)
        

          
    elif opcion == 6:
        print("""\nOpcion 6
Saludos.
Adios!!!!!!!!!!!""")
        break
    

        
    elif(opcion==10):
        impresionGenral(stock)
        
    else:
        print("""Opcion Incorrecta
Vuelta al menú""")
        
        
