import requests

//API_KEY = "5e0f050c0fb2445b9625c76fc3112ee7"
URL = "https://newsapi.org/v2/top-headlines"

def fetch_news(topic):
    """
    Fetch news articles from the API.
    Raises exception if API fails.
    """
    params = {
        "apiKey": API_KEY,
        "category": topic,
        "country": "us"
    }

    response = requests.get(URL, params=params)

    # Error handling for bad response
    if response.status_code != 200:
        raise Exception("API request failed")

    data = response.json()

    if "articles" not in data:
        raise Exception("Invalid API response")

    return data["articles"]
