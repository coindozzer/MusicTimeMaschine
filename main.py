import json
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

URL = f"https://www.billboard.com/charts/hot-100/"
USER = "" # Enter User Here

desired_date = input(f"Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
name = input(f"whom is this list for?")

lookup_url = f"{URL}/{desired_date}/"

response = requests.get(lookup_url)
html = response.text
#
songs = []
artists = []
track_list = []
track_uris = []

soup = BeautifulSoup(html, "html.parser")
songs_html = soup.find_all(name="li", class_="o-chart-results-list__item // lrv-u-flex-grow-1 lrv-u-flex lrv-u-flex-direction-column lrv-u-justify-content-center lrv-u-border-b-1 u-border-b-0@mobile-max lrv-u-border-color-grey-light lrv-u-padding-l-050 lrv-u-padding-l-1@mobile-max")

songs = [song.find(name="h3").getText().strip() for song in songs_html]
artists = [song.find(name="span").getText().strip() for song in songs_html]
print(songs)
print(artists)

zip = zip(songs,artists)

for a,b in zip:
    song = str(a).replace(" ","%20")
    artist = str(b).replace(" ","%20")
    string = f"{song}%20artist:{artist}"
    track_list.append(string)

print(track_list)


#search tracks

scope = "user-read-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
for track in track_list:
    search = sp.search(track,limit=1,offset=1,type="track",market=None)
    print(json.dumps(search, sort_keys=True,indent=4))
    if(search["tracks"]["items"]):
        track_uri = search["tracks"]["items"][0]["uri"]
        track_uris.append(track_uri)
        print(track_uri)


#create a new playlist

scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
response = sp.user_playlist_create(USER,f"{name}'s Geburtstagsliste",False,False,"Das ist deine Geburtstags Playlist!")
playlist_id = response["id"]

# #add a track to a playlist

add_tracks = sp.playlist_add_items(playlist_id=playlist_id, items=track_uris, position=None)

#enter system variables here

# $env:SPOTIPY_CLIENT_ID=''
# $env:SPOTIPY_CLIENT_SECRET=''
# $env:SPOTIPY_REDIRECT_URI='http://google.com'

# print(json.dump(VARIABLE, sort_keys=True, indent=4)