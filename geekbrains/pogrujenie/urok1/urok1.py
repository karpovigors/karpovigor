# Урок 1

print("Задание 1.")
# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.


def check_triangle(side_a, side_b, side_c):
    if side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a:
        if side_a == side_b == side_c:
            return "Равносторонней треугольник"
        elif side_a == side_b or side_b == side_c or side_c == side_a:
            return "Равнобедренный треугольник"
        else:
            return "Разносторонний треугольник"
    else:
        return "Треугольник не существует"


a = float(input("Введите длину сторона треугольника a: \n"))
b = float(input("Введите длину сторона треугольника b: \n"))
c = float(input("Введите длину сторона треугольника c: \n"))

result_1_1 = check_triangle(a, b, c)
print(result_1_1)

print("Домашнее задание 2.")
# Напишите код, который запрашивает число и сообщает - является ли оно простым или составным.
# Используйте правило для проверки:
# "Число является простым, если делится нацело только на единицу и на себя."
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.


def composite_or_prime(num):
    if num < 0:
        return "Ошибка, вы ввели отрицательное число."
    if num > 100_000:
        return "Ошибка, вы ввели число больше 100 000."
    if num < 2:
        return "Число не является ни простым, ни составным."
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return "Число является составным."
    return "Число является простым."


num_1_2 = int(input("Введите число: \n"))

result_1_2 = composite_or_prime(num_1_2)
print(result_1_2)
