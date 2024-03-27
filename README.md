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

### Examples

To fetch popular repositories created after January 1, 2024, written in Python, and limited to 10 results:
    ```
    GET /repositories/popular?date=2024-01-01&language=python&limit=10
    ```

To fetch popular repositories without any filters:
    ```
    GET /repositories/popular
    ```

## Testing

To run tests, execute the following command:
    ```
    pytest
    ```
Make sure that the `PYTHONPATH` environment variable is set to the root project folder.