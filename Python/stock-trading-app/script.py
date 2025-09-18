import requests
import os
from dotenv import load_dotenv

load_dotenv()
limit = 1000

API_KEY = os.getenv('POLYGON_API_KEY')

url = f"https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&order=asc&limit={limit}&sort=ticker&apiKey={API_KEY}"

response = requests.get(url)
tickers = []

data = response.json()
for ticker in data['results']:
    tickers.append(ticker)

while 'next_url' in data:
    print('requesting next page')
    url = data['next_url'] + f"&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    for ticker in data['results']:
        tickers.append(ticker)