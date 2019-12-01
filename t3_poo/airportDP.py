#Dominio del Problema

class Airport:
	def __init__(self):
		self.tracks = None
		self.airplanes = None
		self.passengers = None
		self.pilots = None
		self.attendants = None
		self.travellers = None


    def Populate_airport():
        #Cargador de datos
        data_loader = AirportAD
        #Datos asignados a sus componenetes
        self.pilots = data_loader.read_pilots_file()
        self.travellers = data_loader.read_travellers_file()



class Pilot:
	def __init__(self, _passport, _forename, _surname, _date_of_birth, _country, _marital_status, _gender):

		self.passport = _passport
		self.forename = _forename
		self.surname = _surname
		self.date_of_birth = _date_of_birth
		self.country = _country
		self.gender = _gender
		self.marital_status = _marital_status

#Clases de Administracion de Datos AirportAD

class AirportAD:
	def read_pilots_file(Self):
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

		return pilots#Dominio del Problema


class Airport:
	def __init__(self):
		self.tracks = None
		self.airplanes = None
		self.passengers = None
		self.pilots = None
		self.attendants = None
		self.travellers = None


    def Populate_airport():
        #Cargador de datos
        data_loader = AirportAD
        #Datos asignados a sus componenetes
        self.pilots = data_loader.read_pilots_file()
        self.travellers = data_loader.read_travellers_file()



class Pilot:
	def __init__(self, _passport, _forename, _surname, _date_of_birth, _country, _marital_status, _gender):

		self.passport = _passport
		self.forename = _forename
		self.surname = _surname
		self.date_of_birth = _date_of_birth
		self.country = _country
		self.gender = _gender
		self.marital_status = _marital_status


#Clases de Administracion de Datos AirportAD

class AirportAD:
	def read_pilots_file(Self):
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