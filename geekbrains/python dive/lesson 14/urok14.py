import csv

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
                print("Ошибка при добавлении оценки:", InvalidGradeError())
        else:
            raise InvalidSubjectError(subject_name)

    def add_test_result(self, subject_name, result):
        if subject_name in self.subjects:
            try:
                self.subjects[subject_name].add_test_result(result)
            except InvalidTestResultError:
                print("Ошибка при добавлении результата теста:", InvalidTestResultError())
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

# Пример использования
if __name__ == "__main__":
    import doctest
    import unittest
    import pytest

    # Код с тестами для doctest
    def run_tests():
        """
        >>> student = Student('subjects.csv')
        >>> student.name = "Иван Иванов"

        >>> student.add_grade("Математика", 4)
        >>> student.add_grade("Математика", 5)
        >>> student.add_test_result("Математика", 90)

        >>> student.add_grade("Физика", 3)
        >>> student.add_test_result("Физика", 85)

        >>> student.average_grade('Математика')
        4.5
        >>> student.average_grade('Физика')
        3.0
        >>> student.overall_average_grade()
        3.625
        """
        pass

    doctest.testmod()

    class TestStudentMethods(unittest.TestCase):
        def setUp(self):
            self.student = Student('subjects.csv')
            self.student.name = "Иван Иванов"

        def test_add_grade(self):
            self.student.add_grade("Математика", 4)
            self.assertEqual(self.student.average_grade('Математика'), 4.0)

        def test_add_test_result(self):
            self.student.add_test_result("Математика", 90)
            self.assertEqual(self.student.average_test_result('Математика'), 90.0)

        def test_invalid_grade(self):
            with self.assertRaises(InvalidGradeError):
                self.student.add_grade("Математика", 6)

        def test_invalid_test_result(self):
            with self.assertRaises(InvalidTestResultError):
                self.student.add_test_result("Математика", 105)

        def test_invalid_subject(self):
            with self.assertRaises(InvalidSubjectError):
                self.student.add_grade("История", 5)

    unittest.main()

    def test_add_grade():
        student = Student('subjects.csv')
        student.name = "Иван Иванов"
        student.add_grade("Математика", 4)
        assert student.average_grade('Математика') == 4.0

    def test_add_test_result():
        student = Student('subjects.csv')
        student.name = "Иван Иванов"
        student.add_test_result("Математика", 90)
        assert student.average_test_result('Математика') == 90.0

    def test_invalid_grade():
        student = Student('subjects.csv')
        student.name = "Иван Иванов"
        with pytest.raises(InvalidGradeError):
            student.add_grade("Математика", 6)

    def test_invalid_test_result():
        student = Student('subjects.csv')
        student.name = "Иван Иванов"
        with pytest.raises(InvalidTestResultError):
            student.add_test_result("Математика", 105)

    def test_invalid_subject():
        student = Student('subjects.csv')
        student.name = "Иван Иванов"
        with pytest.raises(InvalidSubjectError):
            student.add_grade("История", 5)
