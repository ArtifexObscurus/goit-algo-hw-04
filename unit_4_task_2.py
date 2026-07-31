from pathlib import Path

def get_cats_info(path: str | Path) -> list[dict[str, str | int]]:
    """
    Read cat information from a text file.

    The input file must contain one cat per line in the following format:
        id,name,age

    Args:
        path: Path to the text file containing cat information.

    Returns:
        A list of dictionaries, where each dictionary contains:
            - "id" (str): The cat's unique identifier.
            - "name" (str): The cat's name.
            - "age" (int): The cat's age.

        Returns an empty list if the file cannot be processed.
    """
    path = Path(path)

    cats = []

    try:
        with open(path, "r", encoding="utf=8") as file:
            for line in file:
                cat_id, name, age = line.strip().split(",")

                cats.append(
                    {
                        "id": cat_id,
                        "name": name,
                        "age": int(age),
                    }
                )

        return cats

    except FileNotFoundError:
        print(f"Error: File '{path}' was not found.")
        return []

    except (ValueError, IndexError):
        print("Error: Invalid file format.")
        return []
