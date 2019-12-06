# -*- coding: utf-8 -*-
class Report:
    def __init__(self, _date, _time, _no_empty_tracks, _no_occupied_tracks,
                 _no_passengers_check_in, _no_passengers_security, _no_passengers_boarded,
                  _no_empty_gates, _no_occupied_gates):
        self.date = _date
        self.time = _time
        self.no_empty_tracks = _no_empty_tracks
        self.no_occupied_tracks = _no_occupied_tracks
        self.no_passengers_check_in = _no_passengers_check_in
        self.no_passengers_security = _no_passengers_security
        self.no_passengers_boarded = _no_passengers_boarded
        self.no_empty_gates = _no_empty_gates
        self.no_occupied_gates = _no_occupied_gates

    def write_file(self):
        statistics_file = open("data/statistics.csv", "w+")
        statistics_file.write("date,time,# of empty tracks,# of occupied tracks, #of passengers in check-in, # of passenger in security, # of passengers boarded , # of empty gates,# of occupied gates\n")
        statistics_file.write(self.date+",")
        statistics_file.write(self.time+",")
        statistics_file.write(str(self.no_empty_tracks)+",")
        statistics_file.write(str(self.no_occupied_tracks)+",")
        statistics_file.weite(str(self.no_passengers_check_in)+",")
        statistics_file.write(str(self.no_passengers_security)+",")
        statistics_file.write(str(self.no_passengers_boarded)+",")
        statistics_file.write(str(self.no_empty_gates)+",")
        statistics_file.write(str(self.no_occupied_gates)+",")



class Airport:
    def __init__(self):
        self.tracks = None
        self.airplanes = None
        self.passengers = None
        self.pilots = None
        self.attendants = "vacío"
        self.travellers = None

    def populate_airport(self):
        data_loader = AirportAD()
        self.pilots = data_loader.read_pilots()
        self.flights = data_loader.read_flights()
        self.attendants = data_loader.read_attendants()
        self.passengers = data_loader.read_passengers()

    def generate_statistics(self, _date, _time):
        
        number_empty_tracks = 0
        number_of_occupied_tracks = 0
        number_of_empty_gates = 0
        number_of_occupied_gates = 0
        number_of_passengers_check_in = 0
        number_of_passengers_security = 0
        number_of_passengers_boarded = 0

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
         
            #aqui va el for para passengers
        for passenger in self.passengers.values():
            #location
            if passenger.location == "check in":
                    number_of_passengers_check_in += 1

            elif passenger.location == "security":
                    number_of_passengers_security += 1
            
            elif passenger.location == "boarded":
                    number_of_passengers_boarded +=  1
            else:
                print("INVALID")



                
        report = Report(_date, _time, number_empty_tracks,
                        number_of_occupied_tracks,
                        number_of_empty_gates, number_of_occupied_gates)

        report.write_file()
        print("Reporte generado")



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
            flights[id+plate] = flight

        return flights
    
    def read_passengers(self):
        passengers_file = open("data/passengers.csv", "r", encoding="utf-8")
        lines = passengers_file.readlines()
        passengers_file.close()
        lines.pop(0)
        passengers = {}
        
        for l in lines:
            fields = l.split(",")
            passport = fields[0]
            passenger = Passenger(passport, fields[1], fields[2], fields[3], fields[4])
            passengers[passport] = passenger
            return passengers

    def read_planes(self):
        planes_file = open("data/planes.csv", "r", encoding="utf-8")
        lines = planes_file.readlines()
        planes_file.close()
        lines.pop(0)
        planes = {}  

        for l in lines:
            fields = l.split(",")
            plate = fields [0]
            plane = Plane(plate, fields[1], fields[2],fields[3],fields[4],fields[5])
            planes[plate] = plane
            return planes

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
            return travellers

    def write_flights(self, _list):
        #escribir en memoria
        flights = {}
        id = _list[0]
        plate = _list[1]
        flight = Flight(id, plate, _list[2], _list[3], _list[4], _list[5], _list[6], _list[7],
                         _list[8], _list[9], _list[10], _list[11], _list[12], _list[13])
        flights[id+plate] = flight
        print(flights)
        return flights
        #escribir en archivo
        #FALTA
    def write_travellers(self, _list):
        travellers = {}
        pasaporte = _list[0]
        traveller = Crew(pasaporte, _list[1], _list[2], _list[3], _list[4], _list[5], _list[6])
        travellers[pasaporte] = traveller
        print(travellers)
        return travellers
    def write_passengers(self, _list):
        #AQUI LO DEJE
        passengers = {}
        pasaporte = _list[1]
        passenger = Passengers(_list[0], pasaporte, _list[2], _list[3], _list[4])
        passengers[pasaporte] = passenger
        print(passengers)
        print(passengers["Me7348"])
        return passengers
    def modify_pilots(self):
        pass

    def modify_crew(self):
        pass

    def modify_travellers(self):
        pass

    def modify_passengers(self):
        pass

    def modify_flights(self):
        pass


