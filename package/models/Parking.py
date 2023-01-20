from models.Plaza import Plaza
from models.Ticket import Ticket
from models.Abonado import Abonado
from models.Cobro import Cobro
from models.auxiliares.EstadoPlaza import EstadoPlaza
from datetime import datetime
import pickle

class Parking():

    def __init__(self, numero_plazas):
        self.plazas = {
        'turismo': [Plaza(f'A-{i+1}', 'turismo', 0.12, EstadoPlaza.LIBRE) for i in range (0 ,int(numero_plazas*0.7))],
        'motocicleta': [Plaza(f'B-{i+1}', 'motocicleta', 0.08, EstadoPlaza.LIBRE) for i in range (0, int(numero_plazas*0.15))],
        'movilidad_reducida': [Plaza(f'C-{i+1}', 'movilidad_reducida', 0.10, EstadoPlaza.LIBRE) for i in range (0, int(numero_plazas*0.15))],}
        self.tickets = {} #pin: Ticket
        self.cobros = []
        self.abonados = {} #pin: Abonado
        pass

    def save(self):
        fichero = open('parking.pckl', 'wb')
        pickle.dump(self, fichero)
        fichero.close()

    def mostrar_plazas(self):

        for plazas in self.plazas.values():
            for plaza in plazas:
                print(plaza)

    def aparcar(self, matricula, tipo_vehiculo):

        if len(self.plazas[tipo_vehiculo]) == 0:
            return None

        plaza = self.plazas[tipo_vehiculo][0]
        plaza.estado = EstadoPlaza.OCUPADA        

        ticket = Ticket(matricula, plaza)
        self.tickets[ticket.pin] = ticket

        self.save()

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

        plaza = self.plazas[tipo][self.plazas[tipo].index(ticket.plaza)]
        plaza.estado = EstadoPlaza.LIBRE

        self.cobros.append(Cobro((divmod((datetime.now() - ticket.fecha ).total_seconds(), 60)[0])*ticket.plaza.precio))

        self.save()

    def aparcar_abonado(self, matricula, dni):

        for abonado in self.abonados.values():
            if abonado.matricula == matricula and abonado.dni == dni:
                abonado.plaza.estado = EstadoPlaza.ABONOOCUPADA
                self.save()

                return abonado
        return None

    def retirar_abonado(self, matricula, plaza, pin):
        
        if pin in self.abonados:
            abonado = self.abonados[pin]
            if matricula == abonado.matricula and plaza == abonado.plaza.nombre:
                
                abonado.plaza.estado = EstadoPlaza.ABONOLIBRE
                self.save()

                print('\nBuen viaje')
            else:
                print('\nIntroduzca la matrícula y el identificador de la plaza correctamente.')
        else:
            print('Introduzca el pin indicado en su ticket correctamente')

    def estado_plazas(self):

        for plazas in self.plazas.values():
            for plaza in plazas:
                print(f'Plaza: {plaza.nombre} Estado -> {plaza.estado.value}')

    def facturacion(self, fecha_inicio, fecha_fin):

        cobros = []
        for cobro in self.cobros:
            if cobro.fecha > fecha_inicio and cobro.fecha < fecha_fin:
                cobros.append(cobro)
        
        return cobros

    def alta_abono(self, dni, nombre, apellidos, matricula, tarjeta, tipo_abono, email, tipo_vehiculo):

        plazas_abonables = [plaza for plaza in self.plazas[tipo_vehiculo] if plaza.estado == EstadoPlaza.LIBRE or plaza.estado == EstadoPlaza.OCUPADA]
        if len(plazas_abonables) > 0:
            abonado = Abonado(dni, nombre, apellidos, matricula, plazas_abonables[0], tarjeta, tipo_abono, email)

            self.abonados[abonado.pin] = abonado
            abonado.plaza.estado.ABONOLIBRE

            self.save()
            return abonado

        return None



def restaurar_parking(numero_plazas):

    try:
        fichero = open('parking.pckl', 'rb')
    except FileNotFoundError:
        return Parking(numero_plazas)
    
    parking = pickle.load(fichero)
    fichero.close()

    return parking