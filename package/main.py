from models.Parking import Parking, restaurar_parking
from models.Abonado import Abonado
from models.auxiliares.EstadoPlaza import EstadoPlaza
from models.auxiliares.TipoAbono import TipoAbono
from datetime import datetime
import pickle


parking = restaurar_parking(60)
seleccion1 = 1
seleccion2 = 1


abonado = Abonado('20491523D', 'Antonio', 'Jiménez Infante', '2336HPS', parking.plazas['turismo'][0], 
    '23421454235376', TipoAbono.MENSUAL, 'email'
)
parking.plazas['turismo'][0].estado = EstadoPlaza.ABONOLIBRE
parking.abonados[abonado.pin] = abonado

print(parking.abonados)
fichero = open('parking.pckl', 'wb')
pickle.dump(parking, fichero)
fichero.close()

def menu():
    return int(input("""\nElija alguna de las siguientes opciones:
    1. Zona pública
    2. Zona admin
    0. Salir
    -> """))

def zona_publica():
    return int(input("""\nElija alguna de las siguientes opciones:
    1. Depositar vehículo
    2. Retirar vehículo
    3. Depositar abonados
    4. Retirar abonados
    0. Salir
    -> """))

def zona_privada():
    return int(input("""\nElija alguna de las siguientes opciones:
    1. Estado del parking
    2. Facturación
    3. Consulta abonados
    4. Abonos
    5. Caducidad abonos
    0. Salir
    -> """))

def zona_abonos():
    return int(input("""\nElija alguna de las siguientes opciones:
    1. Dar de alta un abono
    2. Modificar su abono
    3. Dar de baja su abono
    0. Salir
    -> """))

while True:

    seleccion1 = menu()
    
    if seleccion1==1:
        
        while True:
            
            seleccion2 = zona_publica()
            
            if seleccion2 == 1:

                parking.mostrar_plazas()
                
                #DEPOSITAR VEHICULO
                matricula = str(input('Introduzca su matrícula: '))
                tipo_vehiculo = int(input("""Introduzca su tipo de vehículo:
                1. Turismo
                2. Motocicleta
                3. Movilidad reducida
                0. Salir
                -> """))

                if tipo_vehiculo == 1:
                    tipo_vehiculo = 'turismo'

                elif tipo_vehiculo == 2:
                    tipo_vehiculo = 'motocicleta'

                else:
                    tipo_vehiculo = 'movilidad_reducida'
                
                ticket = parking.aparcar(matricula, tipo_vehiculo)

                if ticket == None:
                    print('No hay plazas libres')
                
                else:
                    print(ticket)

                
            elif seleccion2 == 2:
                
                #RETIRAR VEHICULO
                matricula = str(input('Introduzca su matrícula: '))
                plaza = str(input('Introduzca la plaza en la que está estacionado su vehículo: '))
                pin = int(input('Introduzca el pin de su ticket: '))

                if parking.buscar_vehiculo(matricula, plaza, pin):

                    eleccion = int(input("""¿Desea efectuar el pago?
                    1. Sí
                    2. No
                    -> """))
                    if eleccion == 1:
                        parking.cobrar(pin)                    
                
            
            elif seleccion2 == 3:
                
                #DEPOSITAR ABONADOS
                matricula = str(input('Introduzca su matrícula: '))
                dni = str(input('Introduzca su dni: '))
                
                abonado = parking.aparcar_abonado(matricula, dni)

                if abonado != None:
                    print(abonado.mostrar_ticket_abonado())
                else:
                    print('Introduzca correctamente los datos por favor')


            elif seleccion2 == 4:
                
                #RETIRAR ABONADOS
                matricula = str(input('Introduzca su matrícula: '))
                plaza = str(input('Introduzca la plaza en la que está estacionado su vehículo: '))
                pin = int(input('Introduzca el pin de su ticket: '))

                parking.retirar_abonado(matricula,plaza,pin)

            elif seleccion2 == 0:
                break
        
    elif seleccion1==2:

        while True:

            seleccion2 = zona_privada()

            if seleccion2 == 1:
                
                #ESTADO DEL PARKING
                parking.estado_plazas()
                
            elif seleccion2 == 2:
                
                #FACTURACION
                print('\nFecha inicio:\n')
                fecha_inicio = datetime(
                    int(input('Introduzca el año: ')),
                    int(input('Introduzca el mes: ')),
                    int(input('Introduzca el día: ')),
                    int(input('Introduzca la hora: ')),
                    int(input('Introduzca los minutos: '))
                    )
                
                print('\nFecha fin:\n')
                fecha_fin = datetime(
                    int(input('Introduzca el año: ')),
                    int(input('Introduzca el mes: ')),
                    int(input('Introduzca el día: ')),
                    int(input('Introduzca la hora: ')),
                    int(input('Introduzca los minutos: '))
                    )

                cobros = parking.facturacion(fecha_inicio, fecha_fin)

                for cobro in cobros:
                    print(f'Coste: {cobro.coste} fecha: {cobro.fecha.strftime("%A %d de %B del %Y - %H:%M")}')
                
            elif seleccion2 == 3:
                
                #CONSULTA ABONADOS                
                pass
                
            elif seleccion2 == 4:
                
                #ABONOS
                while True:
                    eleccion = zona_abonos()

                    if eleccion == 1:

                        dni = str(input('Introduzca su dni: '))
                        nombre = str(input('Introduzca su nombre: '))
                        apellidos = str(input('Introduzca su apellido: '))
                        matricula = str(input('Introduzca su matrícula: '))
                        tarjeta = str(input('Introduzca su tarjeta bancaria: '))
                        email = str(input('Introduzca un email: '))

                        tipo_abono = int(input("""Elija el abono deseado:
                        1. Mensual
                        2. Trimestral
                        3. Semestral
                        4. Anual
                        -> """))

                        if tipo_abono == 1:
                            tipo_abono = TipoAbono.MENSUAL
                        elif tipo_abono == 2:
                            tipo_abono = TipoAbono.TRIMESTRAL
                        elif tipo_abono == 3:
                            tipo_abono = TipoAbono.SEMESTRAL
                        elif tipo_abono == 4:
                            tipo_abono = TipoAbono.ANUAL

                        tipo_vehiculo = int(input("""Introduzca su tipo de vehículo:
                        1. Turismo
                        2. Motocicleta
                        3. Movilidad reducida
                        0. Salir
                        -> """))

                        if tipo_vehiculo == 1:
                            tipo_vehiculo = 'turismo'

                        elif tipo_vehiculo == 2:
                            tipo_vehiculo = 'motocicleta'

                        else:
                            tipo_vehiculo = 'movilidad_reducida'

                        abonado = parking.alta_abono(dni, nombre, apellidos, matricula, tarjeta, tipo_abono, email, tipo_vehiculo)

                        if abonado == None:
                            print('Lo sentimos no hay plazas disponibles para su vehículo')
                        else:
                            print(f'Muchas gracias, su abono dura hasta el: {abonado.fecha_baja.strftime("%A %d de %B del %Y - %H:%M")}')

                    elif eleccion == 2:
                        pass

                    elif eleccion == 3:
                        pass

                    elif eleccion == 0:
                        break

                
            elif seleccion2 == 5:
                
                #CADUCIDAD ABONOS
                pass

            elif seleccion2 == 0:
                break

    elif seleccion1==0:
        print('\nAdiós')
        break