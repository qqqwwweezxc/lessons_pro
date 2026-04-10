from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client["school"]
collection = db["users"]


collection.drop()


collection.insert_one({"name": "Vitos", "email": "vitos@example.com", "age": 25})
collection.insert_one({"name": "Anna", "email": "anna@example.com", "age": 30})


for doc in collection.find():
    print(doc)


collection.update_one({"name": "Vitos"}, {"$set": {"age": 26}})
print(collection.find_one({"name": "Vitos"}))


collection.delete_one({"name": "Anna"})


for doc in collection.find():
    print(doc)


collection.drop()
client.close()

# NoSQL (MongoDB)
# Переваги:

# Гнучка схема — кожен документ може мати різну структуру, легко ітерувати
# Горизонтальне масштабування — шардинг, розподіл даних на багато серверів
# JSON-подібний формат — природний для веб-додатків (API ↔ JSON ↔ MongoDB)
# Вкладені документи — зберігаємо складні структури в одному документі без JOIN
# Швидка розробка — не потрібно міграцій для кожної зміни

# Недоліки:

# Слабші транзакності — хоча підтримуються, але не такі надійні як ACID
# Немає JOIN — зв’язки доводиться робити вручну ($lookup незручний)
# Дублювання даних — часто доводиться дублювати дані в документах
# Більше споживання пам’яті — кожен документ зберігає всі ключі