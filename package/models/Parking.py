class Parking():
    
    def __init__(self, numero_plazas):
        self.plazas_turismo = numero_plazas*0.7
        self.plazas_motocicletas = numero_plazas*0.15
        self.plazas_movilidad_reducida = numero_plazas*0.15
        pass
    
    def asignar_plaza(tipo_vehiculo):
        