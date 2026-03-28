# Напишіть функцію analyze_object(obj), яка приймає будь-який об'єкт та виводить:

#     Тип об'єкта.
#     Список всіх методів та атрибутів об'єкта.
#     Тип кожного атрибута.


def analyze_object(obj: object) -> None:
    """Checking object types and attributes"""
    print(f"Type of object: {type(obj)}")
    print("Attibutes and methods:")
    for name in dir(obj):
        if not name.startswith("__"):
            value = getattr(obj, name)
            attr_type = type(value)
            print(f"- {name}: {attr_type}")


class MyClass:
    def __init__(self, value: object) -> None:
        self.value = value

    def say_hello(self) -> str:
        return f"Hello, {self.value}"


obj = MyClass("World")
analyze_object(obj)

# Реалізуйте функцію call_function(obj, method_name, *args), яка приймає об'єкт, назву методу в вигляді рядка '
# 'та довільні аргументи для цього методу. Функція повинна викликати відповідний метод об'єкта і повернути результат.


def call_function(obj: object, method_name: str, *args: object) -> object:
    method = getattr(obj, method_name)
    return method(*args)


class Calculator:
    """Class calculates two numbers"""

    def add(self, a: float, b: float) -> float:
        """Add two numbers"""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Subtract two numbers"""
        return a - b


calc = Calculator()
print(call_function(calc, "add", 10, 5))
print(call_function(calc, "subtract", 10, 5))

# Напишіть програму, яка приймає на вхід назву модуля (рядок) та виводить список усіх класів, функцій
# та їхніх сигнатур у модулі. Використовуйте модуль inspect.
import inspect


def analyze_module(module_name: str) -> None:
    """Analyze module and prints a list of all classes, functions, and their signatures in a module"""

    functions: list[str] = []
    classes: list[str] = []

    for name, obj in inspect.getmembers(module_name):
        if name.startswith("__"):
            continue

        if inspect.isfunction(obj) or inspect.isbuiltin(obj):
            try:
                signature = inspect.signature(obj)
                functions.append(f"- {name}{signature}")
            except ValueError:
                functions.append(f"- {name}(...)")

        elif inspect.isclass(obj):
            classes.append(name)

    print("Functions:")
    if functions:
        for func in functions:
            print(func)
    else:
        print("- module dont have functions")

    print("\nClasses:")
    if classes:
        for cls in classes:
            print(f"- {cls}")
    else:
        print("- module dont have classes")


analyze_module("math")

# Напишіть функцію create_class(class_name, methods), яка створює клас з заданим іменем та методами.

# Методи передаються у вигляді словника, де ключі — це назви методів, а значення — функції.


def create_class(class_name: str, methods: dict[str, callable]) -> type:
    """Creates class"""
    new_class = type(class_name, (object,), methods)
    return new_class


def say_hello(self: object) -> str:
    return "Hello!"


def say_goodbye(self: object) -> str:
    return "Goodbye!"


methods = {"say_hello": say_hello, "say_goodbye": say_goodbye}

MyDynamicClass = create_class("MyDynamicClass", methods)

obj = MyDynamicClass()
print(obj.say_hello())
print(obj.say_goodbye())

# Напишіть клас MutableClass, який має методи для динамічного додавання та видалення атрибутів об'єкта.
# Реалізуйте методи add_attribute(name, value) та remove_attribute(name).


class MutableClass:
    def add_attribute(self, name: str, value: object) -> None:
        """Add a attribute to object"""
        setattr(self, name, value)

    def remove_attribute(self, name: str) -> None:
        """Delete attribute from object"""
        if hasattr(self, name):
            delattr(self, name)
        else:
            raise AttributeError(f"Attribute '{name}' not found")


obj = MutableClass()

obj.add_attribute("name", "Python")
print(obj.name)

obj.remove_attribute("name")
# print(obj.name)

# Напишіть клас Proxy, який приймає на вхід об'єкт і переадресовує виклики методів цього об'єкта,
# додатково логуючи виклики (наприклад, виводячи назву методу та аргументи).


class Proxy:
    """Takes an object as input and forwards calls to the methods of this object, additionally logging the calls"""

    def __init__(self, obj: object) -> None:
        """Initialaize object"""
        self.obj = obj

    def __getattr__(self, name: str) -> object:
        attr = getattr(self.obj, name)
        if callable(attr):

            def wrapper(*args: object, **kwargs: object) -> object:
                print("Calling method:")
                print(f"{name} with args: {args}")
                return attr(*args, **kwargs)

            return wrapper
        return attr


class MyClass:
    def greet(self, name: str):
        return f"Hello, {name}!"


obj = MyClass()
proxy = Proxy(obj)

print(proxy.greet("Alice"))

# Реалізуйте декоратор log_methods, який додається до класу і логуватиме виклики всіх його методів (назва методу та аргументи).


def log_methods(cls: type) -> type:
    for name, value in cls.__dict__.items():
        if callable(value):

            def make_wrapper(method: callable, name: str) -> callable:
                def wrapper(self: object, *args: object, **kwargs: object) -> object:
                    print(f"Logging: {name} called with {args}")
                    return method(self, *args, **kwargs)

                return wrapper

            setattr(cls, name, make_wrapper(value, name))

    return cls


@log_methods
class MyClass:
    """Calculates two numbers"""

    def add(self, a: float, b: float):
        """Add two numbers"""
        return a + b

    def subtract(self, a: float, b: float):
        """Subtract two numbers"""
        return a - b


obj = MyClass()
obj.add(5, 3)
obj.subtract(5, 3)

# Напишіть функцію analyze_inheritance(cls), яка приймає клас, аналізує його спадкування та виводить усі методи,
# які він наслідує від базових класів.


def analyze_inheritance(cls: type) -> None:
    """Analyze class analyzes its inheritance and deduces all the methods it inherits from base classes."""
    print(f"Class {cls.__name__} inheritance:")
    for base in cls.__mro__[1:]:
        if base is object:
            continue

        for attr_name, attr_value in base.__dict__.items():
            if callable(attr_value) and not attr_name.startswith("__"):
                if attr_name not in cls.__dict__:
                    print(f"- {attr_name} from {base.__name__}")


class Parent:
    def parent_method(self):
        pass


class Child(Parent):
    def child_method(self):
        pass


analyze_inheritance(Child)

# Напишіть клас DynamicProperties, в якому можна динамічно додавати властивості через методи. Використовуйте вбудовані
# функції property() для створення геттера та сеттера під час виконання програми.


class DynamicProperties:
    """A class that allows dynamic creation of properties at runtime."""

    def __init__(self) -> None:
        """
        Initialize internal storage for property values.
        """
        self._values: dict[str, object] = {}

    def add_property(self, name: str, default_value: object = None) -> None:
        """
        Dynamically adds a new property with getter and setter.

        Attributes:
            name (str): The name of the property.
            default_value (Any): The initial value of the property.
        """
        self._values[name] = default_value

        def getter(instance: "DynamicProperties") -> object:
            """
            Return the value of the property.
            """
            return instance._values.get(name)

        def setter(instance: "DynamicProperties", value: object) -> None:
            """
            Set the value of the property.
            """
            instance._values[name] = value

        prop: property = property(getter, setter)

        setattr(self.__class__, name, prop)


obj = DynamicProperties()
obj.add_property("name", "default_name")
print(obj.name)
obj.name = "Python"
print(obj.name)

# Реалізуйте метаклас SingletonMeta, який гарантує, що клас може мати лише один екземпляр (патерн Singleton).
# Якщо екземпляр класу вже створений, наступні виклики повинні повертати той самий об'єкт.


class SingletonMeta(type):
    """
    Metaclass that guarantees that a class can only have one instance
    If an instance of the class has already been created, subsequent calls, returns the same object.
    """

    _instance: object = None

    def __call__(cls, *args: tuple, **kwargs: dict) -> object:
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        print("Creating instance")


obj1 = Singleton()
obj2 = Singleton()
print(obj1 is obj2)

# Реалізуйте метаклас LimitedAttributesMeta, який дозволяє класам мати лише фіксовану кількість атрибутів
# (наприклад, максимум 3). Якщо додати більше атрибутів, має виникати помилка.


class LimitedAttributesMeta(type):
    """
    Metaclass that limits the number of attributes in a class.
    Raises TypeError if more than `max_attrs` are defined.
    """

    max_attrs: int = 3

    def __new__(mcs, name: str, bases: tuple, attrs: dict) -> type:
        real_attrs: list[str] = [atr for atr in attrs if not atr.startswith("__")]

        if len(real_attrs) > mcs.max_attrs:
            raise TypeError(
                f"Class {name} cannot have more than {mcs.max_attrs} attributes."
            )

        return super().__new__(mcs, name, bases, attrs)


class LimitedClass(metaclass=LimitedAttributesMeta):
    attr1 = 1
    attr2 = 2
    attr3 = 3
    # attr4 = 4  # Викличе помилку


obj = LimitedClass()

# Створіть метаклас LoggingMeta, який автоматично додає логування при доступі до будь-якого атрибута класу.
# Кожен раз, коли атрибут змінюється або читається, повинно з'являтися повідомлення в консолі.


class LoggingMeta(type):
    """Metaclass which automatically adds logging when accessing any class attribute"""

    def __new__(cls, name: str, bases: tuple, attrs: dict) -> type:

        def __getattribute__(self, item: str) -> object:
            if not item.startswith("__"):
                print(f"Logging: accessed '{item}'")
            return object.__getattribute__(self, item)

        def __setattr__(self, key: str, value: object) -> None:
            if key in self.__dict__:
                print(f"Logging: modified '{key}'")
            return object.__setattr__(self, key, value)

        attrs["__getattribute__"] = __getattribute__
        attrs["__setattr__"] = __setattr__

        return super().__new__(cls, name, bases, attrs)


class MyClass(metaclass=LoggingMeta):
    def __init__(self, name):
        self.name = name


obj = MyClass("Python")
print(obj.name)
obj.name = "New Python"

# Реалізуйте метаклас AutoMethodMeta, який автоматично генерує методи геттера та сеттера для кожного атрибута класу.
# Метод повинен починатися з get_<attribute>() та set_<attribute>(value).


class AutoMethodMeta(type):
    """
    Metaclass that automatically generates getter and setter methods for all class attributes.
    """

    def __new__(cls, name: str, bases: tuple, attrs: dict) -> type:
        new_attrs: dict[str, object] = {}

        for attr_name, value in attrs.items():
            new_attrs[attr_name] = value

            if attr_name.startswith("__") or callable(value):
                continue

            def make_getter(attr: str):
                def getter(self) -> object:
                    return getattr(self, attr)

                return getter

            def make_setter(attr: str):
                def setter(self, value: object) -> None:
                    setattr(self, attr, value)

                return setter

            new_attrs[f"get_{attr_name}"] = make_getter(attr_name)
            new_attrs[f"set_{attr_name}"] = make_setter(attr_name)

        return super().__new__(cls, name, bases, new_attrs)


class Person(metaclass=AutoMethodMeta):
    name = "John"
    age = 30


p = Person()
print(p.get_name())
p.set_age(31)
print(p.get_age())

# Реалізуйте метаклас TypeCheckedMeta, який перевіряє типи атрибутів при їх встановленні.
# Якщо тип значення не відповідає типовому опису, має виникати помилка.


class TypeCheckedMeta(type):
    """Metaclass that enforces type checking for class attributes based on type annotations."""

    def __new__(cls, name: str, bases: tuple, attrs: dict) -> type:
        annotations: dict[str, type] = {}
        for base in bases:
            annotations.update(getattr(base, "__annotations__", {}))
        annotations.update(attrs.get("__annotations__", {}))

        def __setattr__(self, key: str, value: object) -> None:
            if key in annotations:
                expected_type: type = annotations[key]
                if not isinstance(value, expected_type):
                    raise TypeError(
                        f"For attribute '{key}' expected type '{expected_type.__name__}', but got '{type(value).__name__}'."
                    )
            object.__setattr__(self, key, value)

        attrs["__setattr__"] = __setattr__
        return super().__new__(cls, name, bases, attrs)


class MyPerson(metaclass=TypeCheckedMeta):
    name: str = ""
    age: int = 0


person = MyPerson()
person.name = "John"
person.age = "30"
