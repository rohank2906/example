"""Read a CSV file and return its rows as a list of dictionaries.

This is the golden response for the prompt: "Write a Python function that
reads a CSV file and returns the rows as a list of dictionaries, where the
keys are the column headers from the first row."
"""
import csv
from pathlib import Path


def read_csv(path: str) -> list[dict]:
    """Read *path* as a CSV file and return its rows as a list of dicts.

    The first row of the file is treated as the header. Each subsequent
    row is returned as a dict mapping header name to cell value.

    Args:
        path: Filesystem path to the CSV file.

    Returns:
        List of dicts, one per data row. Returns an empty list if the
        file has no rows or only a header row.

    Raises:
        FileNotFoundError: If *path* does not exist.
    """
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"CSV file not found: {path}")

    rows: list[dict] = []
    with open(file_path, "r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            rows.append(dict(row))
    return rows


if __name__ == "__main__":
    # Smoke test on a small inline example.
    import tempfile

    sample = "name,age,city\nAlice,30,NYC\nBob,25,LA\n"
    with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False) as tmp:
        tmp.write(sample)
        tmp_path = tmp.name

    result = read_csv(tmp_path)
    print(result)
