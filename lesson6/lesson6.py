# Напишіть власний ітератор, який буде зчитувати файл у зворотному порядку — рядок за рядком з кінця файлу до початку.
# Це може бути корисно для аналізу лог-файлів, коли останні записи найважливіші.


class ReverseFileIterator:
    """Iterator read the file in reverse order — line by line from the end of the file to the beginning."""

    def __init__(self, filename: str, encoding: str = "utf-8"):
        """
        Initialize file.
        Args:
            filename (str): Path to the file.
            encoding (str): File encoding (default is "utf-8").
        """
        with open(filename, "r", encoding=encoding) as f:
            self.lines = f.readlines()
        self.index = len(self.lines)

    def __iter__(self):
        """Returns the iterator"""
        return self

    def __next__(self):
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

import uuid


class UniqueIdentificatosIterator:
    """An infinite iterator that generates unique identifiers using UUID."""

    def __iter__(self):
        """Returns the iterator"""
        return self

    def __next__(self):
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

import os
import csv
from PIL import Image


class ImageMetadataIterator:
    """
    Iterator that opens each image in turn, extracts metadata from it (size, format) and saves this data to a CSV file.
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
        self.files = [
            os.path.join(directory, f)
            for f in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, f))
        ]
        self.index = 0

        if csv_path:
            with open(csv_path, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["filename", "format", "width", "height"])

    def __iter__(self):
        """Returns the iterator"""
        return self

    def __next__(self):
        while self.index < len(self.files):
            filepath = self.files[self.index]
            self.index += 1

            try:
                with Image.open(filepath) as img:
                    metadata = (
                        os.path.basename(filepath),
                        img.format,
                        img.width,
                        img.height,
                    )

                if self.csv_path:
                    with open(self.csv_path, "a", newline="", encoding="utf-8") as file:
                        writer = csv.writer(file)
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


from contextlib import contextmanager


@contextmanager
def limit_writer(filename: str):
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
