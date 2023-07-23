# chess_module.py
import random

def is_solution(queens):
    # Для каждой пары ферзей проводится проверка на конфликт
    for i in range(8):
        for j in range(i + 1, 8):
            # Если ферзи находятся на одной линии (горизонтали, вертикали или диагонали), возвращается False
            if queens[i] == queens[j] or abs(queens[i] - queens[j]) == j - i:
                return False
    # Если конфликтов между ферзями нет, возвращается True
    return True

def generate_positions():
    # Создаётся список с позициями ферзей
    queens = list(range(1, 9))
    for _ in range(4):  # генерируются и выводятся 4 варианта расстановки
        # Позиции ферзей перемешиваются
        random.shuffle(queens)
        # Если текущая расстановка ферзей не является решением, происходит новое перемешивание
        while not is_solution(queens):
            random.shuffle(queens)
        # При успешной расстановке ферзей она выводится на экран
        print(f'Удачная расстановка: {queens}')

# Запуск генерации позиций
generate_positions()
