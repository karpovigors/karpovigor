import os

def parse_file_path(file_path):
    # Определяем путь, имя файла и его расширение
    path, filename = os.path.split(file_path)
    base, ext = os.path.splitext(filename)
    # Возвращаем кортеж из трех элементов
    return path, base, ext

# Тестирование функции
print(parse_file_path("/home/user/docs/file.txt"))  # вывод: ('/home/user/docs', 'file', '.txt')

def generate_bonus_dict(names, rates, bonuses):
    return {name: rate * float(bonus.rstrip('%')) / 100 for name, rate, bonus in zip(names, rates, bonuses)}

# Тестирование функции
names = ['John', 'Jane', 'Mike']
rates = [100, 200, 150]
bonuses = ['10%', '20%', '15%']
print(generate_bonus_dict(names, rates, bonuses))  # вывод: {'John': 10.0, 'Jane': 40.0, 'Mike': 22.5}

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Тестирование функции
fib = fibonacci()
print(next(fib))  # вывод: 0
print(next(fib))  # вывод: 1
print(next(fib))  # вывод: 1
print(next(fib))  # вывод: 2
print(next(fib))  # вывод: 3
