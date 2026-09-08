import csv

def export_to_csv(file_name, students_list):
    """Exports the list of students to a CSV file."""
    try:
        with open(file_name, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            # Write header
            writer.writerow(["Name", "Section", "Spanish", "English", "Social Studies", "Science"])
            # Write student data
            for student in students_list:
                writer.writerow([
                    student["name"],
                    student["section"],
                    student["grades"]["spanish"],
                    student["grades"]["english"],
                    student["grades"]["social_studies"],
                    student["grades"]["science"]
                ])
        print(f"\n[SUCCESS] Data successfully exported to '{file_name}'!")
    except IOError:
        print("\n[ERROR] Could not write to the file. Please check permissions.")

def import_from_csv(file_name):
    """Imports students from a CSV file and returns a list of dictionaries."""
    students_list = []
    try:
        with open(file_name, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            header = next(reader) # Skip the header
            for row in reader:
                if len(row) == 6:
                    student = {
                        "name": row[0],
                        "section": row[1],
                        "grades": {
                            "spanish": float(row[2]),
                            "english": float(row[3]),
                            "social_studies": float(row[4]),
                            "science": float(row[5])
                        }
                    }
                    students_list.append(student)
        print(f"\n[SUCCESS] Successfully imported {len(students_list)} students from '{file_name}'!")
        return students_list
    except FileNotFoundError:
        print(f"\n[WARNING] No previous export file found with the name '{file_name}'.")
        return []
    except (csv.Error, ValueError):
        print("\n[ERROR] The file is corrupted or has an invalid format.")
        return []