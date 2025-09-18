import os
from dotenv import load_dotenv
from src.polygon import polygon, save_to_csv

load_dotenv()

limit = 1000
API_KEY = os.getenv('POLYGON_API_KEY')
url = f"https://api.polygon.io/v3/reference/tickers?market=stocks&limit={limit}&apiKey={API_KEY}"

try:
    get_data = polygon(url=url, api_key=API_KEY, limit=limit)
    print("Connection successful")
except Exception as e:
    print(f"Connection failed: {e}")
else:
    data = get_data.fetch_tickets()
    tickers = get_data.paginate_tickers(data)
    print(tickers)
    records = len(tickers)
    print(f"Total tickers fetched: {records}")

    # Handle pagination if records exceed limit
    if records > limit and 'next_url' in data:
        get_data.paginate_tickers(data)
        print(f"Total tickers after pagination: {len(tickers)}")
        save = save_to_csv(tickers)
finally:
    print("Connection closed")

