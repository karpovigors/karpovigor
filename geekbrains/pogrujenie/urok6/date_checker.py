# date_checker.py
import sys
from datetime import datetime

def check_date(date_str):
    # Происходит попытка преобразования строки в дату по заданному формату
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        # В случае неудачного преобразования возвращается False
        return False

# Проверка, был ли модуль запущен напрямую, а не импортирован
if __name__ == "__main__":
    # Вызов функции проверки даты с аргументом, переданным из командной строки
    print(check_date(sys.argv[1]))
