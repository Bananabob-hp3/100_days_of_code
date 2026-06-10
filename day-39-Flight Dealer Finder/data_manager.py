import requests

class DataManager:
    def __init__(self):
        self.endpoint = "https://api.sheety.co/b87c11a7cccc7d25a4f65168e2513bd3/copyOfFlightDeals"
        self.headers = {
            "Authorization": "Bearer somesecrettoken"
        }

    def get_sheet_data(self):
        response = requests.get(url=f"{self.endpoint}/prices", headers=self.headers)
        data = response.text
        print(response.status_code)
        print(data)
        return data

    def update_lowest_price(self, row_id, new_price):
        response = requests.put(f"{self.endpoint}/prices/{row_id}", json={"price":{"lowestPrice": new_price}}, headers=self.headers)
        data = response.text

    def get_customer_emails(self):
        response = requests.get(f"{self.endpoint}/users", headers=self.headers)
        data = response.json()
        return data



