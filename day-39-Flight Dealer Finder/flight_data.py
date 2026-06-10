class FlightData:
    def __init__(self, price, origin_airport, destination_airport, out_date, return_date, nr_stops):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.nr_stops = nr_stops

def find_cheapest_flights(data, return_date):
    if not data.get("best_flights"):
        return FlightData(
            price="N/A",
            origin_airport="N/A",
            destination_airport="N/A",
            out_date="N/A",
            return_date="N/A",
            nr_stops="N/A"
        )
    best = data["best_flights"]
    other = data["other_flights"]
    all_flights = best + other
    prices = [flight["price"] for flight in all_flights]
    min_price = min(prices)
    min_flight_data = [flight for flight in all_flights if flight["price"] == min_price][0]
    return FlightData(
        price = min_flight_data["price"],
        origin_airport = min_flight_data["flights"][0]["departure_airport"]["id"],
        destination_airport = min_flight_data["flights"][-1]["arrival_airport"]["id"],
        out_date = min_flight_data["flights"][0]["departure_airport"]["time"].split(" ")[0],
        return_date = return_date,
        nr_stops = len(min_flight_data["flights"]) - 1
        )







































