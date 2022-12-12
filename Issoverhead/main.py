import smtplib
import time
import requests
from datetime import datetime

MY_LATITUDE = 28.459497  # Your latitude
MY_LONGITUDE = 77.026634  # Your longitude
MY_EMAIL = "pythontesting810@gmail.com"
MY_PASSWORD = "jflzmvkrbbuhavxz"


# Your position is within +5 or -5 degrees of the ISS position.


def check_pos():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if (iss_latitude-5) < MY_LATITUDE < (iss_latitude+5) and (iss_longitude-5) < MY_LONGITUDE < (iss_longitude+5):
        return True
    return False


parameters = {
    "lat": MY_LATITUDE,
    "long": MY_LONGITUDE,
    "formatted": 0
}
def is_night():
    response = requests.get("http://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()
    hour = time_now.hour
    if (hour > sunset or hour < sunrise):
        return True

while True:
    if is_night() and check_pos():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="guptakaran094@gmail.com",
                msg="Subject:Look Up!\n\nThe ISS is near your location.\nLook Up"
            )
    time.sleep(60)

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
