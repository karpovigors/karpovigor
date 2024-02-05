import sqlite3

def get_db_schema(db_name):
    # Подключение к базе данных
    conn = sqlite3.connect(db_name)

    # Создание объекта курсора
    cursor = conn.cursor()

    # Получение списка всех таблиц
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    schema = {}

    for table in tables:
        table_name = table[0]
        # Получение информации о столбцах для каждой таблицы
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        # Сохранение названий столбцов
        schema[table_name] = [column[1] for column in columns]

    conn.close()

    return schema

db_schema = get_db_schema('db.sqlite3')

# Вывод схемы базы данных
for table, columns in db_schema.items():
    print(f"Table: {table}")
    for column in columns:
        print(f"    Column: {column}")
