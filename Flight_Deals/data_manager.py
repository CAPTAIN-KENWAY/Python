import requests
TOKEN = "hgurbierigbikerbigtbibetyerbyht"
ENDPOINT = "https://api.sheety.co/ce18b7146fc6c8759164227401f1d1e4/flightDeals"


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.price_endpoint = f"{ENDPOINT}/prices"
        self.user_endpoint = f"{ENDPOINT}/users"
        self.header = {"Authorization": f"Bearer {TOKEN}"}

    def get_data(self):
        response = requests.get(url=self.price_endpoint, headers=self.header)
        response.raise_for_status()
        return response.json()["prices"]

    def put_data(self, obj_id, iatacode):
        data = {
            'price': {
                'iataCode': iatacode
            }
        }
        requests.put(url=f"{self.price_endpoint}/{obj_id}", json=data, headers=self.header)

    def get_data_users(self):
        response = requests.get(url=self.user_endpoint, headers=self.header)
        response.raise_for_status()
        return response.json()["users"]
    
    def put_data_users(self, fname, lname, email):
        data = {
            'user': {
                'firstName': fname,
                'lastName': lname,
                'email': email
            }
        }
        requests.post(url=f"{self.user_endpoint}", json=data, headers=self.header)
        
