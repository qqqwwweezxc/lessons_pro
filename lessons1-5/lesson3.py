# 1.	Реалізуйте клас Fraction (дробові числа), який має методи для додавання, віднімання, множення та
# ділення двох об'єктів цього класу. Використайте спеціальні методи __add__, __sub__, __mul__, __truediv__.
# 2.	Реалізуйте метод __repr__, щоб можна було коректно виводити об'єкти цього класу у форматі "numerator/denominator".


class Fraction:
    """
    Class for working with fractional numbers
    Attributes:
        numerator (int): The top part of the fraction
        denominator (int): The bottom part of the fraction. Cannot be zero
    """

    def __init__(self, numerator: int, denominator: int) -> None:
        """Initialize a Fraction object"""

        if denominator == 0:
            raise ValueError("Denominator cannot be zero")

        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other: "Fraction") -> "Fraction":
        """Add two fractions"""
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __sub__(self, other: "Fraction") -> "Fraction":
        """Subtract two fractions"""
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __mul__(self, other: "Fraction") -> "Fraction":
        """Multiply two fractions"""
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __truediv__(self, other: "Fraction") -> "Fraction":
        """Divide two fractions"""
        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero fraction")

        other.numerator, other.denominator = other.denominator, other.numerator
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __repr__(self) -> str:
        """Return the fraction in 'numerator/denominator' format"""
        return f"{self.numerator}/{self.denominator}"


n1 = Fraction(2, 3)
n2 = Fraction(3, 6)
print(n1 + n2)
print(n1 - n2)
print(n1 * n2)
print(n1 / n2)

# 1.	Реалізуйте клас Vector, що підтримує операції додавання, віднімання, множення на число та
# порівняння за довжиною. Використовуйте відповідні dunder-методи (__add__, __sub__, __mul__, __lt__, __eq__).
# 2.	Додайте до класу метод для отримання довжини вектора.
import math


class Vector:
    """
    A class representing a 2D vector.
    Attributes:
        x (float): coordinate of vector
        y (float): coordinate of vector
    """

    def __init__(self, x: float, y: float) -> None:
        """Initialize a vector with x and y coordinates"""
        self.x = x
        self.y = y

    def length(self) -> float:
        """Return the length of the vector"""

        return math.sqrt(self.x**2 + self.y**2)

    def __add__(self, other: "Vector") -> "Vector":
        """Add two vectors"""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Vector") -> "Vector":
        """Subtract two vectors"""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: float) -> "Vector":
        """Miltiply vector by a scalar"""
        return Vector(self.x * scalar, self.y * scalar)

    def __lt__(self, other: "Vector") -> bool:
        """Compare vectors by their length"""
        return self.length() < other.length()

    def __eq__(self, other: "Vector") -> bool:
        """Check if two vectors are equal by length"""
        return self.length() == other.length()

    def __repr__(self) -> str:
        """Return a string representation of the vector"""
        return f"Vector({self.x}, {self.y})"


v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(v1)
print(v2)
print(v1 + v2)
print(v1 - v2)
print(v1 * 2)
print(v1.length())
print(v1 < v2)
print(v1 == v2)

# 1.	Реалізуйте клас Person із параметрами name та age. Додайте методи для порівняння за віком
# (__lt__, __eq__, __gt__).
# 2.	Напишіть програму для сортування списку об'єктів класу Person за віком.


class Person:
    """
    Class representing a person
    Attributes:
        name (str): name of person
        age (int): age of person
    """

    def __init__(self, name: str, age: int) -> None:
        """Intialize a person's name and age"""
        self.name = name
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.age = age

    def __lt__(self, other: "Person") -> bool:
        """Less-than comparison"""
        return self.age < other.age

    def __gt__(self, other: "Person") -> bool:
        """Greater-than comparison"""
        return self.age > other.age

    def __eq__(self, other: "Person") -> bool:
        """Equality comparison"""
        return self.age == other.age

    def __repr__(self) -> str:
        """Return readable representation"""
        return f"Person with name {self.name} and age {self.age}"


people = [
    Person("Dima", 22),
    Person("Maksim", 39),
    Person("Vitalii", 10),
    Person("Diana", 5),
]
print(people)

sorted_people = sorted(people)

print(sorted_people)

# 1.	Реалізуйте клас BinaryNumber, який представляє двійкове число. Додайте методи для виконання
# двійкових операцій: AND (__and__), OR (__or__), XOR (__xor__) та NOT (__invert__).
# 2.	Напишіть тест для цих операцій.


class BinaryNumber:
    """Class representing a binary number"""

    def __init__(self, value: str):
        """
        Initialize binary number.

        Args:
            value (str): binary string (e.g., "1010")
        """
        if not all(c in "01" for c in value):
            raise ValueError("Value must contain only 0 and 1")

        self.value = value

    def __repr__(self):
        """Return readable representation"""
        return f"BinaryNumber('{self.value}')"

    def __and__(self, other):
        """Binary AND operation"""
        result = int(self.value, 2) & int(other.value, 2)
        return BinaryNumber(bin(result)[2:])

    def __or__(self, other):
        """Binary OR operation"""
        result = int(self.value, 2) | int(other.value, 2)
        return BinaryNumber(bin(result)[2:])

    def __xor__(self, other):
        """Binary XOR operation"""
        result = int(self.value, 2) ^ int(other.value, 2)
        return BinaryNumber(bin(result)[2:])

    def __invert__(self):
        """Binary NOT operation"""
        inverted = "".join("1" if bit == "0" else "0" for bit in self.value)
        return BinaryNumber(inverted)


a = BinaryNumber("1010")
b = BinaryNumber("1100")

print("a =", a)
print("b =", b)
print("a & b =", a & b)
print("a | b =", a | b)
print("a ^ b =", a ^ b)
print("~a =", ~a)
print("~b =", ~b)

# 1.	Реалізуйте власну версію функцій len(), sum(), та min(). Використовуйте спеціальні методи
# __len__, __iter__, __getitem__, якщо необхідно.
# 2.	Напишіть тест для кожної з реалізованих функцій.


class MyBuilitins:
    """
    Class representing a my implementation of functions
    len(), sum(), min()
    """

    def __init__(self, data):
        """Initialize collection with a list of elements"""
        self.data = data

    def __len__(self):
        """Return number of elements in the collection"""
        count = 0
        for _ in self.data:
            count += 1
        return count

    def __iter__(self):
        """Return iterator for the collection"""
        for item in self.data:
            yield item


def my_len(obj):
    """
    Custom implementation of len()
    """
    return obj.__len__()


def my_sum(iterable):
    """
    Custom implementation of sum()
    """
    total = 0
    for item in iterable:
        total += item
    return total


def my_min(iterable):
    """
    Custom implementation of min()
    """
    iterator = iter(iterable)
    minimum = next(iterator)

    for item in iterator:
        if item < minimum:
            minimum = item

    return minimum


test_numbers = [0, 1, 2, 8, 3, 10]

print("length:", my_len(test_numbers))
print("summa:", my_sum(test_numbers))
print("minimum:", my_min(test_numbers))

# 1.	Реалізуйте клас User з атрибутами first_name, last_name, email. Додайте методи для отримання
# та встановлення цих атрибутів через декоратор @property.
# 2.	Додайте методи для перевірки формату email-адреси.

import re


class User:
    """
    Class representing a user
    Atributes:
        first_name (str): first name of user
        last_name (str): last name of user
        email (str): email of user
    """

    def __init__(self, first_name: str, last_name: str, email: str) -> None:
        """Initialize atributes of user"""
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("The first name must be a string")
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("The last name must be a string")
        self._last_name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value: str):
        if not self.validate_email(value):
            raise TypeError("Ivalid email format")
        self._email = value

    def validate_email(self, email: str) -> bool:
        """Check email format"""
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(pattern, email) is not None


user = User("Vladimir", "Novikov", "vladimir.novikov@gmail.com")

print(user.first_name)
print(user.last_name)
print(user.email)

# 1.	Створіть клас Vector, який представляє вектор у просторі з n вимірами. Додайте методи для додавання,
# віднімання векторів та обчислення скалярного добутку. Використовуйте dunder-методи (__add__, __sub__, __mul__).
# 2.	Додайте можливість порівняння двох векторів за їх довжиною.


class VectorExpanse:
    """
    Class representing a vector in the space
    Attributes:
        coordinates (list or tuple): coordinates of vector
    """

    def __init__(self, coordinates) -> None:
        self.coordinates = list(coordinates)

    def __repr__(self):
        return f"Vector: {self.coordinates}"

    def __add__(self, other: "VectorExpanse") -> "VectorExpanse":
        """Add two vectors"""
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError("Vectors must have the same number of coordinates for add")
        return VectorExpanse(
            list(map(lambda a, b: a + b, self.coordinates, other.coordinates))
        )

    def __sub__(self, other: "VectorExpanse") -> "VectorExpanse":
        """Subtract two vectors"""
        if len(self.coordinates) != len(other.coordinates):
            raise ValueError(
                "Vectors must have the same number of coordinates for subtruct"
            )
        return VectorExpanse(
            list(map(lambda a, b: a - b, self.coordinates, other.coordinates))
        )

    def __mul__(self, other: "VectorExpanse") -> "VectorExpanse":
        """Calculates the scalar product"""
        if isinstance(other, VectorExpanse):
            if len(self.coordinates) != len(other.coordinates):
                raise ValueError(
                    "Vectors must have the same number of coordinates for dot product"
                )
            return sum(map(lambda a, b: a * b, self.coordinates, other.coordinates))
        elif isinstance(other, (int, float)):
            return VectorExpanse([a * other for a in self.coordinates])
        else:
            raise TypeError("Unsupported multiplication")

    def length(self):
        """Length of vector"""
        return math.sqrt(sum(a**2 for a in self.coordinates))

    def __lt__(self, other: "VectorExpanse") -> bool:
        """Compare vectors by their length"""
        return self.length() < other.length()

    def __gt__(self, other: "VectorExpanse") -> bool:
        """Compare vectors by their length"""
        return self.length() > other.length()

    def __eq__(self, other: "VectorExpanse") -> bool:
        """Check if two vectors are equal by length"""
        return self.length() == other.length()


v1 = VectorExpanse([1, 2, 3])
v2 = VectorExpanse([4, 5, 6])

print(v1 + v2)
print(v1 - v2)
print(v1 * v2)
print(v1.length())
print(v1 > v2)
print(v1 < v2)

# 1.	Реалізуйте клас Price, що представляє ціну товару з можливістю заокруглення до двох десяткових знаків.
# Додайте методи для додавання, віднімання та порівняння цін.
# 2.	Поміркуйте, як клас Price може бути використаний в майбутньому класі PaymentGateway для обробки
# фінансових транзакцій.


class Price:
    """
    Class representing a price of product rounded to 2 decimal places.
    Attributes:
        price (float): price of product
    """

    def __init__(self, price: float) -> None:
        if price < 0:
            raise ValueError("Price cannot be a negative")

        self.price = round(float(price), 2)

    def __repr__(self):
        return f"Price: {self.price:.2f}"

    def __add__(self, other: "Price") -> "Price":
        """Add price to price"""
        if isinstance(other, Price):
            return Price(self.price + other.price)
        raise TypeError("Can add only price to price")

    def __sub__(self, other: "Price") -> "Price":
        """Subtract price from price"""
        if isinstance(other, Price):
            return Price(self.price - other.price)
        raise TypeError("Can only subtract Price from Price")

    def __eq__(self, other: "Price") -> "Price":
        """Check if two prices are equal"""
        if isinstance(other, Price):
            return self.price == other.price
        return False

    def __lt__(self, other: "Price") -> "Price":
        """Compare two prices"""
        if isinstance(other, Price):
            return self.price < other.price
        raise TypeError("Comparison allowed only between Price objects")

    def __gt__(self, other: "Price") -> "Price":
        """Compare two prices"""
        if isinstance(other, Price):
            return self.price > other.price
        raise TypeError("Comparison allowed only between Price objects")

    def __le__(self, other: "Price") -> "Price":
        """Compare two prices"""
        if isinstance(other, Price):
            return self.price <= other.price
        raise TypeError("Comparison allowed only between Price objects")


p1 = Price(20.1212)
p2 = Price(7.123)

print(p1)
print(p2)
print(p1 + p2)
print(p1 - p2)
print(p1 > p2)
print(p1 < p2)
print(p1 >= p2)
print(p1 == p2)

# Реалізуйте клас Product, який представляє товар з наступними атрибутами:
# 1.	name – назва товару (рядок).
# 2.	price – ціна товару (число з плаваючою комою).
# Вам потрібно реалізувати три варіанти роботи з атрибутом price:
# 1.	Сеттери/геттери: реалізуйте методи get_price() і set_price(), які будуть дозволяти отримувати та
# встановлювати значення атрибута price. Додайте перевірку, що ціна не може бути від'ємною. Якщо ціна менше 0,
# викиньте виняток ValueError.
# 2.	Декоратор @property: використайте декоратор @property для створення властивості price. Також реалізуйте
# перевірку на від'ємне значення ціни.
# 3.	Дескриптори: створіть окремий клас дескриптора PriceDescriptor, який буде контролювати встановлення та
# отримання ціни. Додайте до класу Product атрибут price, що використовує дескриптор для перевірки ціни.
# Завдання:
# 1.	Реалізуйте всі три класи: ProductWithGetSet, ProductWithProperty та ProductWithDescriptor.
# 2.	Напишіть тестову програму, яка створює об'єкти кожного з цих класів та намагається:
# o	Отримати та змінити ціну товару.
# o	Встановити від'ємне значення ціни та впевнитись, що воно правильно обробляється (викидання ValueError).
# 3.	Порівняйте переваги та недоліки кожного з підходів (сеттери/геттери, @property, дескриптори). Напишіть
# висновок, який підхід більш зручний у вашому випадку та чому.


class ProductWithGetSet:
    """
    Class representing a product
    Attributes:
        name (str): - name of product
        price (float): - price of product
    """

    def __init__(self, name: str, price: float) -> None:
        self.set_name(name)
        self.set_price(price)

    def get_name(self):
        return self._name

    def set_name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        self._name = value

    def get_price(self):
        return self._price

    def set_price(self, value: float):
        if value < 0:
            raise ValueError("Price cannot be a negative")
        self._price = value

    def __repr__(self):
        return f"Product with name: {self._name} and price: {self._price}"


class ProductWithProperty:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value


class PriceDescriptor:
    def __get__(self, instance, owner):
        return instance._price

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        instance._price = value


class ProductWithDescriptor:
    price = PriceDescriptor()

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


def test_products():

    print("ProductWithGetSet")
    p1 = ProductWithGetSet("Laptop", 100500)
    print(p1.get_price())

    p1.set_price(100200)
    p1.set_name("IPhone")
    print(p1.get_name())
    print(p1.get_price())

    try:
        p1.set_price(-1)
    except ValueError as e:
        print("Error:", e)

    print("ProductWithProperty")
    p2 = ProductWithProperty("Headphones", 200)
    print(p2.price)

    p2.price = 900
    print(p2.price)

    try:
        p2.price = -50
    except ValueError as e:
        print("Error:", e)

    print("ProductWithDescriptor")
    p3 = ProductWithDescriptor("Airpods", 500)
    print(p3.price)

    p3.price = 700
    print(p3.price)

    try:
        p3.price = -20
    except ValueError as e:
        print("Error:", e)


test_products()
"""
Висновок:
Найзручніший підхід у цьому випадку — @property.
Причини:
1. Код виглядає як робота зі звичайним атрибутом.
2. Зберігається перевірка значень.
3. Менше зайвого коду.
"""
