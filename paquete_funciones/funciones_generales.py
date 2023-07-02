import os

def obtener_entero(mensaje_entrada,mensaje_error):
    while True:
        try:
            valor = int(input(mensaje_entrada))
        except:
            print(mensaje_error)
        else:
            return valor
        
def obtener_flotante(mensaje_entrada,mensaje_error):
    while True:
        try:
            valor = float(input(mensaje_entrada))
        except:
            print(mensaje_error)
        else:
            return valor

def limpiar_pantalla():
    if os.name == 'posix':  # Para sistemas tipo Unix (Linux, macOS)
        os.system('clear')
    elif os.name == 'nt':  # Para sistemas Windows
        os.system('cls')