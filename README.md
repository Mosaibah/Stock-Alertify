# Stock Alertify

Stock investments provide one of the highest returns in the market. Even though they 
are volatile in nature, one can visualize share prices and other statistical factors, 
which helps keen investors carefully decide on which company they want to spend their 
earnings on.

This project will allow users to retrieve the latest stock market prices and create 
alert rules by setting a threshold price for the stock they are interested in and 
receiving alerts if stocks cross those thresholds.

## Technology used

- Web Server - FastAPI
- ORM - SQLAlchemy
- Database -  cockroachdb
- Scheme Validation - Pydantic


## High-Level Architecture

![high-level.png](images%2Fhigh-level.png)



## Prerequisites

Before you begin, ensure you have met the following requirements:
- Docker and Docker Compose installed on your machine.
- Make sure Docker is running.
- A RapidAPI key. You can obtain one by signing up at [RapidAPI](https://rapidapi.com/).

## Installation

Follow these steps to set up your project locally:

1. Clone the repository:
   ```sh
   git clone https://github.com/Mosaibah/Stock-Alertify.git
   ```
2. Copy the environment variables template to create your own `.env` file:
   ```sh
   cp .env.example .env
   ```
3. Open the `.env` file  and add your RapidAPI key to the RAPID_API_KEY field.
4. Start Docker on your machine.
5. Use the Makefile to build and start docker:
   ```sh
   make up
   ```

## Usage

### Make Commands

Check out this handy list of `make` commands

| Command              | Action                      |
|----------------------|-----------------------------|
| `make up`            | Builds and starts docker compose |
| `make run-api`       | Starts the API server       |
| `make start-consumer`| Starts the consumer         |
| `make start-worker`  | Starts the background worker |
| `make start-beat`    | Starts the beat scheduler   |
| `make publish-event` | Manually publishes an event |


## API Endpoints

This project utilizes FastAPI; you can access the API documentation generated by
FastAPI to test the endpoints. By default, the documentation is available at
http://localhost:8000/docs.

### Available Endpoints

- **Get Market Price**: `GET /market-price/`
  - Summary: Retrieves the current market price.
- **Get Rules**: `GET /rules/`
  - Summary: Fetches all the rules.
- **Create Rule**: `POST /rules/`
  - Summary: Creates a new rule.
- **Update Rule**: `PATCH /rules/{rule_id}`
  - Summary: Updates an existing rule.
- **Delete Rule**: `DELETE /rules/{rule_id}`
  - Summary: Deletes a rule.
- **Alerts**: `GET /alerts/`
  - Summary: Retrieves all alerts.

### Testing the Endpoints

You can test the API endpoints using the FastAPI Swagger UI at
http://localhost:8000/docs. This interface allows you to execute API requests 
directly and view their responses.

## Contributing

Got ideas or found a bug? Feel free to open a PR or an issue. 
All contributions are welcome!

### Connecting with Retool
- work in progress

### Live Demo
- work in progress


[![wakatime](https://wakatime.com/badge/user/57a3d66d-3820-42b8-b270-09f4afc66b0a/project/018e19a3-b324-4f53-90a7-2f36d2654a91.svg)](https://wakatime.com/badge/user/57a3d66d-3820-42b8-b270-09f4afc66b0a/project/018e19a3-b324-4f53-90a7-2f36d2654a91)