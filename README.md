# GitHub Popular Repositories

This project implements a backend application for discovering popular repositories on GitHub.

## Setup

1. Clone this repository.
2. Install Docker if not already installed.
3. Build the Docker container:
    ```
    docker build -t github-popular-repos .
    ```
4. Run the Docker container:
    ```
    docker run -p 5000:5000 github-popular-repos
    ```
5. Access the application at http://localhost:5000/repositories/popular

## API Endpoints

- `/repositories/popular`: Fetches popular repositories from GitHub.

### Query Parameters

- `date` (optional): Filter repositories created from this date onwards (format: YYYY-MM-DD).
- `language` (optional): Filter repositories by programming language.
- `limit` (optional): Limit the number of repositories to return.

## Testing

To run tests, execute the following command:
    ```
    pytest
    ```