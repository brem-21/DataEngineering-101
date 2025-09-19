"""Main module to run the stock trading app."""

import os
from dotenv import load_dotenv
from src.polygon import polygon

load_dotenv()

LIMIT = 100
API_KEY = os.getenv("POLYGON_API_KEY")
URL = f"https://api.polygon.io/v3/reference/tickers?market=stocks&limit={LIMIT}&apiKey={API_KEY}"

try:
    get_data = polygon(url=URL, api_key=API_KEY, limit=LIMIT)
    print("Connection successful")
except ConnectionError as e:
    print(f"Connection failed: {e}")
else:
    data = get_data.fetch_tickets()
    if data:
        get_data.paginate_tickers(data)
        print("All tickers saved per record to tickers.csv")
finally:
    print("Connection closed")
