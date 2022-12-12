import time
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


SPOTIPY_CLIENT_ID = "521410e381e34187b18814a3df15cdeb"
SPOTIPY_CLIENT_SECRET = "d959de9d6f894a07a15d7b9831f0b566"
SPOTIPY_REDIRECT_URL = "http://example.com"
URL = "https://www.billboard.com/charts/hot-100/"
ARTIST_CLASS_2 = "c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet"
ARTIST_CLASS = "c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only"
CLASS = "c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"
CLASS_2 = "c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet"

#-------------------------------GET SONGS FROM BILLBOARD-----------------------------------#

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
y = date.split('-')[0]
response = requests.get(url=f"{URL}{date}")
soup = BeautifulSoup(response.text, 'html.parser')
song_1 = soup.find(name="h3", class_=CLASS_2, id="title-of-a-story").getText().strip()
songs = [
    song.getText().strip()
    for song in soup.find_all(name="h3", class_=CLASS, id="title-of-a-story")]
songs.insert(0, song_1)

artist_1 = soup.find(name="span", class_=ARTIST_CLASS_2).getText().strip()
artists = [
    artist.getText().strip()
    for artist in soup.find_all(name="span", class_=ARTIST_CLASS)]
artists.insert(0, artist_1)

for i in range(len(artists)):
    if 'Featuring' in artists[i]:
        artists[i] = artists[i].split('Featuring')[0]
    if ',' in artists[i]:
        artists[i] = artists[i].split(',')[0]
    if '&' in artists[i]:
        artists[i] = artists[i].split('&')[0]
    if '+' in artists[i]:
        artists[i] = artists[i].split('+')[0]

# with open("y.txt", mode="w") as file:
#     for song in songs:
#         file.write(f"{song} \n")

# with open("x.txt", mode="w") as file:
#     for artist in artists:
#         file.write(f"{artist} \n")


#-------------------------------SPOTIFY-----------------------------------------------------#

scope = "playlist-modify-private"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URL, scope=scope))

user_details = sp.current_user()
user_id = user_details['id']


#-------------------------------SEARCH SONGS IN SPOTIFY-----------------------------------#


song_uris = []
for song, artist in zip(songs, artists):
    song_results = sp.search(q=f"{song} year:{y} artist:{artist}", type='track')
    try:
        uri = song_results['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"{song} is not available in Spotify. Skipped")
    
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard Top 100", public=False, description="None")
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)