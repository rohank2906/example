# Prompt

Write a Python function that reads a CSV file from disk and returns its rows as a list of dictionaries, where the keys of each dictionary are the column headers from the file's first row.

## Requirements

1. The function must be named `read_csv` and take a single argument `path` of type `str`.
2. The function must return a value of type `list[dict]`.
3. The function must use the standard library `csv` module — do not use pandas or any third-party library.
4. The first row of the file must be treated as the header row, not as data.
5. If the file does not exist, the function must raise `FileNotFoundError` with a message that includes the path.
6. The file must be opened with `encoding="utf-8"` and `newline=""`.
7. The file handle must be closed cleanly even if an exception is raised mid-read (use a `with` block).

## Constraints

- Do not print to stdout from inside the function.
- Do not include logging.
- Keep the implementation under 30 lines, excluding the docstring.
- Include a Google-style docstring covering Args, Returns, and Raises.

## Format

- Submit a single file named `golden_response.py`.
- Include an `if __name__ == "__main__":` block that demonstrates the function on a small inline CSV sample (3 rows, 3 columns) and prints the result.

## Audience

The reader is an intermediate Python developer who is comfortable with the standard library but may not have used `csv.DictReader` before. Comments are not required, but the docstring should be clear enough that the reader can use the function without reading the implementation.
