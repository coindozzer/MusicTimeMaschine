import requests
from datetime import datetime
from bs4 import BeautifulSoup

URL = f"https://www.billboard.com/charts/hot-100/"
desired_date = input(f"Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
lookup_url = f"{URL}/{desired_date}/"

print(lookup_url)

response = requests.get(lookup_url)
html = response.text

soup = BeautifulSoup(html, "html.parser")
print(soup.prettify())