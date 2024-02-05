import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = "http://example.com/callback"
SPOTIPY_USERNAME = os.environ.get("SPOTIPY_DISPLAY_NAME")

user_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
billboard_url = f"https://www.billboard.com/charts/hot-100/{user_date}"

response = requests.get(url=billboard_url)
billboard_html = response.text

soup = BeautifulSoup(billboard_html, "html.parser")
song_tags = soup.find_all(
    name="ul",
    class_="lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max"
)

song_titles = [tag.find(name="h3").getText().strip() for tag in song_tags]
song_artists = [tag.find(name="span").getText().strip() for tag in song_tags]

spotify = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                       client_secret=SPOTIPY_CLIENT_SECRET,
                       redirect_uri=SPOTIPY_REDIRECT_URI,
                       show_dialog=True,
                       scope="playlist-modify-private",
                       cache_path="token.txt",
                       username=SPOTIPY_USERNAME)

access_token = spotify.get_access_token(as_dict=False)

spotify_api_client = spotipy.client.Spotify(auth=access_token)
user_id = spotify_api_client.current_user()["id"]

uri_tracks_list = []
year_date = user_date.split("-")[0]
for song_title in song_titles:
    query = f"track: {song_title} year: {year_date} artist: {song_artists[song_titles.index(song_title)]}"
    result = spotify_api_client.search(q=query, limit=1, offset=0, type='track', market=None)

    try:
        track_uri = result["tracks"]["items"][0]["uri"]
    except IndexError:
        pass
    else:
        uri_tracks_list.append(track_uri)
