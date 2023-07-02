from funciones_generales import obtener_entero, obtener_flotante, limpiar_pantalla
from tabulate import tabulate
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
        

def ingreso_producto (lista_stock):
    """Ingreso de un nuevo artículo en el stock y al final se actualiza el arvicho Json.

    Args:
        lista_stock {dic}: Diccionario que contiene el stock
    """
    
    limpiar_pantalla()
     
    codigo =str( obtener_entero("Ingrese el código del producto: ", "el código debe ser representado en un número entero."))
    
    producto = input("Ingrese el nombre del producto: ").lower() 
    
    marca = input("Ingrese la marca: ").lower() 

    cantidad = obtener_entero("Ingrese la cantidad a ingresar el producto (unidades enteras): ","Las unidades se representan en números enteros")
    
    precio = obtener_flotante("Ingrese el precio unitario del producto: $","El precio debe ser representado en números.")
    
    
    importado_int = obtener_entero("El producto es de origen nacional? : (1-Sí o 2-No): ", "Opción Invalida (1-Sí o 2-No): ")
    while importado_int != 1 and importado_int != 2:
        importado_int = obtener_entero("El producto es de origen nacional? : (1-Sí o 2-No): ", "Opción Invalida (1-Sí o 2-No): ")  
    if(importado_int == 1):
            importado=True
    elif(importado_int == 2):
            importado=False
     
    lista_stock[codigo] = {'producto':producto,'marca': marca, 'cantidad':cantidad,'precio': precio ,'importado':importado}
    
    guardar_stock(lista_stock)
    

def busqueda_producto(lista_stock):
    
    limpiar_pantalla()
    
    codigo = str(obtener_entero("Ingrese el nombre del producto: ", "Opción Invalida, debe ser un número entero: "))
    
    if codigo in lista_stock: 
         
        print(f"El código {codigo} se encuentra en el inventario.")
        print ((f"{'producto':<15} | {'marca':<15} | {'cantidad':<15} | {'precio':<15}"))
        print ("-" * 65)
        print (f"{lista_stock[codigo]['producto']:<15} | {lista_stock[codigo]['marca']:<15} | {lista_stock[codigo]['cantidad']:<15} | {lista_stock[codigo]['precio']:<15}")
        print ("-" * 65)
            
    else:
        print(f"No se ha encontrado una entrada con la descripción {codigo}")
        
        opcion = obtener_entero(f"Desea ingresar {codigo} a la lista? (1='Si' o 2='No') : ","Opción Invalida, debe ser un número entero (1='Si' o 2='No')")
        while opcion != 1 and opcion != 2: 
            opcion = obtener_entero(f"Desea ingresar {codigo} a la lista? (1='Si' o 2='No') : ","Opción Invalida, debe ser un número entero (1='Si' o 2='No')")
        if opcion == 1 :
                ingreso_producto(lista_stock)
        else:
                print("Vuelta al menú...")
        

def modificar_producto(lista_stock):
    
    limpiar_pantalla()

    codigo=input("Ingrese el producto a modificar: ").lower()
    
    if codigo in lista_stock:
            
            print(f"producto : {lista_stock[codigo]['producto']}")
            
            producto = input("Ingrese el nombre del producto: ").lower()
            if producto == "" :
                producto = lista_stock[codigo]['producto']
            else:
                producto = producto
                
            print(f"marca : {lista_stock[codigo]['marca']}")
            
            marca = input("Ingrese la marca: ").lower() 
            if marca == "" :
                marca = lista_stock[codigo]['marca']
            else:
                marca = marca
            
            print(f"cantidad : {lista_stock[codigo]['cantidad']}")
            
            cantidad = obtener_entero("Ingrese la cantidad a ingresar el producto (unidades enteras): ","Las unidades se representan en números enteros")
            
            print(f"precio : {lista_stock[codigo]['precio']}")
            
            precio = obtener_flotante("Ingrese el precio unitario del producto: $","El precio debe ser representado en números.")
                
            importado_int = obtener_entero("El producto es de origen nacional? : (1-Sí o 2-No): ", "Opción Invalida (1-Sí o 2-No): ")
            while importado_int != 1 and importado_int != 2:
                importado_int = obtener_entero("El producto es de origen nacional? : (1-Sí o 2-No): ", "Opción Invalida (1-Sí o 2-No): ")  
            if(importado_int == 1):
                importado=True
            elif(importado_int == 2):
                importado=False
            
            
            lista_stock[str(codigo)] = {'producto':producto,'marca': marca, 'cantidad':cantidad,'precio': precio ,'importado':importado}
    else:
        print(f"No se encuentra en la lista de stock el producto {codigo} ")
        
    guardar_stock(lista_stock)
            
def listado_productos (lista_stock):
    
    limpiar_pantalla()
    
    if lista_stock:
        
        encabezados = ['id','producto','marca', 'cantidad','precio','importado']
        
        filas = [[codigo, datos["producto"], datos["marca"], datos["cantidad"],datos["precio"],datos["importado"]] for codigo, datos in lista_stock.items()]

        tabla = tabulate(filas, headers=encabezados, tablefmt='grid')
        
        print(tabla)
    else:
        print("No hay entradas en la lista.")
        
def impresionGenral(lista_stock):
    for codigo, producto in lista_stock.items():
        print(f"{codigo} {producto}")


def busqueda_nombre(lista_stock):
    
    nombre=input("ingrese el nombre del producto a buscar: ")
    
    coincidencia = False
    
    for codigo, producto in lista_stock.items():
        
        if nombre in producto['producto']:
            
            if not coincidencia:
                
                print ("+","-" * 85,"+")
                print ((f"{'producto':<20} | {'marca':<20} | {'cantidad':<20} | {'precio':<20}"))
                print ("+","-" * 85,"+")
                
                coincidencia= True
                
            print (f"{lista_stock[codigo]['producto']:<20} | {lista_stock[codigo]['marca']:<20} | {lista_stock[codigo]['cantidad']:<20} | {lista_stock[codigo]['precio']:<20}")
            
            print ("+","-" * 85,"+")
            
    if not coincidencia :
        print(f"el nombre {nombre} no se encuentra en el stock")
    
def borrar_producto_id(lista_stock):
    
    codigo = str(obtener_entero("Ingrese el código del producto: ", "el código debe ser representado en un número entero."))
    
    if codigo in lista_stock:
        
        del lista_stock[codigo]
        print(f"entrada {codigo} borrada")
        
    else:
        print(f"la entrada {codigo} no se encuentra en el stock")
    guardar_stock(lista_stock)