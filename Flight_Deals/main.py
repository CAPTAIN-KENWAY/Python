# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
import datetime as dt
from notification_manager import NotificationManager
ORIGIN = "DEL"


today = dt.datetime.now()
tomorrow = dt.datetime.now() + dt.timedelta(days=1)
tomorrow_date = tomorrow.strftime("%d/%m/%Y")
six_months = dt.datetime.now() + dt.timedelta(days=30*6)
six_months_date = six_months.strftime("%d/%m/%Y")

data_manager = DataManager()
flight_search = FlightSearch()
sheets_data = data_manager.get_data()
users_data = data_manager.get_data_users()
for i in sheets_data:
    iatacode = flight_search.search_iatacode(i["city"])
    data_manager.put_data(i['id'], iatacode)


for i in sheets_data:
    flight_data = flight_search.search_flight(ORIGIN, i['iataCode'], tomorrow_date, six_months_date)
    if flight_data != None:
        if flight_data.price <= i['lowestPrice']:
            notification = NotificationManager(flight_data)
            notification.send_email(users_data)




