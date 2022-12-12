import requests
import datetime as dt

APP_ID = "68702f3b"
API_KEY = "08cfbdd36025af3c7e5582b0658e6e49"
TOKEN = "ytarvkuyvyctunydaiol"
today = dt.datetime.now()
d = today.strftime("%d/%m/%Y")
t = today.strftime("%H:%M:%S")

# Nutritionix 

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
todays_exercise = input("Tell me which exercises you did: ")
query_data = {
    "query": todays_exercise,
    "gender": "male",
    "weight_kg": 65,
    "height_cm": 180,
    "age": 21
}
exercise_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

# Sheety

sheets_endpoint = "https://api.sheety.co/ce18b7146fc6c8759164227401f1d1e4/myWorkouts/workouts"
sheets_header = {
    "Authorization" : f"Bearer {TOKEN}"
}
today = dt.datetime.now()
d = today.strftime("%d/%m/%Y")
response = requests.post(url=exercise_endpoint, json=query_data, headers=exercise_headers)
exercise_data = response.json()
for i in exercise_data["exercises"]:
    Exercise = i["name"].title()
    Duration = i["duration_min"]
    Calories = i["nf_calories"]

    t = today.strftime("%H:%M:%S")
    sheets_data = {
        "workout": {
            "date": d,
            "time": t,
            "exercise": Exercise,
            "duration": Duration,
            "calories": Calories
        }
    }
    requests.post(url=sheets_endpoint, json=sheets_data, headers=sheets_header)