from models.Parking import Parking, restaurar_parking
import pickle


parking = restaurar_parking(60)
seleccion1 = 1
seleccion2 = 1

def menu():
    return int(input("""Elija alguna de las siguientes opciones:
    1. Zona pública
    2. Zona admin
    0. Salir
    -> """))

def zona_publica():
    return int(input("""
    Elija alguna de las siguientes opciones:
    1. Depositar vehículo
    2. Retirar vehículo
    3. Depositar abonados
    4. Retirar abonados
    0. Salir
    -> """))

def zona_privada():
    return int(input("""Elija alguna de las siguientes opciones:
    1. Estado del parking
    2. Facturación
    3. Consulta abonados
    4. Abonos
    5. Caducidad abonos
    0. Salir
    -> """))

while seleccion1 != 0:

    seleccion1 = menu()
    
    if seleccion1==1:
        
        while seleccion2!=0:
            
            seleccion2 = zona_publica()
            
            if seleccion2 == 1:

                parking.mostrar_plazas()
                
                #DEPOSITAR VEHICULO
                matricula = str(input('Introduzca su matrícula: '))
                tipo_vehiculo = int(input("""
                Introduzca su tipo de vehículo:
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

                    eleccion = int(input("""
                    ¿Desea efectuar el pago?
                    1. Sí
                    2. No
                    -> """))
                    if eleccion == 1:
                        parking.cobrar(pin)                    
                
            
            elif seleccion2 == 3:
                
                #DEPOSITAR ABONADOS
                matricula = str(input('Introduzca su matrícula: '))
                dni = str(input('Introduzca su dni: '))
                
                pass


            elif seleccion2 == 4:
                
                #RETIRAR ABONADOS
                pass
        
    elif seleccion1==2:
        
        while seleccion2!=0:
            
            seleccion2 = zona_privada()
            
            if seleccion2 == 1:
                
                #ESTADO DEL PARKING
                pass
                
            elif seleccion2 == 2:
                
                #FACTURACION
                pass
                
            elif seleccion2 == 3:
                
                #CONSULTA ABONADOS
                pass
                
            elif seleccion2 == 4:
                
                #ABONOS
                pass
                
            elif seleccion2 == 5:
                
                #CADUCIDAD ABONOS
                pass