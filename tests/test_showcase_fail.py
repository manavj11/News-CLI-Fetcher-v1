from src.formatter import format_articles

def test_format_articles_failure_demo():
    articles = [
        {"title": "News 1", "source": {"name": "Source A"}}
    ]

    result = format_articles(articles)

    # Intentionally wrong expectation
    assert result == "Wrong Output"