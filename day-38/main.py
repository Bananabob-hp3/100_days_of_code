import os
import requests
from datetime import datetime
from datetime import datetime


App_Id = os.environ.get("App_ID")
API_key = os.environ.get("API_key")

now = datetime.now()
day_now = now.strftime("%Y%m%d")
time_now = str(now).split()[1]


NUTRITION_ENDPOINT = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"


headers = {
    "x-app-id":App_Id,
    "x-app-key":API_key
}

nutrition_config = {
    "query": input("Which exercises did you do today? ")
}


response = requests.post(NUTRITION_ENDPOINT, json=nutrition_config, headers=headers)
data = response.json()
exercises = data["exercises"]

for n in exercises:
    sheety_config= {"workout":{
        "date":day_now,
        "time":time_now,
        "exercise":n["user_input"].title(),
        "duration":n["duration_min"],
        "calories":n["nf_calories"]
    }}

    headers = {
        "Authorization":"Basic TWVsYXRvbmluOlBBU1NXT1JE"
    }

    response = requests.post(url="https://api.sheety.co/b87c11a7cccc7d25a4f65168e2513bd3/copyOfMyWorkouts/workouts", json=sheety_config, headers=headers)
    print(response.text)




