import os
import requests
import time
from twilio.rest import Client

OWM_URL = "https://api.openweathermap.org/data/2.5/forecast"
params ={
    "lat":29.59,
    "lon":79.30,
    "appid":os.environ.get("OWM_API_KEY"),
    "cnt": 4
}

response = requests.get(OWM_URL, params=params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for item in weather_data["list"]:
    id = item["weather"][0]["id"]
    if id < 700:
        will_rain = True
if will_rain:
    account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
    auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Its going to rain today, Maybe no electricity, Heat Relief",
        from_="+12184504624",
        to="+919557633058"
)

