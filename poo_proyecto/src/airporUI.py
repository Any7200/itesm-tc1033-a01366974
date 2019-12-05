from airportDP import *
class AirportUI:
    def user_decision_menu(self):
        while True:
            print("Bienvenido, ¿Qué desea hacer? \n\r 1.Agregar datos \n\r 2.Modificar datos \n\r 3.Reporte \n\r")
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
                    pass
                elif opc2 == 3:
                    pass
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
        return
    def add_passengers(self):
        #terminar
        return

    def get_user_input(self):
        print("Introduce date in format YYMMDD")
        date = input()
        print("Introduce time in format HHMM")
        time = input()

        return date, time


