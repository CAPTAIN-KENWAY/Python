import smtplib
from data_manager import DataManager

from flight_data import FlightData
EMAIL = "pythontesting810@gmail.com"
PASSWORD = "jflzmvkrbbuhavxz"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, data: FlightData):
        self.price = data.price
        self.from_city = data.from_city
        self.from_iatacode = data.going_airport
        self.to_city = data.to_city
        self.to_iatacode = data.return_airport
        self.from_date = data.going_departure_date
        self.to_date = data.return_arrival_date
        self.stopover = data.stopover
        self.via_city = data.via_city

    def send_email(self, users_data: DataManager):
        google_flight_link = f"https://www.google.co.in/flights?hl=en#flt={self.from_iatacode}.{self.to_iatacode}.{self.from_date}*{self.to_iatacode}.{self.from_iatacode}.{self.to_date}"
        if self.stopover == 0:
            msg = f"Subject: Low Price Alert!\n\nOnly ₹{self.price} to fly from {self.from_city}-{self.from_iatacode} to {self.to_city}-{self.to_iatacode}, from {self.from_date} to {self.to_date}.\n{google_flight_link}"
        else:
            msg = f"Subject: Low Price Alert!\n\nOnly ₹{self.price} to fly from {self.from_city}-{self.from_iatacode} to {self.to_city}-{self.to_iatacode}, from {self.from_date} to {self.to_date}. \n\n Flight has {self.stopover} stopover, via {self.via_city}\n{google_flight_link}"
        for i in users_data:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs=f"{i['email']}",
                    msg=msg.encode('utf-8')
                )
