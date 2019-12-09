from airporUI import AirportUI
from airportDP import Airport

if __name__=="__main__":
    #Prueba para ver si salen los valores
    my_airport = Airport()
    x = my_airport.populate_airport()
    test_obj = AirportUI()
    test_obj.user_decision_menu()
    
