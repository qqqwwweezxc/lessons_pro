# 1.	Написати функцію my_sum, яка перекриває вбудовану функцію sum. Функція поинна просто виводити повідомлення:
# "This is my custom sum function!".

import builtins


def sum(*args, **kwargs) -> None:
    """
    Custom function that overrides Python built-in sum().
    """
    print("This is my custom sum function!")


numbers = [1, 2, 3, 5, 10]

result = sum(numbers)
print(result)
sum(numbers)
print(builtins.sum(numbers))

# Створити програму, яка імітує менеджер підписки на розсилку, демонструючи роботу з локальними,
# глобальними та вкладеними областями видимості.

subscribers = []


def subscribe(subscriber: str) -> str:
    """
    Add a subscriber to the global subscribers list
    and return a confirmation message.
    """
    subscribers.append(subscriber)

    def confirm_subscription() -> str:
        """
        Nested function that generates a confirmation message.
        """
        return f"Підписка підтверджена для {subscriber}."

    return confirm_subscription()


def unsubscribe(subscriber: str) -> str:
    """
    Remove a subscriber from the subscribers list
    and reutrns message about the result of the unsubscription.
    """
    if subscriber in subscribers:
        subscribers.remove(subscriber)
        return f"{subscriber} успішно відписаний."
    else:
        return f"Підписника з ім'ям {subscriber} не знайдено"


print(subscribe("Ваня"))
print(subscribe("Дима"))
print(subscribers)
print(unsubscribe("Ваня"))
print(unsubscribe("Петя"))
print(subscribers)

# Написати програму, яка імітує систему замовлення з акціями, де знижки зберігаються у глобальній області,
# а нарахування знижки відбувається локально для кожного клієнта.

discount = 0.1


def create_order(price: float) -> None:
    """
    Creates an order and calculates the final price with discounts.
    """
    final_price = price * (1 - discount)
    print(
        f"Початкова ціна: {price}, кінцева ціна зі знижкою ({int(discount * 100)}%): {final_price}"
    )

    def apply_additional_discount() -> None:
        """
        Applies an additional discount for VIP customers.
        """
        nonlocal final_price

        vip_discount = 0.05
        final_price *= 1 - vip_discount

        print(
            f"Ціна після додаткової VIP-знижки ({int(vip_discount * 100)}%): {final_price}"
        )

    apply_additional_discount()


create_order(1000)

# Розробити програму, яка симулює таймер для тренувань із вбудованою функцією, що дозволяє змінювати час
# тренування на кожному кроці.

default_time = 60


def training_session(rounds: int) -> None:
    """
    Simulates a training timer.
    """

    time_per_round = default_time

    def adjust_time() -> None:
        """
        Adjusts the time for the next training round.
        """
        nonlocal time_per_round
        time_per_round -= 5

    for i in range(1, rounds + 1):
        print(f"Раунд {i}: {time_per_round} хвилин")

        adjust_time()


training_session(3)

# Розробити простий календар подій.

# 1.	Використовуючи замикання, створити функції для додавання подій, видалення подій та перегляду майбутніх подій.

# 2.	Зберігати події у списку за допомогою глобальної змінної.


events_list = []


def create_event_manager():
    """
    Returns three functions for managing events:
    add_event, remove_event, view_events
    """
    global events_list

    def add_event(event_name, event_date):
        """Add a new event to the global events list."""
        events_list.append({"name": event_name, "date": event_date})
        print(f"Event '{event_name}' on {event_date} added.")

    def remove_event(event_name):
        """Remove an event by its name from the global events list."""
        global events_list
        events_list = [event for event in events_list if event["name"] != event_name]
        print(f"Event '{event_name}' removed (if it existed).")

    def view_events():
        """Print all upcoming events."""
        if not events_list:
            print("No upcoming events.")
        else:
            print("Upcoming events:")
            for event in events_list:
                print(f"- {event['name']} on {event['date']}")

    return add_event, remove_event, view_events


add_event, remove_event, view_events = create_event_manager()

add_event("Поход к врачу", "2026-03-15")
add_event("Урок по программированию", "2026-03-20")
view_events()
remove_event("Поход к врачу")
view_events()

# Створити калькулятор, який використовує замикання для створення функцій додавання, віднімання, множення та ділення.


def create_calculator(operator: str):
    """
    Returns a function that performs a calculation based on the given operator.
    """

    def calculate(a: float, b: float) -> float:
        match operator:
            case "+":
                return a + b
            case "-":
                return a - b
            case "*":
                return a * b
            case "/":
                if b == 0:
                    raise ValueError("Cannot divide by zero")
                return a / b
            case _:
                raise ValueError(f"Unsupported operator: {operator}")

    return calculate


add = create_calculator("+")
subtract = create_calculator("-")
multiply = create_calculator("*")
divide = create_calculator("/")

print("5 + 3 =", add(5, 3))
print("10 - 4 =", subtract(10, 4))
print("6 * 7 =", multiply(6, 7))
print("20 / 5 =", divide(20, 5))

# Розробити програму для трекінгу витрат, яка використовує глобальні змінні для зберігання загальної суми витрат.

total_expense = 0.0


def add_expense(amount: float) -> None:
    """
    Adds the given expense amount to the global total_expense.
    """
    global total_expense
    if amount < 0:
        print("Expense amount cannot be negative.")
        return
    total_expense += amount
    print(f"Added {amount} to expenses. Total is now {total_expense}.")


def get_expense() -> float:
    """
    Returns the current total of all expenses.
    """
    return total_expense


def show_menu() -> None:
    """
    Displays the main menu and handles user input.
    """
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add expense")
        print("2. Show total expenses")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        match choice:
            case "1":
                try:
                    amount = float(input("Enter expense amount: "))
                    add_expense(amount)
                except ValueError:
                    print("Please enter a valid number.")
            case "2":
                print(f"Total expenses: {get_expense():.2f}")
            case "3":
                print("Exiting program. Goodbye!")
                break
            case _:
                print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    show_menu()

# Реалізувати систему зберігання налаштувань користувача за допомогою замикань.


def create_user_settings():
    """
    Creates a user settings manager using closure.
    """
    settings = {"theme": "light", "language": "en", "notifications": True}

    def settings_manager(action, key=None, value=None):
        """
        Manage user settings.

        Parameters:
        - action (str): 'get', 'set', or 'update'
        - key (str, optional): the setting key
        - value (any, optional): the value to set

        Returns:
        - For 'get': the value of a setting or all settings if key is None
        - For 'set': None
        - For 'update': None
        """
        nonlocal settings

        if action == "get":
            if key:
                return settings.get(key, None)
            else:
                return settings.copy()  # return all settings

        elif action == "set":
            if key and value is not None:
                settings[key] = value

        elif action == "update":
            if isinstance(value, dict):
                settings.update(value)

        else:
            raise ValueError("Action must be 'get', 'set', or 'update'")

    return settings_manager


user_settings = create_user_settings()

print("Initial settings:", user_settings("get"))

print("Theme:", user_settings("get", key="theme"))

user_settings("set", key="theme", value="dark")
print("Updated theme:", user_settings("get", key="theme"))

user_settings("update", value={"language": "fr", "notifications": False})
print("Updated settings:", user_settings("get"))

# Написати програму для кешування результатів функції, щоб покращити продуктивність.


def memoize(func):
    """
    Decorator - function to cache results of the given function.
    """
    cache = {}

    def wrapper(*args):
        if args in cache:
            print(f"Cache hit for args {args}")
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            print(f"Cache miss for args {args}, computing result...")
            return result

    return wrapper


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


memoized_fibonacci = memoize(fibonacci)

print(memoized_fibonacci(10))
print(memoized_fibonacci(10))
print(memoized_fibonacci(8))

# Розробити програму для управління товарами в онлайн-магазині, використовучи карирувані функції.


def create_product(name: str, price: float, quantity: int):
    """
    Create a product dictionary with name, price, and quantity.
    Returns a function to update the product's price.
    """
    product = {"name": name, "price": price, "quantity": quantity}

    def update_price(new_price: float):
        """
        Update the price of the product.
        """
        if new_price < 0:
            print("Price cannot be negative!")
            return
        product["price"] = new_price
        print(f"Price of '{product['name']}' updated to {product['price']}$")

    def display_product():
        """
        Print current product details.
        """
        print(
            f"Product: {product['name']}, Price: {product['price']}$, Quantity: {product['quantity']}"
        )

    return update_price, display_product


update_price_fn, show_product_fn = create_product("Laptop", 1200.0, 5)

show_product_fn()
update_price_fn(1100.0)
show_product_fn()
update_price_fn(-50)
