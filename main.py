from src.api_client import fetch_news
from src.formatter import format_articles
from src.file_handler import save_to_file
import logging
import argparse

# Setup logging
logging.basicConfig(level=logging.INFO)

def main():
    parser = argparse.ArgumentParser(description="Fetch news by topic")
    parser.add_argument("--topic", type=str, required=True, help="News topic")
    args = parser.parse_args()

    try:
        # Fetch news from API
        articles = fetch_news(args.topic)

        # Format articles for display
        formatted = format_articles(articles)

        # Print to console
        print(formatted)

        # Save to file
        save_to_file("news.txt", formatted)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        print("Something went wrong. Check logs.")

if __name__ == "__main__":
    main()