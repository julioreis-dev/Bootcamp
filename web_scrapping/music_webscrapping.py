import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import pprint


CLIENT_ID = 'e86179a30d914213b1cf236258ce3045'
CLIENT_SECRET = 'ae306fc746e346a888798cbaef626545'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri='http://127.0.0.1:8080/',
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt"
                                               ))

user_id = sp.current_user()['id']
# print(user_id)

period = input('Qual período você deseja obter as músicas? Tipo de data YYYY-MM-DD:')
url = f'https://www.billboard.com/charts/hot-100/{period}'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
ranking_songs = soup.find_all(name='span', class_='chart-element__rank__number')
songs_names = soup.find_all(name='span', class_='chart-element__information__song text--truncate color--primary')
songs = [song.getText() for song in songs_names]
year = period.split('-')[0]
song_uris = []
for song_names in songs:
    result = sp.search(q=f"track:{song_names} year:{year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song_names} doesn't exist in Spotify. Skipped.")

print(song_uris)
playlist = sp.user_playlist_create(user=user_id, name=f"{period} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
