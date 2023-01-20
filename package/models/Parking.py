from models.Plaza import Plaza
from models.Ticket import Ticket
from models.Cobro import Cobro
from datetime import datetime
import pickle

class Parking():

    def __init__(self, numero_plazas):
        self.plazas_ocupadas = {'turismo': [],'motocicleta': [],'movilidad_reducida': [],}
        self.plazas_libres = {
        'turismo': [Plaza(f'A-{i+1}', 'turismo', 0.12) for i in range (0 ,int(numero_plazas*0.7))],
        'motocicleta': [Plaza(f'B-{i+1}', 'motocicleta', 0.08) for i in range (0, int(numero_plazas*0.15))],
        'movilidad_reducida': [Plaza(f'C-{i+1}', 'movilidad_reducida', 0.10) for i in range (0, int(numero_plazas*0.15))],}
        self.tickets = {}
        self.cobros = []
        self.abonos = {}
        pass

    def mostrar_plazas(self):

        for plazas in self.plazas_libres.values():
            for plaza in plazas:
                print(plaza)

    def mostrar_plazas_ocupadas(self):
        for plazas in self.plazas_ocupadas.values():
            for plaza in plazas:
                print(plaza)

    def aparcar(self, matricula, tipo_vehiculo):

        if len(self.plazas_libres[tipo_vehiculo]) == 0:
            return None

        plaza = self.plazas_libres[tipo_vehiculo].pop()
        self.plazas_ocupadas[tipo_vehiculo].append(plaza)

        ticket = Ticket(matricula, plaza)
        self.tickets[ticket.pin] = ticket

        fichero = open('parking.pckl', 'wb')
        pickle.dump(self, fichero)
        fichero.close()

        return ticket

    def buscar_vehiculo(self, matricula, plaza, pin):
        
        if pin in self.tickets:
            ticket = self.tickets[pin]
            if matricula == ticket.matricula and ticket.plaza.nombre == plaza:
                print(f'El coste de la estancia es de {(divmod((datetime.now() - ticket.fecha ).total_seconds(), 60)[0])*ticket.plaza.precio}')
                return True 

            else:
                print('Introduzca la matrícula y la plaza correctamente.')
                return False
        else:
            print('Introduzca el pin indicado en el ticket correctamente.')
            return False

    def cobrar(self, pin):

        ticket = self.tickets[pin]
        tipo = ticket.plaza.tipo_vehiculo

        plaza = self.plazas_ocupadas[tipo].pop(self.plazas_ocupadas[tipo].index(ticket.plaza))
        self.plazas_libres[tipo].append(plaza)

        self.cobros.append(Cobro((divmod((datetime.now() - ticket.fecha ).total_seconds(), 60)[0])*ticket.plaza.precio))

        fichero = open('parking.pckl', 'wb')
        pickle.dump(self, fichero)
        fichero.close()

    def aparcar_abonado():
        pass


def restaurar_parking(numero_plazas):

    try:
        fichero = open('parking.pckl', 'rb')
    except FileNotFoundError:
        return Parking(numero_plazas)
    
    parking = pickle.load(fichero)
    fichero.close()

    return parking