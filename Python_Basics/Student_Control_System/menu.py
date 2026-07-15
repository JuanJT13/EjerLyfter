def show_menu():
    """Prints the main menu options."""
    print("\n==================== STUDENT CONTROL SYSTEM ====================")
    print("1. Register new students")
    print("2. View all students")
    print("3. View Top 3 students (highest averages)")
    print("4. View general average of all students")
    print("5. Export data to CSV")
    print("6. Import data from CSV")
    print("7. Exit")
    print("=================================================================")

def get_menu_option():
    """Asks for and validates the user's menu choice."""
    while True:
        try:
            option = int(input("Select an option (1-7): "))
            if 1 <= option <= 7:
                return option
            else:
                print("[INVALID] Please choose a number between 1 and 7.")
        except ValueError:
            print("[INVALID] Please enter a valid number.")