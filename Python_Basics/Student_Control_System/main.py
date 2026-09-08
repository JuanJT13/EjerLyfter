import menu
import actions
import data

def main():
    # Local list that holds our student data
    students_list = []
    # Local variable for the filename (no hardcoded path, just local filename)
    csv_filename = "students.csv"

    while True:
        menu.show_menu()
        option = menu.get_menu_option()

        if option == 1:
            actions.register_students(students_list)
        elif option == 2:
            actions.view_all_students(students_list)
        elif option == 3:
            actions.view_top_three(students_list)
        elif option == 4:
            actions.view_general_average(students_list)
        elif option == 5:
            data.export_to_csv(csv_filename, students_list)
        elif option == 6:
            # We assign the imported list back to our main list
            students_list = data.import_from_csv(csv_filename)
        elif option == 7:
            print("\nThank you for using the Student Control System. Goodbye!")
            break

if __name__ == "__main__":
    main()