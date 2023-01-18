from models.Parking import Parking

parking = Parking(60)
seleccion1 = 1
seleccion2 = 1

def menu():
    return int(input('Elija alguna de las siguientes opciones:\n1. Zona pública \n2. Zona admin'))

def zona_publica():
    return int(input('Elija alguna de las siguientes opciones: \n1. Depositar vehículo \n2. Retirar vehículo \n3. Depositar abonados \n4. Retirar abonados'))

def zona_privada():
    return int(input('Elija alguna de las siguientes opciones: \n1. Estado del parking \n2. Facturación \n3. Consulta abonados \n4. Abonos \n5. Caducidad abonos'))

while seleccion1 != 0:

    seleccion1 = menu()
    
    if seleccion1==1:
        
        while seleccion2!=0:
            
            seleccion2 = zona_publica()
            
            if seleccion2 == 1:
                
                #DEPOSITAR VEHICULO
                matricula = str(input('Introduzca su matrícula: '))
                tipo_vehiculo = int(input('Introduzca su tipo de vehículo: \n1. Turismo \n2. Motocicleta \n3. Movilidad reducida'))
                
                if()
                
                
            elif seleccion2 == 2:
                
                #RETIRAR VEHICULO
                
            elif seleccion2 == 3:
                
                #DEPOSITAR ABONADOS
                
            elif seleccion2 == 4:
                
                #RETIRAR ABONADOS
        
    elif seleccion1==2:
        
        while seleccion2!=0:
            
            seleccion2 = zona_privada()
            
            if seleccion2 == 1:
                
                #ESTADO DEL PARKING
                
            elif seleccion2 == 2:
                
                #FACTURACION
                
            elif seleccion2 == 3:
                
                #CONSULTA ABONADOS
                
            elif seleccion2 == 4:
                
                #ABONOS
                
            elif seleccion2 == 5:
                
                #CADUCIDAD ABONOS