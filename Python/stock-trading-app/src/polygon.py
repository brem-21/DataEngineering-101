import requests
import csv

class polygon:
    """Ingestion of stock ticker data from Polygon.io API."""
    def __init__(self, url, api_key, limit):
        self.url = url
        self.api_key = api_key
        self.limit = limit

    def fetch_tickets(self):
        """Fetch tickers from Polygon.io API."""
        try:
            response = requests.get(self.url)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching tickers: {e}")
            return None
        else:
            tickers = []
            data = response.json()
            for ticker in data['results']:
                tickers.append(ticker)
        finally:
            print("Fetching tickers complete.")
        
    def paginate_tickers(self, data):
        """Handle pagination for fechting tickers."""
        tickers = []
        try:
            response = requests.get(self.url)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching tickers: {e}")
            return None
        else:
            data = response.json()
            for ticker in data['results']:
                tickers.append(ticker)
            while 'next_url' in data:
                    print('requesting next page')
                    url = data['next_url'] + f"&apiKey={self.api_key}"
                    response = requests.get(url)
                    data = response.json()
                    print(data)
                    for ticker in data['results']:
                        tickers.append(ticker)

class save_to_csv:
    """Save tickers to CSV file."""
    def __init__(self, tickers):
        self.tickers = tickers

    def save_to_csv(self):
        """Save tickers to CSV file."""
        with open('tickers.csv', 'w', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=self.tickers[0].keys())
            writer.writeheader()
            for ticker in self.tickers:
                writer.writerow(ticker)
        print("Tickers saved to CSV file.")