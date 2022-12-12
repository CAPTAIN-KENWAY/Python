class FlightData:
    def __init__(
            self, price, city_from, city_to, days, going_airport, going_dest_airport,
        return_airport, return_dest_airport, going_flightno, return_flightno, going_airline,
            return_airline, going_departure, return_arrival, stopover, via_city):
        
        self.price = price
        self.from_city = city_from
        self.to_city = city_to
        self.total_stay = days
        self.going_airport = going_airport
        self.going_dest_airport = going_dest_airport,
        self.going_flightno = going_flightno
        self.going_airline = going_airline
        self.going_departure_date = going_departure
        self.return_airport = return_airport
        self.return_dest_airport = return_dest_airport
        self.return_flightno = return_flightno
        self.return_airline = return_airline
        self.return_arrival_date = return_arrival
        self.stopover = stopover
        self.via_city = via_city
