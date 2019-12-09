from airporUI import AirportUI
from airportDP import Airport

if __name__ == "__main__":
    #modificar
    interaction = AirportUI()
    date, time = interaction.get_user_input()
    my_airport = Airport()
    my_airport.populate_airport()
    print(my_airport.generate_statistics(date, time))
