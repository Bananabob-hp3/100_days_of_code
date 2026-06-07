import os
import requests
from datetime import datetime
from data_manager import DataManager
api_key = os.environ.get("SerpApi_key")

class FlightSearch:
    def __init__(self):
        self.endpoint = "https://serpapi.com/search?engine=google_flights"

    def get_flights(self, departure, arrival, date_now, return_date):
        parameters = {
            "departure_id": departure,
            "arrival_id": arrival,
            "outbound_date": date_now,
            "type": "1",
            "api_key": api_key,
            "return_date":return_date
        }
        response = requests.get(self.endpoint, params=parameters)
        data = response.json()
        return data

flight_search = FlightSearch()

