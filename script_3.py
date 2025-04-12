class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and 
            course in self.courses_in_progress and 
            course in lecturer.courses_attached and 
            1 <= grade <= 10):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grade(self):
        if not self.grades:
            return 0
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        avg_grade = self._average_grade()
        courses_in_progress = ", ".join(self.courses_in_progress) if self.courses_in_progress else "Нет курсов"
        finished_courses = ", ".join(self.finished_courses) if self.finished_courses else "Нет завершенных курсов"
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
                f"Курсы в процессе изучения: {courses_in_progress}\n"
                f"Завершенные курсы: {finished_courses}")

    def __lt__(self, other):
        if isinstance(other, Student):
            return self._average_grade() < other._average_grade()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Student):
            return self._average_grade() <= other._average_grade()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Student):
            return self._average_grade() == other._average_grade()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Student):
            return self._average_grade() != other._average_grade()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Student):
            return self._average_grade() > other._average_grade()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Student):
            return self._average_grade() >= other._average_grade()
        return NotImplemented

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lectures_given = []
        self.grades = {}

    def give_lecture(self, course):
        if course in self.courses_attached:
            self.lectures_given.append(course)
            return f"Лекция по курсу {course} проведена"
        return "Ошибка: курс не закреплен за лектором"

    def _average_grade(self):
        if not self.grades:
            return 0
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        avg_grade = self._average_grade()
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {avg_grade:.1f}")

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self._average_grade() < other._average_grade()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self._average_grade() <= other._average_grade()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self._average_grade() == other._average_grade()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Lecturer):
            return self._average_grade() != other._average_grade()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self._average_grade() > other._average_grade()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Lecturer):
            return self._average_grade() >= other._average_grade()
        return NotImplemented

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and 
            course in self.courses_attached and 
            course in student.courses_in_progress):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}")

# Пример использования
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_lecturer = Lecturer('Petr', 'Akulinsky')
cool_lecturer.courses_attached += ['Python']

# Проверяющий ставит оценки за домашку
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

# Студент ставит оценки лектору
best_student.rate_lecturer(cool_lecturer, 'Python', 8)
best_student.rate_lecturer(cool_lecturer, 'Python', 9)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)

# Выводим информацию
print(best_student)
print()
print(cool_lecturer)
print()
print(cool_reviewer)
print()

# Пример сравнения
another_student = Student('John', 'Doe', 'male')
another_student.courses_in_progress += ['Python']
cool_reviewer.rate_hw(another_student, 'Python', 8)
cool_reviewer.rate_hw(another_student, 'Python', 8)

another_lecturer = Lecturer('Anna', 'Smith')
another_lecturer.courses_attached += ['Python']
best_student.rate_lecturer(another_lecturer, 'Python', 10)
best_student.rate_lecturer(another_lecturer, 'Python', 10)

print(f"best_student > another_student: {best_student > another_student}")
print(f"cool_lecturer < another_lecturer: {cool_lecturer < another_lecturer}")