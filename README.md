# Vocabulary API

A FastAPI-based REST API for accessing vocabulary data in multiple languages.

## Features

- Get all vocabulary entries
- Get vocabulary by level
- Get all levels
- Support for multiple languages (German, French, English, Ukrainian, Tigrinya, Dari/Farsi)

## Setup

1. Clone the repository:

```bash
git clone <repository-url>
cd progressForgeLangBackend
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory with your database credentials:

```env
DB_HOST=your_host
DB_NAME=your_database
DB_USER=your_user
DB_PASSWORD=your_password
DB_PORT=your_port
```

## Running the Application

Start the server:

```bash
uvicorn src.main:app --reload
```

The server will start at `http://localhost:8000`

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
│   │   ├── __init__.py
│   │   └── schemas.py      # Pydantic models
│   ├── database.py         # Database connection
│   └── api/
│       ├── __init__.py
│       └── routes.py       # API endpoints
├── requirements.txt        # Project dependencies
└── .env                    # Environment variables
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
response = requests.get('http://localhost:8000/vocabulary/b1')

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
  "levelId": "string",
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
