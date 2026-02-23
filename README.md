# py-ha-rest

A simple FastAPI-based REST server providing an echo endpoint.

## Features

- **Echo Endpoint**: Send a message and get it back in the response.

## Prerequisites

- Python 3.7+

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/jules256/py-ha-rest.git
   cd py-ha-rest
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To start the server, use `uvicorn`:

```bash
uvicorn main:app --reload
```

The server will be available at `http://127.0.0.1:8000`.

## API Documentation

### Echo

Returns the provided message.

- **URL**: `/echo`
- **Method**: `GET`
- **Query Parameters**:
  - `message` (string, required): The message to echo.

#### Example Request

```bash
curl "http://127.0.0.1:8000/echo?message=Hello+World"
```

#### Example Response

```json
{
  "message": "Hello World"
}
```

## Running Tests

To run the tests, use `pytest`:

```bash
pytest
```

## License

This project is licensed under the GNU Affero General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
