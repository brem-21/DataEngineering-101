import requests
import csv
import os

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
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching tickers: {e}")
            return None
        
    def paginate_tickers(self, data):
        """Handle pagination and save per record."""
        if not data or 'results' not in data:
            return []
        
        # Save initial batch per record
        for ticker in data['results']:
            save_to_csv([ticker]).save_to_csv()
        
        # Handle pagination
        while 'next_url' in data:
            try:
                url = data['next_url'] + f"&apiKey={self.api_key}"
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()
                for ticker in data['results']:
                    save_to_csv([ticker]).save_to_csv()
            except requests.exceptions.RequestException as e:
                print(f"Error in pagination: {e}")
                break
        
        return data['results'] if data else []

class save_to_csv:
    """Save tickers to CSV file."""
    def __init__(self, tickers):
        self.tickers = tickers

    def save_to_csv(self):
        """Save tickers to CSV file (append mode for per-record saving)."""
        if not self.tickers:
            return
        
        file_exists = os.path.exists('tickers.csv')
        with open('tickers.csv', 'a', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.tickers[0].keys())
            if not file_exists:
                writer.writeheader()
            for ticker in self.tickers:
                writer.writerow(ticker)