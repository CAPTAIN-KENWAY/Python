import requests

api_key = "3610943fdd217a4ce635e35fa0516ee2"
latitude = 28.459497
longitude = 77.026634
parameters = {
    'lat': latitude,
    'lon': longitude,
    'exclude': "daily,minutely,current,alerts",
    'appid': api_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly_12_data = weather_data["hourly"][0:24]
for i in hourly_12_data:
    weather_id = int(i["weather"][0]["id"])
    if weather_id < 700:
        print(f"Bring an Umbrella at {hourly_12_data.index(i)}:00")
