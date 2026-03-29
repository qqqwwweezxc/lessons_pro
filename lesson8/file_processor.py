class FileProcessor:
    """Class representing file processor for write and read in files"""

    @staticmethod
    def write_to_file(file_path: str, data: str) -> None:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(data)

    @staticmethod
    def read_from_file(file_path: str) -> str:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
