class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if (
            isinstance(lecturer, Lecturer)
            and course in self.courses_in_progress
            and course in lecturer.courses_attached
            and 1 <= grade <= 10
        ):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

    def _average_grade(self):
        if not self.grades:
            return 0
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def __str__(self):
        avg_grade = self._average_grade()
        courses_in_progress = (
            ", ".join(self.courses_in_progress)
            if self.courses_in_progress
            else "Нет курсов"
        )
        finished_courses = (
            ", ".join(self.finished_courses)
            if self.finished_courses
            else "Нет завершенных курсов"
        )
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за домашние задания: {avg_grade:.1f}\n"
            f"Курсы в процессе изучения: {courses_in_progress}\n"
            f"Завершенные курсы: {finished_courses}\n"
        )

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
        return (
            f"Имя: {self.name}\n"
            f"Фамилия: {self.surname}\n"
            f"Средняя оценка за лекции: {avg_grade:.1f}\n"
        )

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
        if (
            isinstance(student, Student)
            and course in self.courses_attached
            and course in student.courses_in_progress
        ):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        return f"Имя: {self.name}\n" f"Фамилия: {self.surname}"


# Функции для подсчета средней оценки
def average_hw_grade(students, course):
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    return sum(total_grades) / len(total_grades) if total_grades else 0


def average_lecture_grade(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])
    return sum(total_grades) / len(total_grades) if total_grades else 0


# Создадим студентов
student1 = Student("Ruoy", "Eman", "male")
student1.courses_in_progress += ["Python", "Git"]
student1.finished_courses += ["Введение в программирование"]

student2 = Student("Anna", "Smith", "female")
student2.courses_in_progress += ["Python"]
student2.finished_courses += ["Математика"]

# Проверяющих
reviewer1 = Reviewer("Some", "Buddy")
reviewer1.courses_attached += ["Python", "Git"]

reviewer2 = Reviewer("John", "Doe")
reviewer2.courses_attached += ["Python"]

# Лекторов
lecturer1 = Lecturer("Petr", "Akulinsky")
lecturer1.courses_attached += ["Python"]

lecturer2 = Lecturer("Maria", "Akulinskaya")
lecturer2.courses_attached += ["Python", "Git"]

# Вызовем методы, сказано всех - все и вызовем... Хотя это перебор кажется.
# Проверяющие ставят оценки студентам
reviewer1.rate_hw(student1, "Python", 10)
reviewer1.rate_hw(student1, "Python", 9)
reviewer1.rate_hw(student1, "Git", 8)
reviewer2.rate_hw(student2, "Python", 7)
reviewer2.rate_hw(student2, "Python", 8)

# Студенты оценивают лекторов
student1.rate_lecturer(lecturer1, "Python", 8)
student1.rate_lecturer(lecturer1, "Python", 9)
student2.rate_lecturer(lecturer1, "Python", 10)
student1.rate_lecturer(lecturer2, "Python", 7)
student1.rate_lecturer(lecturer2, "Git", 9)

# Лекторы проводят лекции
print(lecturer1.give_lecture("Python"))
print(lecturer2.give_lecture("Git")) 
print(lecturer2.give_lecture("Python"))

# Вывод информации о каждом объекте
print("\nИнформация об объектах:")
print(student1)
print(student2)
print(reviewer1)
print(reviewer2)
print(lecturer1)
print(lecturer2)

# Сравнение студентов и лекторов
print("\nСравнение:")
print(f"student1 > student2: {student1 > student2}")
print(f"lecturer1 < lecturer2: {lecturer1 < lecturer2}")

# Вызываем функции для подсчета средних оценочек студентов и лекторов
students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]

print("\nСредние оценки:")
print(
    f"Средняя оценка за ДЗ по курсу Python: {average_hw_grade(students_list, 'Python'):.1f}"
)
print(
    f"Средняя оценка за лекции по курсу Python: {average_lecture_grade(lecturers_list, 'Python'):.1f}"
)
print(
    f"Средняя оценка за ДЗ по курсу Git: {average_hw_grade(students_list, 'Git'):.1f}"
)
print(
    f"Средняя оценка за лекции по курсу Git: {average_lecture_grade(lecturers_list, 'Git'):.1f}"
)
