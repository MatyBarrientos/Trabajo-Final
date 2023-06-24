###Gestion de control. Segunda version.
from modulo_funciones import obtener_stock,ingreso_producto, busqueda_producto, modificar_producto, listado_productos

        
    
print("""Bienvenido al Sistema de gestión y Control de stock""")



stock = obtener_stock()

while True:
    print("""Seleccione su Opción.
          1 - Ingresar producto.
          2 - Buscar producto.
          3 - Modificar datos del producto.
          4 - Ver listado de stock.
          5 - Salir.
           """)
    while True:
        try:
            opcion=int(input("Ingrese su opción: "))
            break
        except:
            print("Tiene que ser un valor númerico: ")
    
    if opcion==1: 
        print("""\nOpcion 1
Ingreso de un nuevo producto dentro del stock""")
        ingreso_producto(stock)
     
    elif opcion==2:   
        print("""\nOpcion 2
Buscaremos un artículo en el stock.""")
        busqueda_producto(stock)
  
    elif opcion==3:
        print("""\nOpcion 3
Modificar producto.""")
        modificar_producto(stock)
               
    elif opcion==4: 
        print("""\nOpcion 4
Listado de los productos en el inventario.""")   
        listado_productos(stock)
            
    elif opcion==5:
        print("""\nOpcion 7
Saludos.
Adios!!!!!!!!!!!""")
        break
    else:
        print("""Opcion Incorrecta
Vuelta al menú""")
