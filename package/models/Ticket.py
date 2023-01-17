from datetime import datetime
import random
class Ticket():
    def __init__(self, matricula, plaza):
        self.matricula = matricula
        self.fecha = datetime.now
        self.plaza = plaza
        self.pin = random.randrange(0, 1000000)
        
    def __str__(self):
       return f"Soy una galleta {self.matricula} y {self.plaza}."
   
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
    