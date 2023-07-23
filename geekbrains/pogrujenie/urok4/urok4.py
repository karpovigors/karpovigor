def transpose(matrix):
    # Возвращает транспонированную матрицу
    return [list(row) for row in zip(*matrix)]

# Тестирование функции
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose(matrix))  # вывод: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

def args_to_dict(**kwargs):
    # Возвращает словарь, где ключ - значение переданного аргумента, а значение - имя аргумента
    return {value: key for key, value in kwargs.items()}

# Тестирование функции
print(args_to_dict(name='John', age=30, country='USA'))  # вывод: {'John': 'name', 30: 'age', 'USA': 'country'}

class ATM:
    def __init__(self):
        self.balance = 0
        self.operations = []

    def deposit(self, amount):
        self.balance += amount
        self.operations.append(('deposit', amount))

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient balance')
            return
        self.balance -= amount
        self.operations.append(('withdraw', amount))

    def print_balance(self):
        print(f'Your balance: {self.balance}')

    def print_operations(self):
        for operation, amount in self.operations:
            print(f'{operation}: {amount}')

# Тестирование функций
atm = ATM()
atm.deposit(100)
atm.withdraw(30)
atm.print_balance()  # вывод: Your balance: 70
atm.print_operations()  # вывод: deposit: 100, withdraw: 30
