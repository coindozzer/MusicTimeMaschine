import requests
from datetime import datetime
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

URL = f"https://www.billboard.com/charts/hot-100/"
#desired_date = input(f"Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
# lookup_url = f"{URL}/2015-03-15/"
#
# print(lookup_url)
#
# response = requests.get(lookup_url)
# html = response.text
#
# songs = []
#
# soup = BeautifulSoup(html, "html.parser")
# songs_html = soup.find_all(name="li", class_="o-chart-results-list__item // lrv-u-flex-grow-1 lrv-u-flex lrv-u-flex-direction-column lrv-u-justify-content-center lrv-u-border-b-1 u-border-b-0@mobile-max lrv-u-border-color-grey-light lrv-u-padding-l-050 lrv-u-padding-l-1@mobile-max")
#
# songs = [song.find(name="h3").getText().strip() for song in songs_html]
# print(songs)
