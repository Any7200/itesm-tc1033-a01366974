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
                    obj2.write_flights(x)
                elif opc2 == 2:
                    #EN EL RESTO DE LAS OPCIONES ES PRACTICAMENTE LO MISMO
                    obj1 = CategoriesUI()
                    x = obj1.add_travellers()
                    obj2 = AirportAD()
                    obj2.write_travellers(x)
                elif opc2 == 3:
                    obj1 = CategoriesUI()
                    x = obj1.add_passengers()
                    obj2 = AirportAD()
                    obj2.write_passengers(x)
                else:
                    print("Opción inválida")
            elif opc == 2:
                print("1.De pilotos \n\r 2.De asistentes de vuelos \n\
                        \r  \n\r 3.De viajeros \n\r 4.De pasajeros \n\r 5.De vuelos \n\r")
                opc2 = input()
                if opc2 == 1:
                    #revisar
                    pass
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
                break
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
        print("- vuelo\n\r - pasaporte\n\r - clase\n\r - asiento\n\r - ubicación\n\r)
        print("EJEMPLO: \n\r\
                MA159,Me7348,premier,1A,check-in")
        x = (str(input()))
        lst_pasajeros = x.split(",")
        return lst_pasajeros
    def get_user_input(self):
        print("Introduce date in format YYMMDD")
        date = input()
        print("Introduce time in format HHMM")
        time = input()

        return date, time


