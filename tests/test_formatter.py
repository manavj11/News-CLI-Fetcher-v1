from src.formatter import format_articles

def test_format_articles_output():
    articles = [
        {"title": "News 1", "source": {"name": "Source A"}},
        {"title": "News 2", "source": {"name": "Source B"}}
    ]

    result = format_articles(articles)

    assert "1. News 1 (Source A)" in result
    assert "2. News 2 (Source B)" in result