# News CLI Fetcher v1

## Overview

This is a command-line Python application that fetches news articles from a public News API based on a topic provided by the user. The application demonstrates API integration, error handling, logging, and automated testing.

## Features

* Fetch top headlines by news category from NewsAPI
* Format articles in readable numbered list with source attribution
* Save formatted results to `news.txt` file
* Comprehensive error handling for API failures and file I/O issues
* Structured logging to `app.log` for debugging and monitoring
* Full test coverage with mocked API responses
* Automated CI pipeline with GitHub Actions

## Setup

Install dependencies:
```bash
pip install -r requirements.txt
```

## How to Run

Fetch top headlines for a specific category (e.g., technology, business, sports):
```bash
python main.py --topic technology
```

Results are displayed in the console and saved to `news.txt` in format: `1. Article Title (Source Name)`

## How to Run Tests

```bash
PYTHONPATH=. pytest
```

## Project Structure

```
src/
├── api_client.py      # NewsAPI integration and article fetching
├── formatter.py       # Format articles for display
├── file_handler.py    # File I/O operations
└── logger.py          # Application logging setup

tests/                 # Unit tests with mocked API responses
main.py               # Application entry point and orchestration
requirements.txt      # Python package dependencies
```

## Skills Demonstrated

* **API Integration**: RESTful API calls with request parameters and response parsing
* **Error Handling**: Exception handling for network failures and invalid responses
* **File I/O**: Reading and writing files with proper error handling
* **Logging**: Structured logging with timestamps and severity levels
* **Testing**: Unit tests with mocking for external dependencies
* **CI/CD**: Automated testing with GitHub Actions workflows
