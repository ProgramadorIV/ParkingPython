from datetime import datetime, timedelta
import random

class Abonado ():

    def __init__(self, dni, nombre, apellidos, matricula, plaza, tarjeta, tipo_abono, email):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.matricula = matricula
        self.plaza = plaza
        self.tarjeta = tarjeta
        self.tipo_abono = tipo_abono
        self.fecha_alta = datetime.now()
        self.fecha_baja = self.fecha_alta + timedelta(days=tipo_abono.value)
        self.email = email
        self.pin = random.randrange(0, 1000000)

    def mostrar_ticket_abonado(self):
        return f"""
       ***********************************************
       *          NOMBRE: {self.nombre}              *
       *                                             *
       *    MATRICULA: {self.matricula}              *
       *    PLAZA: {self.plaza.nombre}               *
       *    PIN:   {self.pin}                        *
       *                                             *
       ***********************************************
       """