import csv

from student import Student


def import_from_csv(file_path):
    students_list = []

    try:
        with open(file_path, "r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)

            for student_data in reader:
                student = Student.from_dict(student_data)
                students_list.append(student)

        print("Estudiantes importados correctamente.")

    except FileNotFoundError:
        print("No se encontró el archivo.")

    return students_list


def export_to_csv(file_path, students_list):
    fieldnames = [
        "name",
        "section",
        "spanish",
        "english",
        "social_studies",
        "science"
    ]

    with open(file_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        writer.writeheader()

        for student in students_list:
            writer.writerow(student.to_dict())

    print("Estudiantes exportados correctamente.")