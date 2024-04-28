import sqlite3

# Соединение с базой данных
conn = sqlite3.connect('database.db')
print("База данных открыта успешно")

# Создание курсора
cursor = conn.cursor()

# Создание таблицы пользователей
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
''')
print("Таблица пользователей создана успешно")

# Закрытие соединения
conn.close()