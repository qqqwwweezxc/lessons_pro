# Напишіть власний ітератор, який буде зчитувати файл у зворотному порядку — рядок за рядком з кінця файлу до початку.
# Це може бути корисно для аналізу лог-файлів, коли останні записи найважливіші.
import uuid
import os
import csv
from PIL import Image
from contextlib import contextmanager
import json
import zipfile


class ReverseFileIterator:
    """Iterator read the file in reverse order — line by line from the end of the file to the beginning."""

    def __init__(self, filename: str, encoding: str = "utf-8") -> None:
        """
        Initialize file.
        Args:
            filename (str): Path to the file.
            encoding (str): File encoding (default is "utf-8").
        """
        with open(filename, "r", encoding=encoding) as f:
            self.lines: list[str] = f.readlines()
        self.index: int = len(self.lines)

    def __iter__(self) -> "ReverseFileIterator":
        """Returns the iterator"""
        return self

    def __next__(self) -> str:
        """Return the next line from the end of the file."""
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.lines[self.index].rstrip()


reversefile = ReverseFileIterator("./lesson6/test.txt", "utf-8")
for line in reversefile:
    print(line)

# Створіть ітератор, який генерує унікальні ідентифікатори (наприклад, на основі UUID або хеш-функції).
#  Ідентифікатори повинні генеруватися один за одним при кожній ітерації, і бути унікальними.


class UniqueIdentificatosIterator:
    """An infinite iterator that generates unique identifiers using UUID."""

    def __iter__(self) -> "UniqueIdentificatosIterator":
        """Returns the iterator"""
        return self

    def __next__(self) -> str:
        """
        Generate and return the next unique identificator.
        Returns:
            A unique UUID string.
        """
        return str(uuid.uuid4())


uniqueid = UniqueIdentificatosIterator()
for _ in range(5):
    print(next(uniqueid))

# У вас є каталог з великою кількістю зображень. Напишіть ітератор, який по черзі відкриває кожне зображення
# (наприклад, за допомогою модуля PIL), витягує з нього метадані (розмір, формат тощо) і зберігає ці дані у файл CSV.


class ImageMetadataIterator:
    """
    Iterator that opens each image in turn, extracts metadata from it (size, format) and saves this data to a CSV file.

    Attributes:
        directory (str): Path to the directory containing images.
        csv_path (str | None): Path to the CSV file where metadata will be saved.
        files (list[str]): List of file paths found in the directory.
        index (int): Current position of the iterator.
    """

    def __init__(self, directory: str, csv_path: str = None) -> None:
        """
        Initialize the iterator.

        Args:
            directory (str): Path to the directory with images.
            csv_path (str): Optional path to a CSV file to save metadata.
        """

        self.directory = directory
        self.csv_path = csv_path
        self.files: list[str] = [
            os.path.join(directory, f)
            for f in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, f))
        ]
        self.index: int = 0

        if csv_path:
            with open(csv_path, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["filename", "format", "width", "height"])

    def __iter__(self) -> "ImageMetadataIterator":
        """Returns the iterator"""
        return self

    def __next__(self) -> tuple[str, str, int, int]:
        """
        Returns metadata of the next image.

        Returns: tuple[str, str, int, int]: (filename, format, width, height)
        """
        while self.index < len(self.files):
            filepath: str = self.files[self.index]
            self.index += 1

            try:
                with Image.open(filepath) as img:
                    metadata: tuple[str, str, int, int] = (
                        os.path.basename(filepath),
                        img.format,
                        img.width,
                        img.height,
                    )

                if self.csv_path:
                    with open(self.csv_path, "a", newline="", encoding="utf-8") as file:
                        writer: object = csv.writer(file)
                        writer.writerow(metadata)

                return metadata

            except (OSError, ValueError):
                continue

        raise StopIteration


metadata = ImageMetadataIterator("./lesson6/images", "./lesson6/metadata.csv")
for meta in metadata:
    print(meta)

# Реалізуйте генератор, який читає великий текстовий файл рядок за рядком (наприклад, лог-файл) і
# повертає лише ті рядки, що містять певне ключове слово. Використайте цей генератор для фільтрації файлу та запису
# відповідних рядків у новий файл.


def filter_generator(filename: str, keyword: str):
    """
    Generator that reads a large text file line by line and returns only those lines that contain a keyword
    """
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            if keyword in line:
                yield line


with open("./lesson6/filtered.txt", "w", encoding="utf-8") as file:
    for line in filter_generator("./lesson6/test.txt", "number"):
        print(line.strip())
        file.write(line)

# Створіть генератор, який генерує нескінченну послідовність парних чисел.
# Використайте менеджер контексту для обмеження кількості генерованих чисел до 100 і збереження їх у файл.


def even_numbers():
    """Infinity generator even numbers"""
    num = 0
    while True:
        yield num
        num += 2


@contextmanager
def limit_writer(filename: str) -> object:
    """Custom context manager for limit a function generator"""
    with open(filename, "w", encoding="utf-8") as file:
        yield file


gen = even_numbers()

with limit_writer("./lesson6/even_numbers.txt") as file:
    for i, num in enumerate(gen):
        if i >= 100:
            break
        file.write(f"{num}\n")

# Напишіть ітератор, який буде повертати всі файли в заданому каталозі по черзі. Для кожного файлу виведіть його назву та розмір.


class FilesIterator:
    """
    Iterator which will return all files in the given directory one by one. For each file it prints its name and size

    Attributes:
        directory (str): Path to the directory containing files.
        files (list[str]): List of file paths found in the directory.
        index (int): Current position of the iterator.
    """

    def __init__(self, directory: str) -> None:
        """
        Initialize the iterator.

        Args:
            directory (str): Path to the directory with files.
        """
        self.directory: str = directory
        self.files: list[str] = [
            os.path.join(directory, f)
            for f in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, f))
        ]
        self.index: int = 0

    def __iter__(self) -> "FilesIterator":
        """Returns the iterator"""
        return self

    def __next__(self):
        """ """
        while self.index < len(self.files):
            filepath: str = self.files[self.index]
            self.index += 1

            try:
                file_name: str = os.path.basename(filepath)
                file_size_bytes: int = os.path.getsize(filepath)
                file_size_kb: float = file_size_bytes / 1024
                return f"File name: {file_name}, file size {round(file_size_kb, 3)} kb"

            except (OSError, ValueError):
                continue

        raise StopIteration


check_directory = FilesIterator("./lesson6/images")
for file in check_directory:
    print(file)


# Уявіть, що у вас є великий лог-файл від веб-сервера. Створіть генератор, який зчитує файл порціями (по рядку)
# і повертає тільки рядки з помилками (код статусу 4XX або 5XX). Запишіть ці помилки в окремий файл для подальшого аналізу.


def errors_generator(filename: str):
    """Generator that reads a file and returns only lines with errors (status code 4XX or 5XX)"""
    with open(filename) as file:
        for line in file:
            parts: list[str] = line.split()

            for part in parts:
                if part.isdigit():
                    status_code: int = int(part)
                    if 400 <= status_code < 600:
                        yield line
                        break


with open("./lesson6/errors.txt", "w", encoding="utf-8") as file:
    for line in errors_generator("./lesson6/log_file.txt"):
        print(line.strip())
        file.write(line)

# Напишіть власний контекстний менеджер для роботи з файлом конфігурацій (формат .ini або .json).
# Менеджер має автоматично зчитувати конфігурацію при вході в контекст і записувати зміни в файл після завершення роботи.


@contextmanager
def config_manager(filename: str) -> object:
    """
    Custom context manager for work with json konfigs
    Reads the configuration at the entrance, records changes when leaving
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            config: dict = json.load(file)
    except FileNotFoundError:
        config: dict = {}
    except json.JSONDecodeError:
        raise ValueError(f"File {filename} have incorrect JSON")

    yield config

    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(config, file, indent=4, ensure_ascii=False)
    except Exception as error:
        print(f"Error when writing a file: {error}")


with config_manager("./lesson6/config.json") as cfg:
    cfg["theme"] = "dark"
    cfg["volume"] = 100
    print(cfg)

# Напишіть менеджер контексту, який буде створювати резервну копію важливого файлу перед його обробкою.
# Якщо обробка пройде успішно, оригінальний файл замінюється новим. У разі помилки резервна копія автоматично відновлюється.


@contextmanager
def reserve_copy_file(filename: str):
    """Custom context manager that creates a backup before file processing."""

    name, ext = os.path.splitext(filename)
    backup_path: str = name + "_backup" + ext

    with open(filename, "rb") as original_file:
        backup_data: bytes = original_file.read()

    with open(backup_path, "wb") as backup_file:
        backup_file.write(backup_data)

    try:
        yield filename

        os.remove(backup_path)

    except Exception as error:
        with open(backup_path, "rb") as backup_file:
            backup_data = backup_file.read(backup_path)

        with open(filename, "wb") as original_file:
            original_file.write(backup_data)

        os.remove(backup_path)
        print(f"Error: {error}. File restored")


with reserve_copy_file("./lesson6/test_file.txt") as file:
    with open(file, "w", encoding="utf-8") as f:
        f.write("Something new...")
        # raise ValueError("Test")

# Реалізуйте менеджер контексту для архівування файлів (за допомогою модуля zipfile). Менеджер автоматично створює
# архів, додає файли, а після виходу з блоку with – завершує архівування та закриває архів.


@contextmanager
def archive_files(archive_name: str):
    """Custom context manage that crates a zip-archive and managing it"""

    archive: zipfile.ZipFile = zipfile.ZipFile(
        archive_name, "w", compression=zipfile.ZIP_DEFLATED
    )

    def add_file(filename: str) -> None:
        archive.write(filename)
        print("File succesfuly added!")

    try:
        yield add_file

    finally:
        archive.close()


with archive_files("./lesson6/test.zip") as add:
    add("./lesson6/test_file.txt")
    add("./lesson6/log_file.txt")

# Напишіть генератор, який по черзі зчитує великий файл даних (наприклад, числові показники продуктивності), обчислює
# середнє значення на кожній ітерації та оновлює результат. Це корисно для обробки великих даних, які не можна завантажити
# повністю в пам'ять.


def average_generator(filename: str):
    """Generator that reads a file and returns only lines with errors (status code 4XX or 5XX)"""

    total: int = 0
    count: int = 0

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            if not line:
                continue
            for part in line.split():
                if part.isdigit():
                    total += int(part)
                    count += 1
                    yield total / count


for avg in average_generator("numbers.txt"):
    print(f"Average = {avg}")


# Напишіть програму, яка використовує менеджер контексту для зчитування бінарних файлів великими блоками даних
# (наприклад, по 1024 байти). Виведіть кількість прочитаних байт.


def read_binary_file(filename: str, chunk_size: int = 1024) -> int:
    """Reads binary file and returns total bytes read"""
    total_bytes = 0

    with open(filename, "rb") as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            total_bytes += len(chunk)

    return total_bytes


print("Total bytes readed in file: ", read_binary_file("./lesson6/test.bin"))
