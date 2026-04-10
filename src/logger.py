import logging

def setup_logger():
    logging.basicConfig(
        filename="app.log",
        level=logging.INFO,  # Log INFO and higher severity (WARN, ERROR, CRITICAL)
        format="%(asctime)s - %(levelname)s - %(message)s"
    )