from datetime import datetime
from models.Plaza import Plaza
import random
class Ticket():
    def __init__(self, matricula, plaza):
        self.matricula = matricula
        self.fecha = datetime.now()
        self.plaza = plaza
        self.pin = random.randrange(0, 1000000)
        
    def __str__(self):
       return f"""
       ***********************************************
       *                                             *
       *    MATRICULA: {self.matricula}              *
       *    FECHA: {self.fecha.strftime("%A %d de %B del %Y - %H:%M")}                      *
       *    PLAZA: {self.plaza.nombre}               *
       *    PIN:   {self.pin}                        *
       *                                             *
       ***********************************************
       """
   
    @property
    def get_matricula(self):
        return self.matricula
    
    @property
    def get_fecha(self):
        return self.fecha
    
    @property
    def get_plaza(self):
        return self.plaza
    
    @property
    def get_pin(self):
        return self.pin
    