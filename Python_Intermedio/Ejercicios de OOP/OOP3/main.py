from actions import register_students, view_all_students
from data import import_from_csv, export_to_csv


def main():
    students = []

    while True:
        print("\nSistema de Control de Estudiantes")
        print("1. Registrar estudiante")
        print("2. Ver estudiantes")
        print("3. Importar estudiantes")
        print("4. Exportar estudiantes")
        print("5. Salir")

        option = input("Seleccione una opción: ")

        if option == "1":
            register_students(students)

        elif option == "2":
            view_all_students(students)

        elif option == "3":
            students = import_from_csv("students.csv")

        elif option == "4":
            export_to_csv("students.csv", students)

        elif option == "5":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()