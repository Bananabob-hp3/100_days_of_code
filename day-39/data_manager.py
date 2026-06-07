import requests

class DataManager:
    def __init__(self):
        self.endpoint = "https://api.sheety.co/b87c11a7cccc7d25a4f65168e2513bd3/copyOfFlightDeals/prices"
        self.headers = {"Authorization":"Basic bnVsbDpudWxs"}

    def get_sheet_data(self):
        response = requests.get(self.endpoint, headers=self.headers)
        data = response.json()
        return data

    def update_lowest_price(self, row_id, new_price):
        response = requests.put(f"{self.endpoint}/{row_id}", json={"price":{"lowestPrice": new_price}}, headers=self.headers)
        data = response.text


