import collections
import re

# Урок 3

print("Домашнее задание 1.")
# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.


def get_duplicates(lst_1):
    # Создаем пустое множество, чтобы отслеживать увиденные элементы
    seen = set()
    # Создаем множество дубликатов, добавляя в него только те элементы,
    # которые встречаются более одного раза
    duplicates = set(
        x for x in lst_1 if x in seen or seen.add(x)
    )
    # Преобразуем множество дубликатов обратно в список и возвращаем его
    return list(duplicates)


# Тестирование функции
lst = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7]
print(get_duplicates(lst))  # вывод: [2, 4, 6]

print("Домашнее задание 2.")


# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

def top_words(txt, n=10):
    # Разбиваем текст на слова, игнорируя знаки препинания и регистр
    words = re.findall(r'\w+', txt.lower())
    # Создаем счетчик, который подсчитывает количество каждого слова в списке
    counter = collections.Counter(words)
    # Возвращаем n наиболее часто встречающихся слов
    return counter.most_common(n)


# Тестирование функции
text = ("The Python programming language is an interpreted high-level general-purpose "
        "programming language. Python's design philosophy emphasizes code readability "
        "with its notable use of significant indentation. Its language constructs as well as its "
        "object-oriented approach aim to help programmers write clear, logical code "
        "for small and large-scale projects.")
print(top_words(text))
# вывод: [('python', 2), ('programming', 2), ('language', 2), ('its', 2), ('code', 2),
# ('the', 1), ('is', 1), ('an', 1), ('interpreted', 1), ('high', 1)]

print("Домашнее задание 3.")
# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.


def knapsack(items_1, max_weight_1):
    # Вспомогательная функция для вычисления решения задачи рюкзака
    def helper(i, w):
        if i < 0 or w == 0:
            return set()
        item, weight = items_1[i]
        if weight > w:
            return helper(i - 1, w)
        else:
            without_item = helper(i - 1, w)
            with_item = helper(i - 1, w - weight) | {item}
            if sum(items_dict[x] for x in with_item) > sum(items_dict[x] for x in without_item):
                return with_item
            else:
                return without_item

    # Вызываем вспомогательную функцию с начальными параметрами и возвращаем ее результат
    return helper(len(items) - 1, max_weight_1)


# Создаем словарь со списком вещей и их массой
items_dict = {'tent': 10, 'water': 3, 'food': 4, 'clothes': 5, 'tools': 2}
# Определяем максимальную грузоподъемность рюкзака
max_weight = 15
# Создаем список пар (вещь, масса) из словаря
items = list(items_dict.items())

# Тестирование функции
print(knapsack(items, max_weight))  # вывод: {'tools', 'clothes', 'water', 'food'}
