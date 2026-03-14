# Створіть простий консольний калькулятор, який дозволяє виконувати основні арифметичні операції (+, -, *, /).
# Реалізуйте у ньому обробку таких винятків: ZeroDivisionError, ValueError
# Створіть власний виняток UnknownOperationError для невідомих операцій.
# Додаткове завдання: додайте можливість роботи з десятковими числами та обробку винятків, пов'язаних із переповненням.


class UnknownOperationError(Exception):
    """Custom exception for unknow operations in calculating"""

    pass


def calculator() -> None:
    """
    Calculating two float numbers
    """
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        match operator:
            case "+":
                result = num1 + num2
            case "-":
                result = num1 - num2
            case "*":
                result = num1 * num2
            case "/":
                if num2 == 0:
                    raise ZeroDivisionError("You can't divide by zero")
                result = num1 / num2
            case _:
                raise UnknownOperationError(f"Unknown operator {operator}")

        print("Result:", result)

    except ValueError:
        print("Error: Please enter valid numbers.")

    except ZeroDivisionError as error:
        print("Error:", error)

    except UnknownOperationError as error:
        print("Error:", error)

    except OverflowError:
        print("Error: Number overflow occurred.")

    finally:
        print("End of calculating...")


calculator()

# Напишіть програму, яка зчитує числа з текстового файлу та обчислює їхнє середнє арифметичне. Обробіть такі винятки:
# FileNotFoundError (файл не знайдено)
# ValueError (у файлі містяться нечислові дані)
# Додаткове завдання: реалізуйте можливість обробки порожнього файлу та файлу, що містить лише один рядок.


def average() -> None:
    """Read numbers from a file and calculate their average."""
    try:
        numbers = []
        file_txt = input("Enter file name: ")
        with open(file_txt, "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    numbers.append(float(line))

        if not numbers:
            raise ValueError("File is empty")

        avg = sum(numbers) / len(numbers)
        print("Average:", avg)

    except FileNotFoundError:
        print("Error: File not found.")

    except ValueError as error:
        print("Error:", error)


average()

# Створити гнучкий механізм для обробки різноманітних ігрових подій, надаючи детальну інформацію про події, що відбулися.

# Вимоги:
#     Створити клас GameEventException, наступний від базового класу.
#     Додайте наступні властивості:
#     event_type: рядок, який описує тип події (наприклад, "death", "levelUp").
#     details: словник або об'єкт, що містить додаткову інформацію про події.


class GameEventException(Exception):
    """Custom exception for the game about game events"""

    def __init__(self, event_type: str, details: dict) -> None:
        """
        Initialize game event
        Attributes:
            event_type (str): type of event (death, levelUp)
            details (dict): event information
        """

        self.event_type = event_type
        self.details = details

        message = f"Game event: {event_type}"
        super().__init__(message)


def player_death():
    try:
        raise GameEventException(
            "death", {"reason": "sword strike", "enemy": "zoombie"}
        )

    except GameEventException as event:
        print("Game event started!")
        if event.event_type == "death":
            print("Player died.")
            print(
                f"Reason: {event.details.get("reason")}, killer: {event.details.get("enemy")}."
            )


def level_up():
    try:
        raise GameEventException(
            "levelUp",
            {"new_level": 3, "experience_gained": 100},
        )

    except GameEventException as event:
        print("Game event started!")
        if event.event_type == "levelUp":
            print("Level up!")
            print(
                f"New level: {event.details.get("new_level")}, because {event.details.get("experience_gained")} experience gained!"
            )


player_death()
level_up()


# Створити механізм для обробки ситуацій, коли гравецю не вистачає ресурсів для виконання дій.
# Вимоги:
#     Створити клас InsufficientResourcesException, наступний від базового класу-вийнятку.
#     Додайте наступні властивості:
#     required_resource: рядок, що вказує на бракуючий ресурс (наприклад, "золото", "мана").
#     required_amount: Число, що вказує потрібну кількість ресурсу.
#     current_amount: Число, що вказує поточну кількість ресурсів у гравця.


class InsufficientResourcesException(Exception):
    """Custom exception for games when player dont have some resources"""

    def __init__(
        self, required_resource: str, required_amount: float, current_amount: float
    ) -> None:
        """
        Initialize resources of player
        Attributes:
            required_resource (str): missing resource
            required_amount (float): the required amount of resource
            current_amount (float): current number of resources of player
        """

        self.required_resource = required_resource
        self.required_amount = required_amount
        self.current_amount = current_amount

        super().__init__(
            f"Not enough {required_resource}. Required: {required_amount}, Current: {current_amount}"
        )


def buying_resource(resource_name: str, required_amount: float, player_resources: dict):
    try:
        current_amount = player_resources.get(resource_name, 0)

        if current_amount < required_amount:
            raise InsufficientResourcesException(
                resource_name, required_amount, current_amount
            )

        player_resources[resource_name] -= required_amount
        print(f"Buying resource {resource_name} completed successfully!")

    except InsufficientResourcesException as error:
        print("Error:", error)
        print(
            f"You need {error.required_amount - error.current_amount} more {error.required_resource}."
        )


player_resources = {"gold": 50, "silver": 20}

buying_resource("gold", 100, player_resources)
buying_resource("silver", 10, player_resources)

# Створити механізм обробки ситуацій, коли користувач намагається завершити операцію, для якої у нього
# недостатньо коштів на рахунку.

# Вимоги:

#     Створити клас InsufficientFundsException, наступний від виключеного базового класу.
#     Додайте наступні властивості:
#     required_amount: грошова сума, необхідна для виконання операції.
#     current_balance: поточний баланс рахунку.
#     Опціонально:
#     currency: валюта рахунку.
#     transaction_type: тип транзакції (наприклад, "withdrawal", "purchase").


class InsufficientFundsException(Exception):
    """Custom exception for handling situations when a user tries to complete
    a transaction for which they do not have enough funds in their account"""

    def __init__(
        self,
        required_amount: float,
        current_balance: float,
        currency: str = "UAH",
        transaction_type: str = "transaction",
    ) -> None:
        """Initialize the exception with details of the failed transaction.
        Attibutes:
            required_amount (float): the amount required to complete the transaction.
            current_balance (float): the current account balance.
            currency (str, optional): the currency of the account. Defaults to "UAH".
            transaction_type (str, optional): type of the transaction. Defaults to "transaction".
        """

        self.required_amount = required_amount
        self.current_balance = current_balance
        self.currency = currency
        self.transaction_type = transaction_type
        super().__init__(
            f"Insufficient funds for {self.transaction_type}. Required: {self.required_amount} {self.currency}, available: {self.current_balance} {self.currency}."
        )


def perform_transaction(
    amount: float,
    balance: float,
    currency: str = "UAH",
    transaction_type: str = "withdrawal",
):
    """
    Perform a transaction while handling insufficient funds internally.
    Returns updated balance or None if transaction failed.
    """
    try:
        if amount > balance:
            raise InsufficientFundsException(
                required_amount=amount,
                current_balance=balance,
                currency=currency,
                transaction_type=transaction_type,
            )
        balance -= amount
        print(f"Transaction successful. New balance: {balance} {currency}")
        return balance
    except InsufficientFundsException as error:
        print(error)
        return None


perform_transaction(1000, 500, "UAH", "withdrawal")
perform_transaction(5000, 5999, "USD", "purchase")
