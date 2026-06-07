from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
import requests_cache
from datetime import datetime, timedelta
from flight_data import FlightData, find_cheapest_flights
from notification_manager import NotificationManager



requests_cache.install_cache('flight_cache', allowable_methods=["GET"])
total_days = 180

tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
six_months = (datetime.now() + timedelta(days=total_days)).strftime("%Y-%m-%d")


flight_search = FlightSearch()
data_manager = DataManager()
sheet_code = data_manager.get_sheet_data()
notification_manager = NotificationManager()

for city in sheet_code["prices"]:
    price_list = flight_search.get_flights(departure="DEL", arrival=city["iataCode"], date_now=tomorrow, return_date=six_months)
    cheapest = find_cheapest_flights(price_list, return_date=six_months)
    print(cheapest.price, cheapest.origin_airport, cheapest.destination_airport, cheapest.out_date)
    if cheapest.price != "N/A" and cheapest.price < city["lowestPrice"]:
        notification_manager.send_sms(cheapest)
        data_manager.update_lowest_price(row_id=city["id"], new_price=cheapest.price)
