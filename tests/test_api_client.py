from src.api_client import fetch_news
from unittest.mock import patch

@patch("src.api_client.requests.get")
def test_fetch_news_success(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "articles": [{"title": "Test News", "source": {"name": "Test Source"}}]
    }

    articles = fetch_news("technology")
    assert len(articles) == 1
    assert articles[0]["title"] == "Test News"