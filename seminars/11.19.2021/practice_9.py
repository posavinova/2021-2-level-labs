"""
Programming 2021
Seminar 9
OOP: Encapsulation and Classes Practice
"""


class Student:

    def __init__(self, name: str, last_name: str, group_name: str, age: int):
        self.name = name
        self.last_name = last_name
        self.group_name = group_name
        self.age = age
        self._grades = {}

    def study(self):
        print(f'{self.name} is studying!')

    def sleep(self):
        print(f'{self.name} is sleeping!')

    def do_homework(self):
        print(f'{self.name} is doing homework!')

    def _change_name(self, new_name: str):
        self.name = new_name

    def add_grade(self, subject: str, grade: int):
        if not isinstance(subject, str) or not isinstance(grade, int):
            print('INVALID VALUE')
            return
        if subject in self._grades:
            self._grades[subject].append(grade)
        else:
            self._grades[subject] = [grade]

    def __str__(self):
        return self.name + ' ' + self.last_name


student1 = Student('Andrej', 'K', '17FPL1', 22)
student1.add_grade('math', 7)

student2 = Student('Noah', 'B', '20FPL1', 19)
student2.add_grade('math', 10)


class StudentGroup:
    def __init__(self, group_name: str):
        self.group_name = group_name
        self.max_number_of_students = 15
        self.monitor = None
        self.number_of_students = 0
        self.list_of_students = []

    def add_student(self, student: Student):
        self.number_of_students += 1
        self.list_of_students.append(student)


student1 = Student('Andrej', 'K', '20FPL3', 22)
group1 = StudentGroup('20FPL3')
print(group1.number_of_students)
group1.add_student(student1)
print(group1.number_of_students)
print(group1.list_of_students)
