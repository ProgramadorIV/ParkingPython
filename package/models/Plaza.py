class Plaza ():

    matricula = None
    precio = None

    def __init__(self, nombre, tipo_vehiculo, precio):
        self.nombre = nombre
        self.precio = precio
        self.tipo_vehiculo = tipo_vehiculo

    def __str__(self) :

        return f'Plaza: {self.nombre} para vehículos tipo {self.tipo_vehiculo} \n'

    @property
    def get_nombre_plaza(self):

        return self.nombre
        

    def aparcar_vehiculo(self, matricula):
        self.matricula = matricula
        self.ocupada = True

