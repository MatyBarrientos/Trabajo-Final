from paquete_funciones.funciones_generales import obtener_entero, obtener_flotante, limpiar_pantalla
from tabulate import tabulate #importe el paquete de la libreria tabulate para mostrar info por pantalla https://pypi.org/project/tabulate/
import json

def obtener_stock():
    """Carga los datos de un archivo Json, en caso de no existir crea un diccionario vacio"""
    try:
        filename = 'lista_stock.json'
        with open (filename,'r') as file:
            stock = json.load(file)      
    except FileNotFoundError:
        stock = {}
    return stock

def guardar_stock(stock):
    '''esta función actualiza los datos alojados en el diccionario Stock y lo vuelva en el archivo Json.
    
    Args :
        stock {dic} : Diccionario que contiene un stock.
    '''
    filename = 'lista_stock.json'
    with open(filename, 'w') as file :
        json.dump(stock, file, indent = 2)
        
def listado_productos (lista_stock): 
    #muestro por pantalla en formato de tabla todos los articulos del diccionario (quedó bonito)
    limpiar_pantalla()
    
    if lista_stock: #Si el diccionario no está vacio se procede la siguiente manera.
        
        encabezados = ['id','producto','marca', 'cantidad','precio','importado'] #la variable encabezado es una lista y tiene los encabezados de la tabla  
        
        filas = [[codigo, datos["producto"], datos["marca"], datos["cantidad"],datos["precio"],datos["importado"]] for codigo, datos in lista_stock.items()]
        #fila es una lista creada por compresión donde se toma cada value del diccionario "stock" y se lo recorre mediente un for. (lo hice así para ahorrar un par de lineas)
        tabla = tabulate(filas, headers=encabezados, tablefmt='fancy_grid') 
        #utilizé la funcion tabulate recibé 3 argumentos: filas,el encabezado (ambos son listas con contenido del stock) y tablefmt es para darle el estilo de la tabla me gustó "fancy_grid".
        print(tabla)
    else:
        print("No hay entradas en la lista.")
        #en caso de estar vacio, muestra este mjs.
        
def ingreso_producto (lista_stock):
    """Ingreso de un nuevo artículo en el stock y al final se actualiza el arvicho Json.

    Args:
        lista_stock {dic}: Diccionario que contiene el stock
    """
    
    limpiar_pantalla()
    #una funcion limpiar pantalla para no andar cargando de tanta info la consola
    codigo =str( obtener_entero("Ingrese el código del producto: ", "el código debe ser representado en un número entero."))
    #utilizamos la funcion obtener_entero para no estar poniendo condicionales cada vez que se pida por consola algún valor.
    producto = input("Ingrese el nombre del producto: ").lower() 
    
    marca = input("Ingrese la marca: ").lower() 

    cantidad = obtener_entero("Ingrese la cantidad a ingresar el producto (unidades enteras): ","Las unidades se representan en números enteros")
    
    precio = obtener_flotante("Ingrese el precio unitario del producto: $","El precio debe ser representado en números.")
    #utilizamos la funcion obtener_flotante para no estar poniendo condicionales cada vez que se pida por consola algún valor.
    
    importado_int = obtener_entero("El producto es de origen nacional? : (1-Sí o 2-No): ", "Opción Invalida (1-Sí o 2-No): ")
    while importado_int != 1 and importado_int != 2:
        importado_int = obtener_entero("El producto es de origen nacional? : (1-Sí o 2-No): ", "Opción Invalida (1-Sí o 2-No): ")  
    if(importado_int == 1):
            importado=True
    elif(importado_int == 2):
            importado=False
     
    lista_stock[codigo] = {'producto':producto,'marca': marca, 'cantidad':cantidad,'precio': precio ,'importado':importado}
    #creación del diccionario con sus respectivas keys y values.
    guardar_stock(lista_stock) #se llama a la funcion guardar_stock para actualizar los datos en el archivo .Json
    
def borrar_producto_id(lista_stock):
    """se borra determinada entrada, se los busca por codigo

    Args:
        lista_stock (dicc): diccionario que almacena el stock
    """
    codigo = str(obtener_entero("Ingrese el código del producto: ", "el código debe ser representado en un número entero."))
    
    if codigo in lista_stock:
        
        del lista_stock[codigo]
        print(f"entrada {codigo} borrada")
        
    else:
        print(f"la entrada {codigo} no se encuentra en el stock")
    guardar_stock(lista_stock)

def busqueda_producto(lista_stock):
    """_Devuelve por pantalla los datos de un determinado producto_

    Args:
        lista_stock (Dic): _el diccionario con los datos del stock_
    """
    limpiar_pantalla()
    
    codigo = str(obtener_entero("Ingrese el nombre del producto: ", "Opción Invalida, debe ser un número entero: "))
    
    if codigo in lista_stock: 
        #si el código se encuentra dentro de la lista del stock, te muestra los datos (un choclo hermoso)
        print(f"El código {codigo} se encuentra en el inventario.")
        print ((f"{'producto':<15} | {'marca':<15} | {'cantidad':<15} | {'precio':<15}"))
        print ("-" * 65)
        print (f"{lista_stock[codigo]['producto']:<15} | {lista_stock[codigo]['marca']:<15} | {lista_stock[codigo]['cantidad']:<15} | {lista_stock[codigo]['precio']:<15}")
        print ("-" * 65)
            
    else:
        print(f"No se ha encontrado una entrada con la descripción {codigo}")
        #si no está te muestra un mjs diciendo que no está y procede a preguntar si lo querés agregar?, en caso de ser afirmativo llama a la funcion ingreso_producto()
        opcion = obtener_entero(f"Desea ingresar {codigo} a la lista? (1='Si' o 2='No') : ","Opción Invalida, debe ser un número entero (1='Si' o 2='No')")
        while opcion != 1 and opcion != 2: #un while para quedar en bucle en caso de que no sean los valores esperados "1 o 2"
            opcion = obtener_entero(f"Desea ingresar {codigo} a la lista? (1='Si' o 2='No') : ","Opción Invalida, debe ser un número entero (1='Si' o 2='No')")
        if opcion == 1 : #el if está fuera del while si opcion es 1 o 2 pasa directamente acá.
                ingreso_producto(lista_stock) #se llama a una función dentro de otra función
        else:
                print("Vuelta al menú...") #mjs de ***vuelta al menú.***
                
def busqueda_nombre(lista_stock): 
    """similar a la busqueda por código pero te muestra los producctos que es su nombre tengan coincidencias con la cadena ingresada

    Args:
        lista_stock (dicc): datos del stock almacenados en el diccionario
    """
    
    nombre=input("ingrese el nombre del producto a buscar: ")
    
    coincidencia = False
    
    for codigo, producto in lista_stock.items():
        
        if nombre in producto['producto']: #recorremos la lista y buscamos dentro de cada value producto["producto"] y vemos si hay coincidencia con el input
            
            if not coincidencia: #si concidencia es verdadero imprime una vez lo siguiente
                
                print ("+","-" * 85,"+")
                print ((f"{'producto':<20} | {'marca':<20} | {'cantidad':<20} | {'precio':<20}"))
                print ("+","-" * 85,"+")
                
                coincidencia= True
                
            print (f"{lista_stock[codigo]['producto']:<20} | {lista_stock[codigo]['marca']:<20} | {lista_stock[codigo]['cantidad']:<20} | {lista_stock[codigo]['precio']:<20}") #info del producto/os que coinciden con el string ingresado por teclado
            
            print ("+","-" * 85,"+")
            
    if not coincidencia :
        print(f"el nombre {nombre} no se encuentra en el stock") #si no hay coincidencia, lo mostramos como mjs
        
def modificar_producto(lista_stock):
    """_Pide un codigo y sí se encuentra dentro del stock te da la opcion de modificarlo_

    Args:
        lista_stock (Dic): Diccionario que contiene la info del stock
    """
    limpiar_pantalla()

    codigo=input("Ingrese el producto a modificar: ").lower()
    
    if codigo in lista_stock: #un if para verificar de que el código se encuentre dentro del stock (el código siempre es la llave del diccionario)
            
            print(f"producto : {lista_stock[codigo]['producto']}")
            #por cada value te voy a mostrar el valor previo
            producto = input("Ingrese el nombre del producto: ").lower()
            if producto == "" :
                producto = lista_stock[codigo]['producto']
            else:
                producto = producto
                
            print(f"marca : {lista_stock[codigo]['marca']}")
            #por cada value te voy a mostrar el valor previo
            marca = input("Ingrese la marca: ").lower() 
            if marca == "" :
                marca = lista_stock[codigo]['marca']
            else:
                marca = marca
            
            print(f"cantidad : {lista_stock[codigo]['cantidad']}")
            #por cada value te voy a mostrar el valor previo
            cantidad = obtener_entero("Ingrese la cantidad a ingresar el producto (unidades enteras): ","Las unidades se representan en números enteros")
            
            print(f"precio : {lista_stock[codigo]['precio']}")
            #por cada value te voy a mostrar el valor previo
            precio = obtener_flotante("Ingrese el precio unitario del producto: $","El precio debe ser representado en números.")
                
            importado_int = obtener_entero("El producto es de origen nacional? : (1-Sí o 2-No): ", "Opción Invalida (1-Sí o 2-No): ")
            while importado_int != 1 and importado_int != 2:
                importado_int = obtener_entero("El producto es de origen nacional? : (1-Sí o 2-No): ", "Opción Invalida (1-Sí o 2-No): ")  
            if(importado_int == 1):
                importado=True
            elif(importado_int == 2):
                importado=False
            
            #acá se actualizan los values del dic que contiene toda la info
            lista_stock[str(codigo)] = {'producto':producto,'marca': marca, 'cantidad':cantidad,'precio': precio ,'importado':importado}
    else:
        print(f"No se encuentra en la lista de stock el producto {codigo} ")
        #si no se encuentra en el stock lo muestra por pantalla
    guardar_stock(lista_stock) #siempre se llama a esta funcion para poder actualizar los datos
                   
def impresionGenral(lista_stock):
    for codigo, producto in lista_stock.items():
        print(f"{codigo} {producto}")
 
