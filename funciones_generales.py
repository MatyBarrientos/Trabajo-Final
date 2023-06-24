def obtenerEntero(mensaje_entrada,mensaje_error):
    while True:
        try:
            valor=int(input(mensaje_entrada))
        except:
            print(mensaje_error)
        else:
            return valor
        
def obtenerFlotante(mensaje_entrada,mensaje_error):
    while True:
        try:
            valor=float(input(mensaje_entrada))
        except:
            print(mensaje_error)
        else:
            return valor