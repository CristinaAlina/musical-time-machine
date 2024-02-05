import os

SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = "http://example.com/callback"
SPOTIPY_USERNAME = os.environ.get("SPOTIPY_DISPLAY_NAME")

user_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
billboard_url = f"https://www.billboard.com/charts/hot-100/{user_date}"