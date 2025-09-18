# Stock Trading App

A comprehensive Python data engineering pipeline for fetching, processing, and analyzing stock market data from Polygon.io API using modern data processing frameworks.

## Architecture

```
Polygon.io API → Python Ingestion → CSV Storage → PySpark Processing → Analytics
```

## Features

### Data Ingestion
- **Real-time API Integration**: Connects to Polygon.io REST API
- **Automatic Pagination**: Handles large datasets with seamless pagination
- **Per-record Streaming**: Saves data incrementally to prevent memory overflow
- **Error Handling**: Robust exception handling for network failures
- **Environment Configuration**: Secure API key management via `.env`

### Data Processing
- **PySpark Integration**: Distributed processing for large datasets
- **Schema Validation**: Enforced data types and structure
- **Data Transformation**: Column cleaning and type conversion
- **Analytics Ready**: Prepared for visualization and analysis

## Technical Stack

| Component | Technology | Purpose |
|-----------|------------|----------|
| API Client | `requests` | HTTP communication |
| Environment | `python-dotenv` | Configuration management |
| Processing | `PySpark` | Distributed data processing |
| Analytics | `pandas`, `matplotlib`, `seaborn` | Data analysis and visualization |
| Storage | CSV | Intermediate data persistence |

## Setup

### Prerequisites
- Python 3.8+
- Java 8+ (for PySpark)
- [uv](https://docs.astral.sh/uv/) package manager
- Polygon.io API key

### Installation
```bash
# Install dependencies with uv
uv sync
```

### Configuration
1. Create `.env` file:
```env
POLYGON_API_KEY=your_polygon_api_key_here
```

2. Get API key from [Polygon.io](https://polygon.io/)

## Usage

### Data Ingestion Pipeline
```bash
python main.py
```

**Process Flow:**
1. Loads environment variables
2. Initializes Polygon API client
3. Fetches initial batch (100 records)
4. Handles pagination automatically
5. Saves each record to `tickers.csv`
6. Provides progress feedback

### Data Processing & Analysis
```bash
jupyter notebook transform.ipynb
```

**Capabilities:**
- Schema enforcement with PySpark
- Data quality validation
- Column transformations
- Statistical analysis
- Data visualization

## Project Structure

```
stock-trading-app/
├── src/
│   ├── __init__.py
│   └── polygon.py          # API client and data persistence
├── main.py                 # Entry point and orchestration
├── transform.ipynb         # PySpark data processing
├── .env                    # Environment configuration
├── tickers.csv            # Output dataset
└── README.md              # Documentation
```

## Data Schema

### Raw API Response
```json
{
  "ticker": "AAPL",
  "name": "Apple Inc.",
  "market": "stocks",
  "locale": "us",
  "primary_exchange": "XNAS",
  "type": "CS",
  "active": true,
  "currency_name": "usd",
  "cik": "0000320193",
  "composite_figi": "BBG000B9XRY4",
  "share_class_figi": "BBG001S5N8V8",
  "last_updated_utc": "2025-09-18T06:05:00Z"
}
```

### PySpark Schema
```python
StructType([
    StructField("ticker", StringType(), True),
    StructField("name", StringType(), True),
    StructField("market", StringType(), True),
    StructField("locale", StringType(), True),
    StructField("primary_exchange", StringType(), True),
    StructField("type", StringType(), True),
    StructField("active", BooleanType(), True),
    StructField("currency_name", StringType(), True),
    StructField("cik", StringType(), True),
    StructField("composite_figi", StringType(), True),
    StructField("share_class_figi", StringType(), True),
    StructField("last_updated_utc", TimestampType(), True)
])
```

## API Integration

### Endpoint
```
GET https://api.polygon.io/v3/reference/tickers
```

### Parameters
- `market=stocks`: Filter for stock market
- `limit=100`: Records per request
- `apiKey`: Authentication token

### Rate Limits
- Free tier: 5 requests/minute
- Paid tiers: Higher limits available

## Error Handling

### Network Errors
- Automatic retry logic
- Graceful degradation
- Connection timeout handling

### Data Validation
- Schema enforcement
- Null value handling
- Type conversion errors

## Performance Considerations

### Memory Management
- Streaming data processing
- Per-record CSV writing
- Pagination to handle large datasets

### Scalability
- PySpark for distributed processing
- Configurable batch sizes
- Horizontal scaling ready

## Monitoring & Logging

- Connection status feedback
- Record count tracking
- Error reporting
- Progress indicators

## Future Enhancements

- [ ] Database integration (PostgreSQL/MongoDB)
- [ ] Real-time streaming with Kafka
- [ ] Docker containerization
- [ ] CI/CD pipeline
- [ ] Data quality metrics
- [ ] Automated testing suite
- [ ] Dashboard integration

## Contributing

1. Fork the repository
2. Create feature branch
3. Add tests for new functionality
4. Submit pull request

## License

MIT License - see LICENSE file for details