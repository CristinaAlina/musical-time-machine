# Day 46 - 100 Days of Code: The Complete Python Pro Bootcamp for 2023

![Musical Time Machine](https://d112y698adiu2z.cloudfront.net/photos/production/software_photos/001/634/622/datas/original.jpg)

## Musical Time Machine Program - Get the TOP 100 songs on Billboard on a specific datetime of your life and make a playlist with them on Spotify! 🎶

## Steps:
1. Create input prompt for input user in format YYYY-MM-DD.
2. Scrape the top 100 songs on Billboard, use BeautifulSoup module to parse the html and format 2 Python lists, one with songs and the other one with the artists.
3. Authenticate on Spotify: [Spotify link](http://spotify.com/signup/)
4. Go to Developer Dashboard and create a Spotify App: [Developer Dashboard](https://developer.spotify.com/dashboard/)
5. Set an Redirect Uri and get your Cliend Id and Client Secret for Spotipy APIs 
6. Use Spotipy documentation [Spotipy documentation]([https://spotipy.readthedocs.io/en/2.22.1/](https://spotipy.readthedocs.io/en/2.22.1/#spotipy.oauth2.SpotifyOAuth)) for Authorization Code Flow
7. Use Search for item API for getting track uri using a format query with year, song title and artist: [Developer Spotify - Search](https://developer.spotify.com/documentation/web-api/reference/search)
8. Format a list with all of the tracks uri that the search API has found.
9. Use Create Playlist API for creating a playlist in Spotify: [Developer Spotify - create-playlist](https://developer.spotify.com/documentation/web-api/reference/create-playlist)
10. Use Add Items to Playlist API for adding the list of uri songs to the new playlist id: [Developer Spotify - add-tracks-to-playlist](https://developer.spotify.com/documentation/web-api/reference/add-tracks-to-playlist)
