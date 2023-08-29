import csv
import logging
import argparse

# Исключение для неверной оценки
class InvalidGradeError(Exception):
    def __init__(self, message="Оценка должна быть от 2 до 5"):
        self.message = message
        super().__init__(self.message)

# Исключение для неверного результата теста
class InvalidTestResultError(Exception):
    def __init__(self, message="Результат теста должен быть от 0 до 100"):
        self.message = message
        super().__init__(self.message)

# Исключение для неправильного предмета
class InvalidSubjectError(Exception):
    def __init__(self, subject_name):
        self.subject_name = subject_name
        self.message = f"Предмет '{subject_name}' не существует"
        super().__init__(self.message)

# Дескриптор для проверки ФИО
class NameDescriptor:
    def __get__(self, instance, owner):
        return instance._name

    def __set__(self, instance, value):
        if not value.isalpha() or not value.istitle():
            raise ValueError("ФИО должно содержать только буквы и начинаться с заглавной буквы")
        instance._name = value

# Класс для хранения оценок и результатов тестов по предмету
class Subject:
    def __init__(self):
        self.grades = []
        self.test_results = []

    def add_grade(self, grade):
        if 2 <= grade <= 5:
            self.grades.append(grade)
        else:
            raise InvalidGradeError()

    def add_test_result(self, result):
        if 0 <= result <= 100:
            self.test_results.append(result)
        else:
            raise InvalidTestResultError()

    def average_grade(self):
        if not self.grades:
            return None
        return sum(self.grades) / len(self.grades)

    def average_test_result(self):
        if not self.test_results:
            return None
        return sum(self.test_results) / len(self.test_results)

# Класс студента
class Student:
    name = NameDescriptor()

    def __init__(self, csv_filename):
        self.subjects = {}
        self.load_subjects(csv_filename)

    def load_subjects(self, csv_filename):
        with open(csv_filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                subject_name = row[0]
                self.subjects[subject_name] = Subject()

    def add_grade(self, subject_name, grade):
        if subject_name in self.subjects:
            try:
                self.subjects[subject_name].add_grade(grade)
            except InvalidGradeError:
                logging.error(f"Ошибка при добавлении оценки для предмета '{subject_name}': {InvalidGradeError()}")
        else:
            raise InvalidSubjectError(subject_name)

    def add_test_result(self, subject_name, result):
        if subject_name in self.subjects:
            try:
                self.subjects[subject_name].add_test_result(result)
            except InvalidTestResultError:
                logging.error(f"Ошибка при добавлении результата теста для предмета '{subject_name}': {InvalidTestResultError()}")
        else:
            raise InvalidSubjectError(subject_name)

    def average_grade(self, subject_name):
        if subject_name in self.subjects:
            return self.subjects[subject_name].average_grade()
        else:
            raise InvalidSubjectError(subject_name)

    def average_test_result(self, subject_name):
        if subject_name in self.subjects:
            return self.subjects[subject_name].average_test_result()
        else:
            raise InvalidSubjectError(subject_name)

    def overall_average_grade(self):
        total_grades = []
        for subject in self.subjects.values():
            total_grades.extend(subject.grades)
        if not total_grades:
            return None
        return sum(total_grades) / len(total_grades)

def configure_logging(log_to_file=False):
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=log_format)
    
    if log_to_file:
        file_handler = logging.FileHandler('app.log')
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(logging.Formatter(log_format))
        logging.getLogger('').addHandler(file_handler)

def main():
    parser = argparse.ArgumentParser(description='Управление студентами.')
    parser.add_argument('--log_to_file', action='store_true', help='Записывать логи в файл app.log')

    args = parser.parse_args()

    configure_logging(log_to_file=args.log_to_file)

    try:
        student = Student('subjects.csv')
        student.name = "Иван Иванов"  # Установка ФИО

        student.add_grade("Математика", 4)
        student.add_grade("Математика", 5)
        student.add_test_result("Математика", 90)

        student.add_grade("Физика", 3)
        student.add_test_result("Физика", 105)  # Ошибка: результат теста выходит за допустимый диапазон

        print(f"Средний балл по Математике: {student.average_grade('Математика')}")
        print(f"Средний балл по Физике: {student.average_grade('Физика')}")
        print(f"Общий средний балл: {student.overall_average_grade()}")

    except InvalidGradeError as e:
        logging.error(f"Ошибка: {e}")

    except InvalidTestResultError as e:
        logging.error(f"Ошибка: {e}")

    except InvalidSubjectError as e:
        logging.error(f"Ошибка: {e}")

    except ValueError as e:
        logging.error(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
