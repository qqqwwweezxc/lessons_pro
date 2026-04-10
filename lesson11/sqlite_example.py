import sqlite3


conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        age INTEGER
    )
""")
conn.commit()


cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
               ("Vitos", "vitos@example.com", 25))
cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
               ("Anna", "anna@example.com", 30))
conn.commit()


cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)


cursor.execute("UPDATE users SET age = 26 WHERE name = 'Vitos'")
conn.commit()

cursor.execute("SELECT * FROM users WHERE name = 'Vitos'")
print(cursor.fetchone())


cursor.execute("DELETE FROM users WHERE name = 'Anna'")
conn.commit()

cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)


cursor.execute("DROP TABLE users")
conn.commit()
conn.close()

# SQL (SQLite3)
# Переваги:

# ACID-транзакції — гарантія цілісності даних (ідеально для фінансів, замовлень)
# Строга схема — дані завжди валідні, легко ловити помилки на ранньому етапі
# JOINs — потужні зв’язки між таблицями (користувач → замовлення → товари)
# Зрілість — стандартизований SQL, величезна екосистема інструментів
# SQLite — вбудований, нульова конфігурація, ідеальний для малих проектів

# Недоліки:

# Масштабування — вертикальне (потрібен потужніший сервер)
# Фіксована схема — зміна структури = міграції, ALTER TABLE
# Складність для ієрархічних/документних даних (JSON-дерева, вкладені об’єкти)