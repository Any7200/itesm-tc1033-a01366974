#A01366974 ANA LAURA RODRIGUEZ JURADO
#-*- coding:utf-8 -*-

class Airport:
	def __init__(self):
		self.tracks = None
		self.airplanes = None
		self.passengers = None
		self.pilots = None
		self.attendants = None
		self.travellers = None

	def populate__airport(self):
		data_loader = AirportAD
		#Datos asignados a sus componenetes
		self.pilots = data_loader.read_pilots_file()
		self.passengers = data_loader.read_passengers_file()
class Crew:
	def __init__(self, _passport, _forename, _surname, _date_of_birth, _country, _marital_status, _gender):

		self.passport = _passport
		self.forename = _forename
		self.surname = _surname
		self.date_of_birth = _date_of_birth
		self.country = _country
		self.gender = _gender
		self.marital_status = _marital_status


class Pilot(Crew):
	def __init__(self, _passport, _forename, _surname, _date_of_birth, _country, _marital_status, _gender):

		self.passport = _passport
		self.forename = _forename
		self.surname = _surname
		self.date_of_birth = _date_of_birth
		self.country = _country
		self.gender = _gender
		self.marital_status = _marital_status

class Passenger:
	def __init__(self, _passport, _forename, _surname, _date_of_birth, _country, _marital_status, _gender, _airport_status):

		self.passport = _passport
		self.forename = _forename
		self.surname = _surname
		self.date_of_birth = _date_of_birth
		self.country = _country
		self.gender = _gender
		self.marital_status = _marital_status
		self.airport_status = _airport_status

	def registerOnline(self):
		pass

	def documentLuggage(self):
		pass
class Airline:
	def __init__(self,_name):
		self.name = _name

class Airplane:
	def __init__(self, _id, _manufacturer, _nmodel, _pCapacity, _lCapacity, _maxV, _flights, _nFlights):
		self.id = _id
		self.manufacturer = _manufacturer
		self.nmodel = _pCapacity
		self.lCapacity = _lCapacity
		self.maxV = _maxV
		self.flights = _flights
		self.nFlights = _nFlights

	def takeOff(self):
		pass

	def land(self):
		pass

	def checkFlightsNumber(self):
		pass

class Report:
	def __init__(self, _trackState, _airplanes, _passengers, _pilots, _assistant):
		self._trackState = _trackState
		self.airplanes = _airplanes
		self.passengers = _passengers
		self.pilots = _pilots
		self.assistants = _assistant

	def checkTrackstate(self):
		pass 

	def countAirplanes(self):
		pass 

	def countPassengers(self):
		pass 

	def countPilots(self):
		pass 
	def countAssistants(self):
		pass
class Flight():
	def __init__(self, _id, _tArrival, _tDeparture, _fType, _state, _gArrival, _gDeparture, _trackArrival, _trackDeparture, _pilots, _assistants, _passengers):
		self.id = _id
		self.tArrival = _tArrival
		self.tDeparture = _tDeparture
		self.fType = _fType
		self.state = _state
		self.gArrival = _gArrival
		self.gDeparture = _gDeparture
		self.trackArrival = _trackArrival
		self.trackDeparture = _trackDeparture
		self.pilots = _pilots
		self.assistants =  _assistants
		self.passengers = _passengers

	def checkPilots(self):
		pass 
	
	def checkAssistants(self):
		pass 
	
	def checkPassengers(self):
		pass 

#Clases de Administracion de Datos AirportAD
class AirportAD:
	def read_pilots_file(self):
		pilots_file=open("data/pilots.csv", "r")
		lines=pilots_file.readlines()
		lines.pop(0)

		pilots = {}

		for line in lines:

			#ME1559,Valentina,Garza,660404,Mexico,NA,Single

			fields=line.split(",")
			passport=fields[0]
			forename=fields[1]
			surname=fields[2]
			date_of_birth=fields[3]
			country=fields[4]
			gender=fields[5]
			marital_status=fields[6]

			pilot = Pilot(passport, forename, surname, date_of_birth, country, gender, marital_status)

			pilots[passport]=pilot

		return pilots
	def read_passengers_file(self):
		pass_file=open("data/travellers.csv", "r")
		lines=pass_file.readlines()
		lines.pop(0)
		pass_file.close()
		pass_file=open("data/passengers.csv", "r")
		lines2=pass_file.readline()
		lines2.pop(0)
		
		passengers = {}

		for line in lines:

			#ME1559,Valentina,Garza,660404,Mexico,NA,Single

			fields=line.split(",")
			passport=fields[0]
			forename=fields[1]
			surname=fields[2]
			date_of_birth=fields[3]
			country=fields[4]
			gender=fields[5]
			marital_status=fields[6]

			passenger = Passenger(passport, forename, surname, date_of_birth, country, gender, marital_status)

			passengers[passport]=passenger
		
		return passengers
