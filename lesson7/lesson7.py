# Встанови пакет requests за допомогою pip.
# Напиши скрипт, який завантажує сторінку з вказаного URL та зберігає її вміст у текстовий файл.
# Додай обробку помилок на випадок, якщо сторінка недоступна.

import requests
import csv
import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
import re

def download_page(url: str, filename: str) -> None:
    """Function loads the page from the specified URL and saves its contents to a text file"""

    try:
        response = requests.get(url, timeout=10)

        response.raise_for_status()

        with open(filename, "w", encoding="utf-8") as file:
            file.write(response.text)

        print(f"File succesfully saved to: {filename}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")

    except requests.exceptions.ConnectionError:
        print("Connection error. Check your internet or URL.")

    except requests.exceptions.Timeout:
        print("The request timed out.")

    except requests.exceptions.RequestException as error:
        print(f"Error: {error}")


# download_page("https://lms.ithillel.ua/", "./lesson7/page.txt")

# Створи CSV-файл з даними про студентів, де кожен рядок містить:
# Ім'я студента
# Вік
# Оцінку
# Напиши програму, яка:
# Читає дані з CSV-файлу.
# Виводить середню оцінку студентів.
# Додає нового студента до файлу.


def read_students(filename: str) -> list:
    students = []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                name, age, grade = row
                students.append({
                    "name": name,
                    "age": int(age),
                    "grade": float(grade)
                })
    except FileNotFoundError:
        print("File not found!")
    return students

def calculate_average(students: list) -> float:
    if not students:
        return 0
    total = sum(student["grade"] for student in students)
    return total / len(students)

def add_student(filename: str) -> None:
    name = input("Enter the name for add student: ")
    age = int(input("Enter his age: "))
    grade = int(input("Enter his grade: "))
    try:
        with open(filename, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([name, age, grade])
            print(f"Student {name} sucessfuly added!")
    except FileNotFoundError:
        print("File not found!")

def main_csv() -> None:
    filename: str = "./lesson7/students.csv"
    students: list = read_students(filename)
    average: float = calculate_average(students)
    print(f"Average grade: {average}")
    choice: str = input("Do yo want to add new student? (y/n): ")
    if choice.lower() == "y":
        add_student(filename)

# main_csv()

# Створи JSON-файл з інформацією про книги, кожна книга повинна мати:
# Назву
# Автора
# Рік видання
# Наявність (True або False)
# Напиши програму, яка:
# Завантажує JSON-файл.
# Виводить список доступних книг (наявність True).
# Додає нову книгу в цей файл.


def load_books(filename: str) -> list:
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def show_available_books(books: list) -> None:
    print("Available books:")
    for book in books:
        if book["availability"]:
            print(f'- {book["title"]} ({book["author"]}, {book["year of publication"]})')


def add_book(filename: str) -> None:
    title: str = input("Enter title: ")
    author: str = input("Enter author of book: ")
    year: int = int(input("Enter the year of publication: "))
    available: bool = input("Enter availability (True/False): ").lower() == "true"

    books = load_books(filename)

    new_book: dict = {
        "title": title,
        "author": author,
        "year of publication": year,
        "availability": available
    }

    books.append(new_book)

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(books, file, indent=4, ensure_ascii=False)

    print("Book successfully added!")


def main_json() -> None:
    filename: str = "./lesson7/books.json"
    books: list = load_books(filename)
    show_available_books(books)
    choice: str = input("Do yo want to add new book? (y/n): ")
    if choice.lower() == "y":
        add_book(filename)


# main_json()

# Створи XML-файл, що містить інформацію про продукти магазину:
# Назва продукту
# Ціна
# Кількість на складі
# Напиши програму, яка:
# Читає XML-файл і виводить назви продуктів та їхню кількість.
# Змінює кількість товару та зберігає зміни в XML-файл.
      

def read_products(filename: str) -> None:
    tree = ET.parse(filename)
    root = tree.getroot()

    print("Products list:")
    for product in root.findall("product"):
        name = product.find("name").text
        quantity = product.find("quantity").text
        print(f"{name}: {quantity}")


def update_quantity(filename: str) -> None:
    tree = ET.parse(filename)
    root = tree.getroot()

    product_name = input("Enter product name: ")
    new_quantity = input("Enter new quantity: ")

    found = False

    for product in root.findall("product"):
        name = product.find("name").text

        if name.lower() == product_name.lower():
            product.find("quantity").text = new_quantity
            found = True
            print("Quantity updated!")
            break

    if not found:
        print("Product not found!")

    tree.write(filename, encoding="utf-8", xml_declaration=True)


def main_xml() -> None:
    filename: str = "products.xml"

    read_products(filename)

    choice: str = input("Do you want to update quantity? (y/n): ")
    if choice.lower() == "y":
        update_quantity(filename)

# main_xml()

# Перетворення між форматами:
# Реалізуй класи, які перетворюватимуть CSV-файл до JSON та навпаки.
# Додай функціонал для перетворення XML-файлу до JSON.

class CSVandJSONConverter:
    """Converting CSV to JSON and vice versa"""

    @staticmethod
    def csv_to_json(csv_path: str, json_path: str) -> None:
        """Reads CSV file and writes it as JSON"""
        with open(csv_path, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = [line for line in reader]

        with open(json_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)
        
    @staticmethod
    def json_to_csv(json_path: str, csv_path: str) -> None:
        """Reads JSON file and writes it as CSV"""
        with open(json_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
        
        with open(csv_path, "w", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, data[0].keys())
            writer.writeheader()
            for line in data:
                writer.writerow(line)


class XMLtoJSONConverter:
    """Converts XML files to JSON"""

    @staticmethod
    def xml_to_json(xml_file_path: str, json_file_path: str):
        """Reads an XML file and writes it as JSON"""
        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        def parse_element(element):
            """Recursively converts an XML element into a dictionary"""
            parsed = {}
            parsed.update(element.attrib)
            if element.text and element.text.strip():
                parsed["text"] = element.text.strip()
            for child in element:
                child_parsed = parse_element(child)
                if child.tag not in parsed:
                    parsed[child.tag] = []
                parsed[child.tag].append(child_parsed)
            return parsed

        data = {root.tag: parse_element(root)}

        with open(json_file_path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)

# CSVandJSONConverter.csv_to_json("./lesson7/students.csv", "./lesson7/students.json")
# CSVandJSONConverter.json_to_csv("./lesson7/books.json", "./lesson7/books.csv")
# XMLtoJSONConverter.xml_to_json("./lesson7/products.xml", "./lesson7/products.json")

# Уяви, що ти розробляєш систему для відправки повідомлень різними каналами: через SMS, Email та Push-повідомлення. 
# Усі ці канали мають різні інтерфейси для відправки повідомлень, але ти хочеш уніфікувати їх, щоб використовувати один 
# універсальний інтерфейс для відправки повідомлень незалежно від каналу.

class MessageSender(ABC):
    """Abstract interface for sending messages"""

    @abstractmethod
    def send_message(self, message: str) -> None:
        """Send a message"""
        pass

class SMSService:
    """Service for sending SMS messages"""

    def send_sms(self, phone_number: str, message: str) -> None:
        """Send an SMS message"""
        if not re.fullmatch(r"\+?\d{10,15}", phone_number):
            raise ValueError("Invalid phone number")
        
        print(f"Sending SMS to {phone_number}: {message}")


class EmailService:
    """Service for sending email messages"""

    def send_email(self, email_address: str, message: str) -> None:
        """Send an email meassage"""
        if not re.fullmatch(r"[\w\.-]+@[\w\.-]+\.\w{2,}", email_address):
            raise ValueError("Invalid email adress")
        
        print(f"Sending email to {email_address}: {message}")


class PushService:
    """Service for sending push messages"""

    def send_push(self, device_id: str, message: str) -> None:
        """Send a push message"""
        if not device_id:
            raise ValueError("Device ID cannot be empty.")
        
        print(f"Sending Push to device {device_id}: {message}")


class SMSAdapter(MessageSender):
    """Adapter to use SMSService via MessageSender interface"""

    def __init__(self, sms_service: SMSService, phone_number: str) -> None:
        """Initialize SMS adapter"""
        self.sms_service: SMSService = sms_service
        self.phone_number: str = phone_number

    def send_message(self, message: str) -> None:
        """Send a SMS message"""
        self.sms_service.send_sms(self.phone_number, message)
        
class EmailAdapter(MessageSender):
    """Adapter to use EmailService via MessageSender interface"""

    def __init__(self, email_service: EmailService, email_adress: str) -> None:
        """Initialize Email adapter"""
        self.email_service: EmailService = email_service
        self.email_adress: str = email_adress

    def send_message(self, message: str) -> None:
        """Send an email message"""
        self.email_service.send_email(self.email_adress, message)


class PushAdapter(MessageSender):
    """Adapter to use PushService via MessageSender interface"""

    def __init__(self, push_service: PushService, device_id: str) -> None:
        """Initialize Push adapter"""
        self.push_service: PushService = push_service
        self.device_id: str = device_id

    def send_message(self, message: str) -> None:
        """Send a push notification"""
        self.push_service.send_push(self.device_id, message)


class NotificationSystem:
    def __init__(self, senders: list) -> None:
        self.senders: list = senders

    def send_to_all(self, message: str) -> None:
        for sender in self.senders:
            try:
                sender.send_message(message)
            except Exception as error:
                print(f"Error {sender.__class__.__name__}: {error}")


sms_service = SMSService()
email_service = EmailService()
push_service = PushService()

sms_adapter = SMSAdapter(sms_service, "+380123456789")
email_adapter = EmailAdapter(email_service, "user@example.com")
push_adapter = PushAdapter(push_service, "device123")

system = NotificationSystem([sms_adapter, email_adapter, push_adapter])    
system.send_to_all("Hello world!")

