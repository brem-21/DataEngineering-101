import requests
import csv
import os
import time
import json


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
        if not data or "results" not in data:
            return []

        # Save initial batch per record
        print(f"Records in page: {len(data['results'])}")
        for ticker in data["results"]:
            print(json.dumps(ticker, indent=2))
            save_to_csv([ticker]).save_to_csv()

        # Handle pagination with rate limiting
        while "next_url" in data:
            try:
                time.sleep(12)  # Wait 12 seconds (5 requests/minute limit)
                url = data["next_url"] + f"&apiKey={self.api_key}"
                response = requests.get(url)
                response.raise_for_status()
                data = response.json()
                print(f"Records in page: {len(data['results'])}")
                for ticker in data["results"]:
                    print(json.dumps(ticker, indent=2))
                    save_to_csv([ticker]).save_to_csv()
            except requests.exceptions.RequestException as e:
                print(f"Error in pagination: {e}")
                if "429" in str(e):
                    time.sleep(60)  # Wait 1 minute on rate limit
                    continue
                break

        return data["results"] if data else []


class save_to_csv:
    """Save tickers to CSV file."""

    def __init__(self, tickers):
        self.tickers = tickers

    def save_to_csv(self):
        """Save tickers to CSV file (append mode for per-record saving)."""
        if not self.tickers:
            return

        file_exists = os.path.exists("tickers.csv")
        with open("tickers.csv", "a", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.tickers[0].keys())
            if not file_exists:
                writer.writeheader()
            for ticker in self.tickers:
                writer.writerow(ticker)
