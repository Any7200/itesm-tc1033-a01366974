# -*- coding: utf-8 -*-
class Report:
    def __init__(self, _date, _time, _no_empty_tracks, _no_occupied_tracks,
                 _no_passengers_check_in, _no_passengers_security, _no_passengers_boarded, _no_flights_landed, 
                 _no_flights_in_transit , _no_empty_gates, _no_occupied_gates):
        self.date = _date
        self.time = _time
        self.no_empty_tracks = _no_empty_tracks
        self.no_occupied_tracks = _no_occupied_tracks
        self.no_passengers_check_in = _no_passengers_check_in
        self.no_passengers_security = _no_passengers_security
        self.no_passengers_boarded = _no_passengers_boarded
        self.no_flights_landed = _no_flights_landed
        self.no_flights_in_transit = _no_flights_in_transit
        self.no_empty_gates = _no_empty_gates
        self.no_occupied_gates = _no_occupied_gates

    def write_file(self):
        statistics_file = open("data/statistics.csv", "w+")
        statistics_file.write("date,time,# of empty tracks,# of occupied tracks, # of passengers in check-in, # of passenger in security, # of passengers boarded , # of flights landed, # of flights departured, # of empty gates,# of occupied gates\n")
        statistics_file.write(self.date+",")
        statistics_file.write(self.time+",")
        statistics_file.write(str(self.no_empty_tracks)+",")
        statistics_file.write(str(self.no_occupied_tracks)+",")
        statistics_file.write(str(self.no_passengers_check_in)+",")
        statistics_file.write(str(self.no_passengers_security)+",")
        statistics_file.write(str(self.no_passengers_boarded)+",")
        statistics_file.write(str(self.no_flights_landed)+",")
        statistics_file.write(str(self.no_flights_in_transit)+",")
        statistics_file.write(str(self.no_empty_gates)+",")
        statistics_file.write(str(self.no_occupied_gates)+",")


class Airport:
    def __init__(self):
        self.tracks = None
        self.passengers = None
        self.pilots = None
        self.attendants = None
        self.travellers = None
        self.flights = None
        self.planes = None

    def populate_airport(self):
        data_loader = AirportAD()
        self.pilots = data_loader.read_pilots()
        self.flights = data_loader.read_flights()
        self.attendants = data_loader.read_attendants()
        self.passengers = data_loader.read_passengers()
        self.travellers = data_loader.read_travellers()
        self.planes = data_loader.read_planes()

    def update_file_attendants(self):
        archivo = open("data/attendants.csv","w+")
        archivo.write("passport,forename,surname,date of birth,country,gender,marital status")
        for i in self.attendants.values():
            archivo.write()
            archivo.write(",")
            if i.marital_status == True:
                archivo.write("\n")
        archivo.close()
    
    def update_file_flights(self):
        archivo = open("data/flights.csv","w+")
        archivo.write("id,plate,origin,destiny,departure,arriving,status,departure gate,take off track,arriving gate,landing track,pilot,copilot, attendants")
        for i in self.flights.values():
            archivo.write(i)
            archivo.write(",")
            if i.attendants == True:
                archivo.write("\n")
        archivo.close()
    
    def update_file_passengers(self):
        archivo = open("data/passengers.csv","w+")
        archivo.write("id,plate,origin,destiny,departure,arriving,status,departure gate,take off track,arriving gate,landing track,pilot,copilot, attendants")
        for i in self.passengers.values():
            archivo.write(i)
            archivo.write(",")
            if i.location == True:
                archivo.write("\n")
        archivo.close()
    
    def update_file_pilots(self):
        archivo = open("data/pilots.csv","w+")
        archivo.write("passport,forename,surname,date of birth, country, gender, marital status")
        for i in self.pilots.values():
            archivo.write(i)
            archivo.write(",")
            if i.marital_status == True:
                archivo.write("\n")
        archivo.close()
    
    def update_file_travellers(self):
        archivo = open("data/travellers.csv","w+")
        archivo.write("passport,forename,surname,date of birth, country, gender, marital status")
        for i in self.travellers.values():
            archivo.write(i)
            archivo.write(",")
            if i.marital_status == True:
                archivo.write("\n")
        archivo.close()

    def generate_statistics(self, _date, _time):
        
        number_empty_tracks = 0
        number_of_occupied_tracks = 0
        number_of_empty_gates = 0
        number_of_occupied_gates = 0
        number_of_passengers_check_in = 0
        number_of_passengers_security = 0
        number_of_passengers_boarded = 0
        number_of_flights_landed = 0
        number_of_flights_in_transit = 0


        for flight in self.flights.values():
            # origin
            if flight.origin == "Ciudad de Mexico - MEXICO":
                date = flight.departure.split("_")[0]
                time = flight.departure.split("_")[1]
            else:
                date = flight.arriving.split("_")[0]
                time = flight.arriving.split("_")[1]

            if date == _date and int(time) == int(_time):
                # counting tracks
                if flight.status in ["boarded", "landing"]:
                    number_of_occupied_tracks += 1
                else:
                    number_empty_tracks += 1

                # counting gates
                if flight.status in ["boarded", "landing", "in transit"]:
                    number_of_empty_gates += 1
                else:
                    number_of_occupied_gates += 1
         
        for passenger in self.passengers.values():
            #location
            if passenger.location == "check-in":
                    number_of_passengers_check_in += 1

            elif passenger.location == "security":
                    number_of_passengers_security += 1
            
            elif passenger.location == "boarded":
                    number_of_passengers_boarded +=  1
            else:
                print("INVALID") 
        
        for flight in self.flights.values():
            if flight.status == "landed":
                number_of_flights_landed += 1

            elif flight.status == "in transit":
                number_of_flights_in_transit +=1
            
            else:
                print("INVALID")

                
        report = Report(_date, _time, number_empty_tracks,
                        number_of_occupied_tracks, number_of_passengers_check_in, number_of_passengers_security, 
                        number_of_passengers_boarded, number_of_flights_landed, number_of_flights_in_transit, 
                        number_of_empty_gates, number_of_occupied_gates)

        report.write_file()
        print("Reporte generado")

class Planes:
    def __init__(self, _plate, _manufacturer, _model, _pcapacity, _lcapacity, _maxspeed):
        self.plate = _plate
        self.manufacturer = _manufacturer
        self.model = _model
        self.pcapacity = _pcapacity
        self.lcapacity = _lcapacity
        self.maxspeed = _maxspeed

class Flight:
    def __init__(self, _id, _plate, _origin, _destiny,
                 _departure, _arriving, _status, _departure_gate,
                 _take_off_track, _arriving_gate, _landing_track,
                 _pilot, _copilot, _attendants):

        self.id = _id
        self.plate = _plate
        self.origin = _origin
        self.destiny = _destiny
        self.departure = _departure
        self.arriving = _arriving
        self.status = _status
        self.departure_gate = _departure_gate
        self.take_off_track = _take_off_track
        self.arriving_gate = _arriving
        self.landing_track = _landing_track
        self.pilot = _pilot
        self.copilot = _copilot
        self.attendants = _attendants

class Passengers:
    def __init__(self, _flight, _passport, _classes, _seat, _location):
        self.flight = _flight
        self.passport = _passport
        self.classes = _classes
        self.seat = _seat
        self.location = _location

class Crew:
    def __init__(self, _passport, _forename, _surname, _date_of_birth,
                 _country, _gender, _marital_status):
        self.passport = _passport
        self.forename = _forename
        self.surname = _surname
        self.date_of_birth = _date_of_birth
        self.country = _country
        self.gender = _gender
        self.marital_status = _marital_status
class Traveller(Crew):
    pass

class Attendant(Crew):
    pass


class Pilot(Crew):
    pass


class AirportAD:

    def read_attendants(self):
        attendants_file = open("data/attendants.csv", "r", encoding="utf-8")
        lines = attendants_file.readlines()
        attendants_file.close()
        lines.pop(0)

        attendants = {}

        for l in lines:
            fields = l.split(",")
            passport = fields[0]
            attendant = Attendant(passport, fields[1], fields[2],
                                  fields[3], fields[4], fields[5], fields[6])
            attendants[passport] = attendant
        obj1 = Airport()
        
        obj1.attendants = attendants
        return attendants

    def read_pilots(self):
        pilots_file = open("data/pilots.csv", "r", encoding="utf-8")
        lines = pilots_file.readlines()
        pilots_file.close()
        lines.pop(0)

        pilots = {}

        for l in lines:
            fields = l.split(",")
            passport = fields[0]
            pilot = Pilot(passport, fields[1], fields[2],
                           fields[3], fields[4], fields[5], fields[6])
            pilots[passport] = pilot
        obj1 = Airport()
        
        obj1.pilots = pilots
        return pilots

    def read_flights(self):
        flights_file = open("data/flights.csv", "r", encoding="utf-8")
        lines = flights_file.readlines()
        flights_file.close()
        lines.pop(0)

        flights = {}

        for l in lines:
            fields = l.split(",")
            id = fields[0]
            plate = fields[1]
            flight = Flight(id, plate, fields[2],
                            fields[3], fields[4], fields[5], fields[6],
                            fields[7], fields[8], fields[9], fields[10],
                            fields[11], fields[12], fields[13])
            code = id+plate
            flights[code] = flight
        obj1 = Airport()
        
        obj1.flights = flights
        return flights

    def read_planes(self):
        planes_file = open("data/planes.csv", "r", encoding="utf-8")
        lines = planes_file.readlines()
        planes_file.close()
        lines.pop(0)
        planes = {}
        
        for l in lines:
            fields = l.split(",")
            plate = fields[0]
            plane = Planes(plate, fields[1], fields[2], fields[3], fields[4], fields[5])
            planes[plate] = plane
        obj1 = Airport()
        
        obj1.planes = planes
        return planes 
    
    def read_passengers(self):
        passengers_file = open("data/passengers.csv", "r", encoding="utf-8")
        lines = passengers_file.readlines()
        passengers_file.close()
        lines.pop(0)
        passengers = {}
        
        for l in lines:
            fields = l.split(",")
            passport = fields[1]
            passenger = Passengers(fields[0], passport, fields[2], fields[3], fields[4])
            passengers[passport] = passenger
        obj1 = Airport()
        
        obj1.passengers = passengers
        return passengers 

    def read_travellers(self):
        travellers_file = open("data/travellers.csv", "r", encoding="utf-8")
        lines = travellers_file.readlines()
        travellers_file.close()
        lines.pop(0)
        travellers = {} 

        for l in lines:
            fields = l.split(",")
            passport = fields [0]
            traveller = Traveller(passport,fields[1], fields[2], fields[3], fields[4], fields[5], fields[6])
            travellers[passport] = traveller
        obj1 = Airport()
        
        obj1.travellers = travellers
        return travellers

    def write_flights(self, _list, _prev_list):
        #escribir en memoria
        flights = {}
        id = _list[0]
        plate = _list[1]
        flight = Flight(id, plate, _list[2], _list[3], _list[4], _list[5], _list[6], _list[7],
                         _list[8], _list[9], _list[10], _list[11], _list[12], _list[13])
        code = id+plate
        print(flights)
        _prev_list[code] = flight
        print(_prev_list)
        obj1 = Airport()
        
        obj1.flights = _prev_list
        return _prev_list
        #escribir en archivo
        #FALTA
    def write_travellers(self, _list, _prev_list):
        travellers = {}
        pasaporte = _list[0]
        traveller = Crew(pasaporte, _list[1], _list[2], _list[3], _list[4], _list[5], _list[6])
        print(travellers)
        _prev_list[pasaporte] = traveller
        print(_prev_list)
        obj1 = Airport()
        
        obj1.travellers = _prev_list
        return _prev_list
    def write_passengers(self, _list, _prev_list):
        #AQUI LO DEJE
        passengers = {}
        pasaporte = _list[1]
        passenger = Passengers(_list[0], pasaporte, _list[2], _list[3], _list[4])
        print(passengers)
        _prev_list[pasaporte] = passenger
        print(_prev_list)
        obj1 = Airport()
        
        obj1.passengers = _prev_list
        return _prev_list
    def modify_pilots(self, _passport, _x, _dict):
        if _x == 1:
            _dict[_passport].marital_status = "Single"
        elif _x == 2:
            _dict[_passport].marital_status = "Married"
        elif _x == 3:
            _dict[_passport].marital_status = "Divorced"
        elif _x == 4:
            _dict[_passport].marital_status = "Widowed"
        else:
            print("Opción inválida")
        print(_dict[_passport].marital_status)
        obj1 = Airport()
        
        obj1.pilots = _dict
        return _dict
    def modify_attendants(self, _passport, _x, _dict):
        if _x == 1:
            _dict[_passport].marital_status = "Single"
        elif _x == 2:
            _dict[_passport].marital_status = "Married"
        elif _x == 3:
            _dict[_passport].marital_status = "Divorced"
        elif _x == 4:
            _dict[_passport].marital_status = "Widowed"
        else:
            print("Opción inválida")
        print(_dict[_passport].marital_status)
        obj1 = Airport()
        
        obj1.attendants = _dict
        return _dict
    def modify_travellers(self, _passport, _x, x, _dict):
        if _x == 1:
            if x == 1:
                _dict[_passport].marital_status = "Single"
            elif x == 2:
                _dict[_passport].marital_status = "Married"
            elif x == 3:
                _dict[_passport].marital_status = "Divorced"
            elif x == 4:
                _dict[_passport].marital_status = "Widowed"
            else:
                print("Opción inválida")
            print(_dict[_passport].marital_status)
            obj1 = Airport()
            
            obj1.travellers = _dict
        elif _x == 2:
            if x == 1:
                _dict[_passport].gender = "MA"
            elif x == 2:
                _dict[_passport].gender = "FE"
            else:
                print("Opción inválida")
            print(_dict[_passport].gender)
            obj1 = Airport()
            
            obj1.travellers = _dict
        elif _x == 3:
            _dict[_passport].date_of_birth = x
            print(_dict[_passport].date_of_birth)
            obj1 = Airport()
            
            obj1.travellers = _dict
        elif _x == 4:
            flname = x.split(",")
            _dict[_passport].forename = flname[0]
            _dict[_passport].surname = flname[1]
            print(_dict[_passport].forename, _dict[_passport].surname)
            obj1 = Airport()
            
            obj1.travellers = _dict
        else:
            print("Opción inválida")
    def modify_passengers(self, _passport, _x, x, _dict):
        if _x == 1:
            _dict[_passport].seat = x
            print(_dict[_passport].seat)
            obj1 = Airport()
            
            obj1.passengers = _dict
        elif _x == 2:
            if x == 1:
                _dict[_passport].classes = "premier"
            elif x == 2:
                _dict[_passport].classes = "business"
            elif x == 3:
                _dict[_passport].classes = "economic"
            else:
                print("Opción inválida")
            print(_dict[_passport].classes)
            obj1 = Airport()
            
            obj1.passengers = _dict
        elif _x == 3:
            if x == 1:
                _dict[_passport].location = "check-in"
            elif x == 2:
                _dict[_passport].location = "security"
            elif x == 3:
                _dict[_passport].location = "boarded"
            else:
                print("Opción inválida")
            print(_dict[_passport].location)
            obj1 = Airport()
            
            obj1.passengers = _dict
        else:
            print("Opción inválida")
    def modify_flights(self, _code, _x, x, _dict):
        if _x == 1:
            _dict[_code].status = x
            print(_dict[_code].status)
        elif _x == 2:
            gates = x.split(",")
            _dict[_code].departure_gate = gates[0]
            _dict[_code].arriving_gate = gates[1]
            print(_dict[_code].departure_gate, _dict[_code].arriving_gate)
        elif _x == 3:
            tracks = x.split(",")
            _dict[_code].take_off_track = tracks[0]
            _dict[_code].landing_track = tracks[1]
            print(_dict[_code].departure_gate, _dict[_code].arriving_gate)
        elif _x == 4:
            _dict[_code].attendants = x
            print(_dict[_code].attendants)
        else:
            print("Opción inválida")
        obj1 = Airport()
        
        obj1.flights = _dict


