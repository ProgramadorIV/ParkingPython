class Plaza ():

    def __init__(self, nombre, tipo_vehiculo, precio, estado):
        self.nombre = nombre
        self.precio = precio
        self.tipo_vehiculo = tipo_vehiculo
        self.estado = estado

    def __str__(self) :

        return f'Plaza: {self.nombre} para vehículos tipo {self.tipo_vehiculo} estado -> {self.estado.value}\n'

    @property
    def get_nombre_plaza(self):

        return self.nombre

