from src.file_handler import save_to_file

def test_save_to_file(tmp_path):
    file_path = tmp_path / "test.txt"

    save_to_file(file_path, "Hello World")

    content = file_path.read_text()
    assert content == "Hello World"