import os
from dotenv import load_dotenv
from src.polygon import polygon, save_to_csv

load_dotenv()

limit = 100
API_KEY = os.getenv('POLYGON_API_KEY')
url = f"https://api.polygon.io/v3/reference/tickers?market=stocks&limit={limit}&apiKey={API_KEY}"

try:
    get_data = polygon(url=url, api_key=API_KEY, limit=limit)
    print("Connection successful")
except Exception as e:
    print(f"Connection failed: {e}")
else:
    data = get_data.fetch_tickets()
    if data:
        get_data.paginate_tickers(data)
        print("All tickers saved per record to tickers.csv")
finally:
    print("Connection closed")

