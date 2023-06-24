from os import system

import json

def obtener_stock():
    try:
        filename='lista_stock.json'
        with open (filename,'r') as file:
            stock=json.load(file)      
    except FileNotFoundError:
        stock={}
    return stock


def guardar_stock(stock):
    filename= 'lista_stock.json'
    with open(filename,'w') as file:
        json.dump(stock,file, indent=2)
        

def ingreso_producto (lista_stock):
    system('cls')
        
    producto=input("Ingrese el nombre del producto: ").lower() 
    ###Ingreso de un nuevo item la idea la key 'producto' esté en minuscula para facilitar la busqueda.
    while True:
        try:
            cantidad=int(input("Ingrese la cantidad a ingresar el producto (unidades enteras): "))
            break
        except:
            print("Las unidades se representan en números enteros")
      
    while True:
        try:
            precio=float(input("Ingrese el precio unitario del producto: $"))
            break
        except:
                print("El precio debe ser representado en números.")
     
    lista_stock[producto]={"cantidad":cantidad,"precio":precio} 
    guardar_stock(lista_stock)
    

def busqueda_producto(lista_stock):
    system('cls')
    producto=input("Ingrese el nombre del producto: ").lower() #seguimos con las minusculas
    
    if producto in lista_stock: 
        ###un condicional para la busqueda, si esta se muestra los datos sino un mjs indicando que no esta.
         
        print(f"""El producto {producto} se encuentra en el inventario.
    Estas son las unidades disponibles: {lista_stock[producto]["cantidad"]}.
    Este es el precio unitario {lista_stock[producto]["precio"]}""")
            
    else:
        print(f"No se ha encontrado una entrada con la descripción {producto}")
        
        while True:
            try:
                opcion=int(input(f"Desea ingresar {producto} a la lista? (1='Si' o 2='No') : "))
            except:
                print("Elija entre (1='Si' o 2='No'): ")
            else:   
                if opcion == 1 :ingreso_producto(lista_stock)
                elif opcion== 2:print("Vuelta al menú...")
                else:print("Opción Invalida, vuelta al menú.") 
                break
        
        #Me gustaria agreagar un mjs y una funcion en el caso de que si no esta le pregunte al usuario si desea crear una nueva entrada

def modificar_producto(lista_stock):
    system('cls')
    producto=input("Ingrese el producto a modificar: ").lower()
    if producto in lista_stock: #me fijo si está el producto y en caso de ser afirmativo procedo a eliminar el par (key-value) y agregar el qu el usuario elija
            lista_stock.pop(producto)
            producto=input("Ingrese el nombre del producto: ").lower()
            cantidad=int(input("Ingrese la cantidad a ingresar el producto: "))
            precio=float(input("Ingrese el precio unitario del producto: "))
            lista_stock[producto]={"cantidad":cantidad,"precio":precio}
    else:
        print(f"No se encuentra en la lista de stock el producto {producto} ")
            
def listado_productos (lista_stock):
    system('cls')
    for nombre,producto in lista_stock.items():
        print (f"{nombre} - cantidad: {producto['cantidad']} - precio:{producto['precio']}.")
        
def exportar_archivo():
    system('cls')
    pass

def importar_archivo():
    system('cls')
    pass