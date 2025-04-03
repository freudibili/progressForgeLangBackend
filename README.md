# Vocabulary API

A FastAPI-based REST API for accessing vocabulary data in multiple languages.

## Features

- Get all vocabulary entries
- Get vocabulary by level
- Search vocabulary by word
- Get vocabulary by word type
- Get specific vocabulary entry by ID
- Support for multiple languages (German, French, English, Ukrainian, Tigrinya, Dari/Farsi)

## Setup

1. Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the server:

```bash
python main.py
```

The server will start at `http://localhost:8000`

## API Endpoints

### Root

- `GET /`: Welcome message

### Vocabulary

- `GET /vocabulary`: Get all vocabulary entries
- `GET /vocabulary/{level_id}`: Get vocabulary entries for a specific level
- `GET /vocabulary/search/{word}`: Search vocabulary entries by word
- `GET /vocabulary/type/{word_type}`: Get vocabulary entries by word type
- `GET /vocabulary/entry/{entry_id}`: Get a specific vocabulary entry by ID

## API Documentation

Once the server is running, you can access:

- Interactive API documentation: `http://localhost:8000/docs`
- Alternative API documentation: `http://localhost:8000/redoc`

## Example Usage

```python
import requests

# Get all vocabulary
response = requests.get('http://localhost:8000/vocabulary')

# Get vocabulary for a specific level
response = requests.get('http://localhost:8000/vocabulary/b1')

# Search for a word
response = requests.get('http://localhost:8000/vocabulary/search/hello')

# Get vocabulary by type
response = requests.get('http://localhost:8000/vocabulary/type/noun')

# Get specific entry
response = requests.get('http://localhost:8000/vocabulary/entry/123')
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
