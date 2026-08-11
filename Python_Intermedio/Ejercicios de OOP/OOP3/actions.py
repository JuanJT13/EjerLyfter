from student import Student


def register_students(students_list):
    name = input("Inserte el nombre: ")
    section = input("Inserte la sección: ")

    spanish = float(input("Nota de Español: "))
    english = float(input("Nota de Inglés: "))
    social_studies = float(input("Nota de Estudios Sociales: "))
    science = float(input("Nota de Ciencias: "))

    student = Student(
        name,
        section,
        spanish,
        english,
        social_studies,
        science
    )

    students_list.append(student)

    print("Estudiante registrado correctamente.")


def view_all_students(students_list):
    if not students_list:
        print("No hay estudiantes registrados.")
        return

    for student in students_list:
        print("------------------------")
        print(f"Nombre: {student.name}")
        print(f"Sección: {student.section}")
        print(f"Español: {student.spanish}")
        print(f"Inglés: {student.english}")
        print(f"Estudios Sociales: {student.social_studies}")
        print(f"Ciencias: {student.science}")