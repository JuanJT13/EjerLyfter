def calculate_student_average(student):
    """Calculates the average grade of a single student."""
    grades = student["grades"].values()
    return sum(grades) / len(grades)

def get_valid_grade(subject_name):
    """Asks for a grade and validates that it is a number between 0 and 100."""
    while True:
        try:
            grade = float(input(f"Enter grade for {subject_name} (0-100): "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("[INVALID] Grade must be between 0 and 100. Try again.")
        except ValueError:
            print("[INVALID] Please enter a valid number.")

def register_students(students_list):
    """Allows registering multiple students one by one."""
    print("\n--- REGISTER NEW STUDENTS ---")
    while True:
        name = input("Enter student's full name (or press Enter to stop): ").strip()
        if name == "":
            break
            
        section = input("Enter section (e.g., 11B): ").strip().upper()
        if section == "":
            print("[ERROR] Section cannot be empty.")
            continue

        # Ask and validate each grade
        spanish = get_valid_grade("Spanish")
        english = get_valid_grade("English")
        social_studies = get_valid_grade("Social Studies")
        science = get_valid_grade("Science")

        new_student = {
            "name": name,
            "section": section,
            "grades": {
                "spanish": spanish,
                "english": english,
                "social_studies": social_studies,
                "science": science
            }
        }
        
        students_list.append(new_student)
        print(f"Student '{name}' registered successfully!\n")
        
        option = input("Do you want to register another student? (yes/no): ").strip().lower()
        if option != "yes" and option != "y":
            break

def view_all_students(students_list):
    """Prints the information of all registered students."""
    if not students_list:
        print("\n[INFO] No students registered yet.")
        return

    print("\n==================== REGISTERED STUDENTS ====================")
    for student in students_list:
        avg = calculate_student_average(student)
        print(f"Name: {student['name']} | Section: {student['section']}")
        print(f"  Grades -> Spanish: {student['grades']['spanish']} | English: {student['grades']['english']} | Social Studies: {student['grades']['social_studies']} | Science: {student['grades']['science']}")
        print(f"  Average: {avg:.2f}")
        print("-" * 60)

def view_top_three(students_list):
    """Displays the top 3 students with the highest averages."""
    if not students_list:
        print("\n[INFO] No students registered yet.")
        return

    # Sort students by average in descending order
    sorted_students = sorted(students_list, key=calculate_student_average, reverse=True)
    
    print("\n==================== TOP 3 STUDENTS ====================")
    for index, student in enumerate(sorted_students[:3], start=1):
        avg = calculate_student_average(student)
        print(f"{index}. {student['name']} (Section: {student['section']}) - Average: {avg:.2f}")

def view_general_average(students_list):
    """Displays the global average grade among all students."""
    if not students_list:
        print("\n[INFO] No students registered yet.")
        return

    total_averages = [calculate_student_average(s) for s in students_list]
    global_average = sum(total_averages) / len(total_averages)
    print(f"\n==================================================")
    print(f"The general average of all students is: {global_average:.2f}")
    print(f"==================================================")