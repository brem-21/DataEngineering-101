# DataEngineering-101

A comprehensive learning hub for Data Engineering skills, featuring hands-on projects with Python, SQL, and modern data processing frameworks.

## 🚀 Projects

### Python Data Engineering

#### Stock Trading App
- **Location**: `Python/stock-trading-app/`
- **Description**: Real-time stock data pipeline using Polygon.io API
- **Tech Stack**: Python, PySpark, Pandas, Matplotlib
- **Features**:
  - API integration with automatic pagination
  - Per-record streaming to CSV
  - PySpark data processing and analytics
  - Schema validation and transformations

#### Stream Ingestion
- **Location**: `Python/Stream_Ingestion/`
- **Description**: Real-time data streaming and processing
- **Tech Stack**: Python, SQLite
- **Features**: Live data ingestion and storage

#### Python Fundamentals
- **Location**: `Python/Start.ipynb`
- **Description**: Complete Python programming tutorial
- **Topics**: Syntax, data types, functions, OOP, error handling

### SQL Data Engineering

#### NY Taxi Data Pipeline
- **Location**: `SQL/`
- **Description**: PostgreSQL data pipeline for NYC taxi data
- **Tech Stack**: PostgreSQL, Docker
- **Features**:
  - Dockerized PostgreSQL setup
  - Data modeling and table generation
  - Large dataset processing

## 🛠️ Tech Stack

| Technology | Purpose | Projects |
|------------|---------|----------|
| **Python** | Core programming | All projects |
| **PySpark** | Distributed processing | Stock Trading App |
| **PostgreSQL** | Relational database | NY Taxi Pipeline |
| **Docker** | Containerization | SQL projects |
| **Pandas** | Data manipulation | Stock Trading App |
| **Matplotlib/Seaborn** | Visualization | Stock Trading App |
| **SQLite** | Lightweight database | Stream Ingestion |
| **Jupyter** | Interactive development | All notebooks |
| **uv** | Package management | All projects |

## 🚦 Getting Started

### Prerequisites
- Python 3.11+
- [uv](https://docs.astral.sh/uv/) package manager
- Docker (for SQL projects)
- Java 8+ (for PySpark)

### Installation
```bash
# Clone repository
git clone <repository-url>
cd DataEngineering-101

# Install dependencies
uv sync

# Activate virtual environment
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate     # Windows
```

### Quick Start
```bash
# Run Python fundamentals
jupyter notebook Python/Start.ipynb

# Start stock trading app
cd Python/stock-trading-app
python main.py

# Launch SQL environment
cd SQL
docker-compose up -d
```

## 📁 Project Structure

```
DataEngineering-101/
├── Python/
│   ├── stock-trading-app/          # Real-time stock data pipeline
│   │   ├── src/polygon.py          # API client
│   │   ├── main.py                 # Entry point
│   │   ├── transform.ipynb         # PySpark processing
│   │   └── README.md               # Project documentation
│   ├── Stream_Ingestion/           # Streaming data project
│   │   ├── stream.ipynb            # Stream processing
│   │   └── rides.db                # SQLite database
│   └── Start.ipynb                 # Python fundamentals
├── SQL/
│   ├── ny_taxi_postgres_data/      # NYC taxi dataset
│   ├── docker-compose.yaml         # PostgreSQL setup
│   └── generate_table.sql          # Database schema
├── pyproject.toml                  # Dependencies
├── uv.lock                         # Lock file
└── README.md                       # This file
```

## 🎯 Learning Path

### Beginner
1. **Python Fundamentals** (`Python/Start.ipynb`)
   - Basic syntax and data types
   - Control structures and functions
   - Object-oriented programming

### Intermediate
2. **Data Processing** (`Python/stock-trading-app/`)
   - API integration
   - Data transformation with Pandas
   - CSV file operations

3. **Database Operations** (`SQL/`)
   - PostgreSQL setup with Docker
   - SQL queries and data modeling
   - Large dataset handling

### Advanced
4. **Distributed Processing** (`Python/stock-trading-app/transform.ipynb`)
   - PySpark fundamentals
   - Schema enforcement
   - Data analytics at scale

5. **Real-time Streaming** (`Python/Stream_Ingestion/`)
   - Stream processing concepts
   - Real-time data ingestion
   - Database integration

## 🔧 Development

### Package Management
- **Tool**: uv (ultra-fast Python package installer)
- **Configuration**: `pyproject.toml`
- **Lock file**: `uv.lock` for reproducible builds
- **Virtual environment**: Automatic `.venv` creation

### Dependencies
- **Core**: pandas, requests, python-dotenv
- **Processing**: pyspark
- **Visualization**: matplotlib, seaborn
- **Development**: jupyter, black, ipykernel

### Code Quality
- **Formatting**: Black code formatter
- **Environment**: Python 3.11+

## 📊 Key Features

### Data Pipeline Capabilities
- **Real-time API integration** with error handling
- **Distributed processing** with PySpark
- **Schema validation** and type enforcement
- **Incremental data loading** and pagination
- **Containerized databases** with Docker

### Analytics & Visualization
- **Statistical analysis** with Pandas
- **Data visualization** with Matplotlib/Seaborn
- **Interactive notebooks** for exploration
- **Performance monitoring** and logging

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎓 Learning Resources

- **Python**: Official Python documentation
- **PySpark**: Apache Spark documentation
- **PostgreSQL**: PostgreSQL official docs
- **Docker**: Docker getting started guide
- **Data Engineering**: Industry best practices and patterns