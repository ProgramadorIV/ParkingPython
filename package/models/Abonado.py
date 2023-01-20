import random

class Abonado ():
    def __init__(self, dni, nombre, apellidos, tarjeta, tipo_abono, email):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.tarjeta = tarjeta
        self.tipo_abono = tipo_abono
        self.email = email
        self.pin = random.randrange(0, 1000000)

    def mostrar_abono():
        print("""
        
        """)