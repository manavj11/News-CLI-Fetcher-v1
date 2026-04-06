# News CLI Fetcher v1

## Overview

This is a command-line Python application that fetches news articles from a public News API based on a topic provided by the user. The application demonstrates API integration, error handling, logging, and automated testing.

## Features

* Fetch news by topic
* Format and display top headlines
* Save results to a file
* Error handling for API and file issues
* Logging for debugging
* Unit tests with mocked API responses
* GitHub Actions CI to run tests automatically

## How to Run

```bash
python main.py --topic technology
```

## How to Run Tests

```bash
PYTHONPATH=. pytest
```

## Project Structure

* `src/` → Application code
* `tests/` → Unit tests
* `main.py` → Entry point
* `.github/workflows/` → CI pipeline

## Skills Demonstrated

API usage, testing, debugging, error handling, logging, CI/CD.
