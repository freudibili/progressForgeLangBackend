# Vocabulary API

A FastAPI-based REST API for accessing vocabulary data in multiple languages.

## Features

- Get all vocabulary entries
- Get vocabulary by level
- Get all levels
- Support for multiple languages (German, French, English, Ukrainian, Tigrinya, Dari/Farsi)

## Setup

### Prerequisites

- Docker
- Docker Compose

### Running the Application

1. Clone the repository:

```bash
git clone <repository-url>
cd progressForgeLangBackend
```

2. Start the containers:

```bash
docker-compose up --build
```

The API will be available at `http://localhost:8000`

### Docker Commands

- Start containers: `docker-compose up`
- Start in detached mode: `docker-compose up -d`
- Stop containers: `docker-compose down`
- Rebuild and start: `docker-compose up --build`
- View logs: `docker-compose logs -f`

## API Endpoints

### Root

- `GET /`: Welcome message

### Vocabulary

- `GET /vocabulary`: Get all vocabulary entries (optional limit parameter)
- `GET /vocabulary/{level_id}`: Get vocabulary entries for a specific level

### Levels

- `GET /levels`: Get all available levels

## API Documentation

Once the server is running, you can access:

- Interactive API documentation: `http://localhost:8000/docs`
- Alternative API documentation: `http://localhost:8000/redoc`

## Project Structure

```
project/
├── src/
│   ├── __init__.py
│   ├── main.py              # FastAPI app setup
│   ├── models/
│   │   ├── __init__.py
│   │   └── schemas.py      # Pydantic models
│   ├── database.py         # Database connection
│   └── api/
│       ├── __init__.py
│       └── routes.py       # API endpoints
├── requirements.txt        # Project dependencies
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Docker Compose configuration
├── my_postgres_backup.sql # Database initialization
└── .env                   # Environment variables
```

## Dependencies

- FastAPI
- Uvicorn
- psycopg2-binary
- python-dotenv
- pydantic

## Example Usage

```python
import requests

# Get all vocabulary
response = requests.get('http://localhost:8000/vocabulary')

# Get vocabulary for a specific level
response = requests.get('http://localhost:8000/vocabulary/2a6ca7bd-b274-44d9-aebb-4eb60885908d')

# Get all levels
response = requests.get('http://localhost:8000/levels')
```

## Data Structure

Each vocabulary entry has the following structure:

```json
{
  "id": "string",
  "infinitiv": {
    "de": "string",
    "fr": "string",
    "en": "string",
    "uk": "string",
    "er": "string",
    "af": "string"
  },
  "level_id": "string",
  "type": "string",
  "example": {
    "de": "string",
    "fr": "string",
    "en": "string",
    "uk": "string",
    "er": "string",
    "af": "string"
  }
}
```
