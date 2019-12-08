from airportDP import *
class AirportUI:
    def user_decision_menu(self):
        while True:
            print("Bienvenido, ¿Qué desea hacer? \n\r 1.Agregar datos \n\r 2.Modificar datos \n\r 3.Reporte \n\r 4.-Salir")
            opc = int(input())
            if opc == 1:
                print("1.De vuelos \n\r 2.De viajeros \n\r 3.De pasajeros \n\r")
                opc2 = int(input())
                if opc2 == 1:
                    #casi listo, sólo falta que lo guarde en el archivo
                    obj1 = CategoriesUI()
                    x = obj1.add_data_flight()
                    obj2 = AirportAD()
                    y = obj2.read_flights()
                    obj2.write_flights(x, y)
                elif opc2 == 2:
                    #EN EL RESTO DE LAS OPCIONES ES PRACTICAMENTE LO MISMO
                    obj1 = CategoriesUI()
                    x = obj1.add_travellers()
                    obj2 = AirportAD()
                    y = obj2.read_travellers()
                    obj2.write_travellers(x, y)
                elif opc2 == 3:
                    obj1 = CategoriesUI()
                    x = obj1.add_passengers()
                    obj2 = AirportAD()
                    y = obj2.read_passengers()
                    obj2.write_passengers(x, y)
                else:
                    print("Opción inválida")
            elif opc == 2:
                print("1.De pilotos \n\r 2.De asistentes de vuelos\
                        \n\r 3.De viajeros \n\r 4.De pasajeros \n\r 5.De vuelos \n\r")
                opc2 = int(input())
                if opc2 == 1:
                    obj1 = CategoriesUI()
                    obj2 = Airport()
                    obj3 = AirportAD()
                    passport, x = obj1.change_pilots()
                    obj3.modify_pilots(passport, x, obj2.pilots)
                elif opc2 == 2:
                    pass
                elif opc2 == 3:
                    pass
                elif opc2 == 4:
                    pass
                elif opc2 == 5:
                    pass
                else:
                    print("Opción inválida")
            elif opc == 3:
                interaction = AirportUI()
                date, time = interaction.get_user_input()

                my_airport = Airport()
                my_airport.populate_airport()
                my_airport.generate_statistics(date, time)
            elif opc == 4:
                pass
                #Falta
            else:
                print("Opción inválida")

class CategoriesUI:   
    def add_data_flight(self):
        #REVISADO
        print("Ingrese los siguientes datos en una sola línea, separados por comas:\n\r")   
        print("- id\n\r - matrícula\n\r - origen\n\r - destino\n\r - llegada\n\r - salida\
                \n\r - estado\n\r - puerta de salida\n\r - pista de despegue\n\r - puerta de llegada\
                \n\r - pista de aterrizaje\n\r - piloto\n\r - copiloto\n\r - asistentes(separados con punto y coma)\n\r")
        print("EJEMPLO: \n\r\
                MA159,I359,Cancun - MEXICO,Ciudad de Mexico - MEXICO,180119_1757_America/Mexico_City,\n\
                180119_1957_America/Mexico_City,boarded,D1,3,C13,3,US5049,US5311,\n\
                ME1933;JA7918;ME9204;Me6629;US2945")
        x = (str(input()))
        lst_vuelos = x.split(",")
        return lst_vuelos
    def add_travellers(self):
        #terminar
        print("Ingrese los siguientes datos en una sola línea, separados por comas:\n\r")   
        print("- pasaporte\n\r - nombre \n\r - apellido\n\r - fecha de nacimiento\n\r - país\
                \n\r - género\n\r - estado civil\n\r")
        print("EJEMPLO: \n\r\
                ME4467,Elizabeth,Soto,590412,Mexico,NA,Single")
        x = (str(input()))
        lst_viajeros = x.split(",")
        return lst_viajeros
    def add_passengers(self):
        #terminar
        print("Ingrese los siguientes datos en una sola línea, separados por comas:\n\r")   
        print("- vuelo\n\r - pasaporte\n\r - clase\n\r - asiento\n\r - ubicación\n\r")
        print("EJEMPLO: \n\r\
                MA159,Me7348,premier,1A,check-in")
        x = (str(input()))
        lst_pasajeros = x.split(",")
        return lst_pasajeros
    def change_pilots(self):
        print("Ingrese el pasaporte del piloto")
        passport_pilot = str(input())
        print("Elija el estado civil al que desee cambiarlo:\n\r 1.Single (soltero)\
                \n\r 2.Married (casado)\n\r 3.Divorced (divorciado)\
                \n\r 4.Widowed (viudo)")
        new_marital_status = int(input())
        return passport_pilot, new_marital_status
    def change_attendants(self):
        print("Ingrese el pasaporte del asistente de vuelo")
        passport_attendant = str(input())
        print("Elija el estado civil al que desee cambiarlo:\n\r 1.Single (soltero)\
                \n\r 2.Married (casado)\n\r 3.Divorced (divorciado)\
                \n\r 4.Widowed (viudo)")
        new_marital_status = int(input())
        return passport_attendant, new_marital_status
    def change_travellers(self):
        print("Ingrese el pasaporte del viajero")
        passport_travellers = str(input())
        print("¿Qué desea modificar?\n\r 1.Estado Civil\n\r 2.Género\
                \n\r 3.Fecha de Nacimiento\n\r 4.Nombre y Apellido")
        decision = int(input())
        if decision == 1:
            print("Elija el estado civil al que desee cambiarlo:\n\r 1.Single (soltero)\
                \n\r 2.Married (casado)\n\r 3.Divorced (divorciado)\
                \n\r 4.Widowed (viudo)")
            x = int(input())
        elif decision == 2:
            print("Elija el género al que desee cambiarlo:\
                    \n\r 1.Masculino\n\r 2.Femenino")
            x = int(input())
        elif decision == 3:
            print("Escriba la nueva fecha de nacimiento en el formato YYMMDD")
            x = input()
        elif decision == 4:
            print("Escriba el nombre del viajero al que desee cambiarlo")
            y1 = str(input())
            print("Escriba el apellido del viajero al que desee cambiarlo")
            y2 = str(input())
            x = [y1,y2]
        else:
            print("Opción inválida")  
        return passport_travellers, x  
    def get_user_input(self):
        print("Introduce date in format YYMMDD")
        date = input()
        print("Introduce time in format HHMM")
        time = input()

        return date, time


