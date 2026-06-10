from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
import requests_cache
from datetime import datetime, timedelta
from flight_data import FlightData, find_cheapest_flights
from notification_manager import NotificationManager


#requests_cache.install_cache(
 #   'flight_cache',
  #  urls_expire_after={
   #     "*.sheety.co*": requests_cache.DO_NOT_CACHE,
    #    "*": 3600,
    #}
#)
total_days = 180

tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
six_months = (datetime.now() + timedelta(days=total_days)).strftime("%Y-%m-%d")


flight_search = FlightSearch()
data_manager = DataManager()
sheet_code = data_manager.get_sheet_data()
print(sheet_code)
customer_emails = data_manager.get_customer_emails()
emails = [email["whatIsYourEmail ?"] for email in customer_emails["users"]][0]
notification_manager = NotificationManager()

for city in sheet_code["prices"]:
    price_list = flight_search.get_flights(departure="DEL", arrival=city["iataCode"], date_now=tomorrow, return_date=six_months)
    cheapest = find_cheapest_flights(price_list, return_date=six_months)
    print(cheapest.price, cheapest.origin_airport, cheapest.destination_airport, cheapest.out_date)
    if cheapest.price != "N/A" and cheapest.price < city["lowestPrice"]:
        notification_manager.send_sms(cheapest)
        data_manager.update_lowest_price(row_id=city["id"], new_price=cheapest.price)
    if cheapest.price == "N/A":
        price_list = flight_search.get_flights(departure="DEL", arrival=city["iataCode"], date_now=tomorrow, return_date=six_months, is_direct=False)
        cheapest = find_cheapest_flights(price_list, return_date=six_months)
        print(cheapest.price, cheapest.origin_airport, cheapest.destination_airport, cheapest.out_date, cheapest.nr_stops)




