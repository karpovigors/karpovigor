import cmath
import csv
import random
import json

# Нахождение корней квадратного уравнения
def quadratic_roots(a, b, c):
    discriminant = cmath.sqrt(b**2 - 4*a*c)
    root1 = (-b + discriminant) / (2*a)
    root2 = (-b - discriminant) / (2*a)
    return root1, root2

# Генерация csv файла с тремя случайными числами в каждой строке
def generate_csv(filename, lines=100):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for _ in range(lines):
            writer.writerow([random.randint(1, 100) for _ in range(3)])

# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла
def process_csv_quadratic(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    a, b, c = map(int, row)
                    print(f"For a={a}, b={b}, c={c} -> Roots are: {func(a, b, c)}")
        return wrapper
    return decorator

# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл
def save_to_json(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'w') as file:
                json.dump({"parameters": args, "result": result}, file)
            return result
        return wrapper
    return decorator

@save_to_json('results.json')
@process_csv_quadratic('numbers.csv')
def quadratic_roots_with_csv(a, b, c):
    return quadratic_roots(a, b, c)

# Генерация файла CSV для тестирования
generate_csv('numbers.csv', 10)

# Вызов функции для обработки CSV и сохранения результатов
quadratic_roots_with_csv(0, 0, 0)  # Эти параметры не используются, но необходимы из-за декоратора.
