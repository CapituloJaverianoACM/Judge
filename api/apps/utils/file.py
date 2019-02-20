

def get_data_from_file(
        *,
        file_path: str
) -> str:

    with open(file_path, "r") as f:
        try:
            data = f.read()
        except Exception:
            data = "Not file"
    return data
