class Student:
    def __init__(self, name, score_1):
        self.name = name
        self.score_1 = score_1


def create_student(students_list):
    name = input("Inserte su nombre: ")
    score_1 = float(input("Inserte su nota: "))

    student = Student(name, score_1)
    students_list.append(student)


students = []

create_student(students)

for student in students:
    print(f"Nombre: {student.name}")
    print(f"Nota: {student.score_1}")