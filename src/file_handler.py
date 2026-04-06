def save_to_file(filename, content):
    """
    Save content to a file with error handling.
    """
    try:
        with open(filename, "w") as file:
            file.write(content)
    except IOError:
        raise Exception("Failed to write to file")