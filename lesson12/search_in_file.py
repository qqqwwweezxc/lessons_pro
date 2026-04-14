from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List


def search_in_file(filename: str, target: str) -> List[int]:
    """Searching a target text in file"""

    founded_lines = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, 1):
                if target in line:
                    founded_lines.append(line_number)

    except FileNotFoundError:
        print("File not found!")

    return founded_lines


def search_in_files(files: List[str], target: str) -> dict:
    """Searches for text in multiple files in parallel."""

    results = {}

    with ThreadPoolExecutor(max_workers=len(files)) as executor:
        futures = {
            executor.submit(search_in_file, file, target): file for file in files
        }

        for future in as_completed(futures):
            file = futures[future]
            results[file] = future.result()
        
    return results


if __name__ == "__main__":
    files = ["./lesson12/test_files/test_1.txt", "./lesson12/test_files/test_2.txt"]
    target = "Python"

    result = search_in_files(files, target)

    for file, lines in result.items():
        if lines:
            print(f"{file}: founded target '{target}' in lines {lines}")
        else:
            print(f"{file}: not found")