###Gestion de control. Segunda version.
from modulo_funciones import ingreso_producto, busqueda_producto, modificar_producto, listado_productos, exportar_archivo, importar_archivo, obtener_stock

        
    
print("""Bienvenido al Sistema de gestión y Control de stock""")

# stock={
#     "procesador":{"cantidad":12,"precio":50000},
#     "motherboard":{"cantidad":10,"precio":11450},
#     "mouse":{"cantidad":52,"precio":5000},
#     "teclado":{"cantidad":14,"precio":4500},
# } 
###Datos para realizar pruebas básicas de funcionamiento, me gustaria cambiar los datos a mostrar quizas agregarle más.
#Que el diccionario queda algo así stock={ 100200 : {'producto':'procesador','cantidad':12,'precio':50000,'importado':False}} ***100200 es una especie de codigo del stock

stock= obtener_stock()

while True:
    print("""Seleccione su Opción.
          1 - Ingresar producto.
          2 - Buscar producto.
          3 - Modificar datos del producto.
          4 - Ver listado de stock.
          5 - Exportar a un Archivo.
          6 - Importar a un Archivo
          7 - Salir.
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
        ###Un simple print del diccionario, falta dejarlo bonito es muy basico y no es una linda salida.
        print("""\nOpcion 4
Listado de los productos en el inventario.""")   
        listado_productos(stock)
            
    elif opcion==5:
        print("""\nOpcion 5.
Importar desde un archivo!!!!!!!!!!!""")
        pass
    
    elif opcion==6:
        print("""\nOpcion 6
Exportar desde un Archivo!!!!!!!!!!!""")
        pass
    
    elif opcion==7:
        print("""\nOpcion 7
Saludos.
Adios!!!!!!!!!!!""")
        break
    else:
        print("""Opcion Incorrecta
Vuelta al menú""")
