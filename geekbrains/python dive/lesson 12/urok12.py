import csv


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
            raise ValueError("Оценка должна быть от 2 до 5")

    def add_test_result(self, result):
        if 0 <= result <= 100:
            self.test_results.append(result)
        else:
            raise ValueError("Результат теста должен быть от 0 до 100")

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
            self.subjects[subject_name].add_grade(grade)
        else:
            raise ValueError(f"Предмет '{subject_name}' не существует")

    def add_test_result(self, subject_name, result):
        if subject_name in self.subjects:
            self.subjects[subject_name].add_test_result(result)
        else:
            raise ValueError(f"Предмет '{subject_name}' не существует")

    def average_grade(self, subject_name):
        if subject_name in self.subjects:
            return self.subjects[subject_name].average_grade()
        else:
            raise ValueError(f"Предмет '{subject_name}' не существует")

    def average_test_result(self, subject_name):
        if subject_name in self.subjects:
            return self.subjects[subject_name].average_test_result()
        else:
            raise ValueError(f"Предмет '{subject_name}' не существует")

    def overall_average_grade(self):
        total_grades = []
        for subject in self.subjects.values():
            total_grades.extend(subject.grades)
        if not total_grades:
            return None
        return sum(total_grades) / len(total_grades)


# Пример использования
if __name__ == "__main__":
    student = Student('subjects.csv')
    student.name = "Иван Иванов"  # Установка ФИО

    student.add_grade("Математика", 4)
    student.add_grade("Математика", 5)
    student.add_test_result("Математика", 90)

    student.add_grade("Физика", 3)
    student.add_test_result("Физика", 85)

    print(f"Средний балл по Математике: {student.average_grade('Математика')}")
    print(f"Средний балл по Физике: {student.average_grade('Физика')}")
    print(f"Общий средний балл: {student.overall_average_grade()}")
