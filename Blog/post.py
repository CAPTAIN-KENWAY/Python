import requests


class Post:
    def get_all_posts(self):
        response = requests.get(url="https://api.npoint.io/4af156202f984d3464c3")
        data = response.json()
        return data

    def get_post(self, id):
        response = requests.get(url="https://api.npoint.io/4af156202f984d3464c3")
        data = response.json()
        return data[id-1]
