def format_articles(articles):
    """
    Format articles into readable text.
    """
    if not articles:
        return "No articles found."

    output = ""
    # Show only first 5 articles for readability
    for i, article in enumerate(articles[:5], start=1):
        title = article.get("title", "No title")
        source = article.get("source", {}).get("name", "Unknown source")

        output += f"{i}. {title} ({source})\n"

    return output