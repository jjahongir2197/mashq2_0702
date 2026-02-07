class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def average(self):
        return sum(self.grades.values()) / len(self.grades) if self.grades else 0


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject


class School:
    def __init__(self):
        self.students = []
        self.teachers = []

    def add_student(self, s):
        self.students.append(s)

    def add_teacher(self, t):
        self.teachers.append(t)

    def report(self):
        for s in self.students:
            print(s.name, "| O‘rtacha:", round(s.average(), 2))


school = School()
school.add_student(Student("Jahongir"))
school.students[0].add_grade("Math", 5)
school.students[0].add_grade("Python", 5)
school.report()
