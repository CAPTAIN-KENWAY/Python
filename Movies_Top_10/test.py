import requests

API_URL = "https://api.themoviedb.org/3/search/movie"
API_KEY = "bd68532447e6f3d03e92a058c1e6403e"
IMAGE_URL = 'https://image.tmdb.org/t/p/original'

search = "Drive"
parameters = {
    'language': 'en-US',
    'api_key': API_KEY,
    'query': search,
    'page': 1
}
movie = requests.get(url=API_URL, params=parameters).json()

print(movie['results'][0]['id'])
print(movie['results'][0]['title'])
print(movie['results'][0]['release_date'])
print(movie['results'][0]['overview'])
print(IMAGE_URL + movie['results'][0]['poster_path'])
