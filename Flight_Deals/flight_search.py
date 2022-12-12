import requests

from flight_data import FlightData
API_KEY = "XB6mDHUnNWBVjnR2Xin5uGqvtfKAZlIK"
KIWI_ENDPOINT = "https://tequila-api.kiwi.com"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.header = {'apikey': API_KEY}

    def search_iatacode(self, city):
        loc_parameters = {
            'term': city,
            'locale': 'en-US',
            'location_types': 'airport',
            'active_only': 'true'
        }
        response = requests.get(url=f"{KIWI_ENDPOINT}/locations/query",
                                params=loc_parameters, headers=self.header)
        response.raise_for_status()
        iatacode = response.json()['locations'][0]['city']['code']
        return iatacode

    def search_flight(self, fromcity, tocity, fromdate, todate):
        flight_parameters = {
            'fly_from': fromcity,
            'fly_to': tocity,
            'dateFrom': fromdate,
            'dateTo': todate,
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'curr': 'INR',
            'vehicle_type': 'aircraft',
            'one_for_city': 1,
            'max_stopovers': 0,
            'flight_type': 'round'
        }
        response = requests.get(url=f"{KIWI_ENDPOINT}/v2/search",
                                params=flight_parameters, headers=self.header)

        try:
            response.json()['data'][0]
        except IndexError:
            flight_parameters['max_stopovers'] = 2
            response = requests.get(url=f"{KIWI_ENDPOINT}/v2/search",
                                params=flight_parameters, headers=self.header)
            try:
                response.json()['data'][0]
            except IndexError:
                print(f"No direct/stopover flights found for destination {tocity}")
                return None
            flight_data = FlightData(
            price=response.json()['data'][0]['price'],
            city_from=response.json()['data'][0]['cityFrom'],
            city_to=response.json()['data'][0]['cityTo'],
            days=response.json()['data'][0]['nightsInDest'],
            going_airport=response.json()['data'][0]['route'][0]['flyFrom'],
            going_dest_airport=response.json()['data'][0]['route'][0]['flyTo'],
            going_flightno=response.json()['data'][0]['route'][0]['flight_no'],
            going_airline=response.json()['data'][0]['route'][0]['airline'],
            return_airport=response.json()['data'][0]['route'][2]['flyFrom'],
            return_dest_airport=response.json()['data'][0]['route'][2]['flyTo'],
            return_flightno=response.json()['data'][0]['route'][2]['flight_no'],
            return_airline=response.json()['data'][0]['route'][2]['airline'],
            going_departure=response.json()['data'][0]['route'][0]['utc_departure'].split("T")[0],
            return_arrival=response.json()['data'][0]['route'][2]['utc_arrival'].split("T")[0],
            stopover= 1,
            via_city=response.json()['data'][0]['route'][1]['cityFrom']
            )
            return flight_data

        flight_data = FlightData(
            price=response.json()['data'][0]['price'],
            city_from=response.json()['data'][0]['cityFrom'],
            city_to=response.json()['data'][0]['cityTo'],
            days=response.json()['data'][0]['nightsInDest'],
            going_airport=response.json()['data'][0]['route'][0]['flyFrom'],
            going_dest_airport=response.json()['data'][0]['route'][0]['flyTo'],
            going_flightno=response.json()['data'][0]['route'][0]['flight_no'],
            going_airline=response.json()['data'][0]['route'][0]['airline'],
            return_airport=response.json()['data'][0]['route'][1]['flyFrom'],
            return_dest_airport=response.json()['data'][0]['route'][1]['flyTo'],
            return_flightno=response.json()['data'][0]['route'][1]['flight_no'],
            return_airline=response.json()['data'][0]['route'][1]['airline'],
            going_departure=response.json()['data'][0]['route'][0]['utc_departure'].split("T")[0],
            return_arrival=response.json()['data'][0]['route'][1]['utc_arrival'].split("T")[0],
            via_city="",
            stopover=0
        )
        return flight_data
