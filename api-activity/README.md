# CS188 API Activity

A small Flask REST API used to practice HTTP endpoints, HTTPS, SQLite, password hashing, and HTTP Basic Authentication.

## Requirements

- Python 3.12 or newer
- `uv` (recommended) or another Python environment manager
- The local certificate files at the project root:
	- `MyCertificate.crt`
	- `MyKey.pem`

## Setup

From this directory:

```bash
uv sync
source .venv/bin/activate
```

The application uses SQLite. The first request that opens the database creates `activity.db` and its `users` table.

## Run the API

Start the development server with HTTPS:

```bash
uv run api-activity
```

The server runs at `https://127.0.0.1:5000` by default. Because the certificate is local or self-signed, Postman or `curl` may warn that the certificate cannot be verified. Disable certificate verification in the client for local testing only.

To start it from Python without SSL, use:

```bash
uv run python -c "from api_activity.app import run_app; run_app(with_ssl=False)"
```

Note that Flask-Talisman still forces HTTP requests to redirect to HTTPS, so the normal development setup is the HTTPS command above.

## API Endpoints

| Method | Path | Purpose |
| --- | --- | --- |
| `GET` | `/` | Returns a hello-world message. |
| `GET` | `/square/<number>` | Returns the square's area for an integer. |
| `GET` | `/echo?arg1=...&arg2=...` | Returns the supplied query arguments. |
| `PUT` | `/register` | Creates a user and hashes the password before storing it. |
| `GET` | `/profile` | Returns a greeting for an authenticated user. |

### Example requests

```bash
curl -k https://127.0.0.1:5000/
curl -k https://127.0.0.1:5000/square/5
curl -k "https://127.0.0.1:5000/echo?arg1=Hello&arg2=World"
```

Register a user. The form fields are sent as request parameters, not JSON:

```bash
curl -k -X PUT \
	-d "username=testuser" \
	-d "password=testpass123" \
	https://127.0.0.1:5000/register
```

Authenticate with HTTP Basic Auth:

```bash
curl -k -u testuser:testpass123 https://127.0.0.1:5000/profile
```

`/profile` returns `401` when credentials are missing or invalid. A successful registration returns `201`; attempting to register the same username again returns `409`.

## Run Tests

```bash
uv run pytest
```

The tests use Flask's test client, so they do not require the development server to be running.

## Project Layout

```text
src/api_activity/
	app.py          Flask app, routes, HTTPS, and authentication
	db.py           SQLite connection and user persistence
	_constants.py   Project-root path used to locate certificates
tests/test_api.py API tests
MyCertificate.crt Local TLS certificate
MyKey.pem         Local TLS private key
activity.db       Local SQLite database, created at runtime
```

## Postman Notes

For local HTTPS requests, turn off certificate verification in the Postman settings or add the local certificate to Postman's trusted certificates. For `/profile`, select **Authorization > Basic Auth** and provide the username and password created through `/register`.

Do not use the development certificate or the local database for production secrets or deployment.
