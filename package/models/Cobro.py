from datetime import datetime
class Cobro():

    def __init__(self, coste):
        self.coste = coste
        self.fecha = datetime.now()