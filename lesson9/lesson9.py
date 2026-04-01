import re
from collections import Counter

# Напишіть функцію, яка перевіряє, чи є email-адреса валідною. Email вважається валідним, 
# якщо він має формат example@domain.com
def valid_email(email: str) -> bool:
    """Function checks if the email address is valid"""
    return bool(re.match(r"[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*@[a-zA-Z0-9]+\.[a-z]{2,6}", email))


print(valid_email("example@domain.com"))


# Напишіть функцію, яка знаходить усі телефонні номери в тексті. Номери можуть бути в форматах:

# (123) 456-7890
# 123-456-7890
# 123.456.7890
# 1234567890
text = """
Hello world! Hello world!
121
(123) 456-7890
123-456-7890
123.456.7890
1234567890
1255
"""


def find_number_of_phones(text: str) -> list:
    """Function finds all phone numbers in the text"""
    return re.findall(r"\(?\d{3}\)?[\s().-]?\d{3}[\s.-]?\d{4}", text)


print(find_number_of_phones(text))


# Напишіть функцію, яка з тексту повертає список хеш-тегів. Хеш-тег — це слово, що починається з #, 
# і може включати лише букви та цифри.
def list_of_hashtags(text: str) -> list:
    """Function finds all hashtags in text"""
    return re.findall(r"#[a-zA-Z0-9]+", text)


hashtags = """
#hello world

Today is #sunny121 and #warm
"""


print(list_of_hashtags(hashtags))


# Напишіть функцію, яка перетворює дати з формату DD/MM/YYYY у формат YYYY-MM-DD.
def convert_date(date: str) -> str:
    """Function convert date from formate DD/MM/YYYY to YYYY/MM/DD"""
    day, month, year = date.split("/")
    return f"{year}-{month}-{day}"


print(convert_date("24/10/2000"))


# Напишіть функцію, яка видаляє всі HTML-теги з тексту.
def delete_html_tags(text: str) -> str:
    """Deletes all html tags from text"""
    return re.sub(r"<[^>]+>", "", text)


html_text = """
<header>
<p1> kdsksks <p1>
<main> Hello world<main>
<h6> kskdks </h6>
"""


print(delete_html_tags(html_text))


# Напишіть функцію, яка перевіряє, чи є пароль надійним. Пароль вважається надійним, якщо він:

#     містить як мінімум 8 символів,
#     містить принаймні одну цифру,
#     має хоча б одну велику літеру та одну малу,
#     містить хоча б один спеціальний символ (@, #, $, %, &, тощо).
def is_good_password(password: str) -> bool:
    """Function checks if the password is strong"""
    if len(password) < 8:
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[@#$%&*]", password):
        return False
    return True


print(is_good_password("Paassword1#"))
print(is_good_password("notgoodpassword"))


# Напишіть функцію, яка з тексту витягує всі IPv4-адреси. IPv4-адреса складається з чотирьох чисел 
# (від 0 до 255), розділених крапками.
def find_all_ipv4(text: str) -> list:
    """Function finds all IPv4 ip adresses in text"""
    return re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", text)


ipv4 = "192.168.1.1 some text some text 8.8.8.8 text text text 172.16.254.1"
print(find_all_ipv4(ipv4))


# Напишіть функцію, яка вилучає всі URL з заданого тексту.
def find_all_url(text: str) -> list:
    """Function finds all urls in text"""
    return re.findall(r"https?://[^\s,]+", text)


urls = """
Hello world! Hello world! Hello world!
Hello world! https://www.example.com Hello world!
http://www.example.com Hello world!
https://example.com Hello world!
http://google.com
https://github.com/user/repo Hello world!
Hello world! https://stackoverflow.com/questions/12345/test
"""


print(find_all_url(urls))


# Напишіть програму, яка аналізує лог-файл веб-сервера та виводить статистику за кількістю запитів з різних IP-адрес.
def analyze_log_file(log_filename: str) -> dict:
    """
    Function analyzes the web server log file and displays statistics 
    on the number of requests from different IP addresses
    """

    with open(log_filename, "r", encoding="utf-8") as log_file:
        data = log_file.read()

    ip_addresses = re.findall(r"\b(?:\d{1,3}\.){3}\d{1,3}\b", data)
    return dict(Counter(ip_addresses))


for ip, count in analyze_log_file("./lesson6/log_file.txt").items():
    print(f"{ip}: {count}")


# Спробуйте створити свої власні регулярні вирази для вирішення різноманітних завдань, наприклад, для пошуку 
# певних слів у тексті, для перевірки формату даних тощо.
def find_all_words(text: str, word: str) -> list:
    """Function for finds any words in text"""
    return re.findall(rf"\b{word}\b", text)


test_text = "some text cat in some text cat hello world! test text cat"
print(find_all_words(test_text, "cat"))