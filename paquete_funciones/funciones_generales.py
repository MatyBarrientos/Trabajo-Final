import os

def obtener_entero(mensaje_entrada,mensaje_error):
    """pide un valor entero y los argumentos a pasar son dos cadenas de texto

    Args:
        mensaje_entrada (str): mensaje para pedir datos en el input
        mensaje_error (str): mjs en caso de no ser correcto el ingreso

    Returns:
        int: el valor entero
    """
    while True:
        try:
            valor = int(input(mensaje_entrada))
        except ValueError:
            print(mensaje_error)
        else:
            return valor
        
def obtener_flotante(mensaje_entrada,mensaje_error):
    """pide un valor flotante y los argumentos a pasar son dos cadenas de texto

    Args:
        mensaje_entrada (str): mensaje para pedir datos en el float
        mensaje_error (str): mjs en caso de no ser correcto el ingreso

    Returns:
        float : el valor entero
    """
    while True:
        try:
            valor = float(input(mensaje_entrada))
        except ValueError:
            print(mensaje_error)
        else:
            return valor

def limpiar_pantalla():
    """limpieza de la terminal
    sirve para windows y linux
    """
    if os.name == 'posix':  # Para sistemas tipo Unix (Linux, macOS)
        os.system('clear')
    elif os.name == 'nt':  # Para sistemas Windows
        os.system('cls')