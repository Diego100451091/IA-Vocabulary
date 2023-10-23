import json

def read_json_file(filepath):
    """
    Reads a JSON file and returns its contents as a Python object.

    Args:
        filepath (str): The path to the JSON file to be read.

    Returns:
        dict: A dictionary containing the contents of the JSON file.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def write_json_file(filepath, data):
    """
    Write data to a JSON file at the specified filepath.

    Args:
        filepath (str): The path to the file to write.
        data (dict): The data to write to the file.

    Returns:
        None
    """
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
