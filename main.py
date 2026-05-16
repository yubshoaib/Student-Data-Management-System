import os

FILE_NAME = "students.txt"

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{roll},{marks}\n")

    print("Student added successfully!")

def view_students():
    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return

    with open(FILE_NAME, "r") as file:
        data = file.readlines()

    if not data:
        print("No student records.")
        return

    print("\nStudent Records:")
    for student in data:
        name, roll, marks = student.strip().split(",")
        print(f"Name: {name} | Roll No: {roll} | Marks: {marks}")

def delete_student():
    roll_to_delete = input("Enter roll number to delete: ")

    if not os.path.exists(FILE_NAME):
        print("No records found.")
        return

    with open(FILE_NAME, "r") as file:
        students = file.readlines()

    with open(FILE_NAME, "w") as file:
        found = False
        for student in students:
            name, roll, marks = student.strip().split(",")
            if roll != roll_to_delete:
                file.write(student)
            else:
                found = True

    if found:
        print("Student deleted successfully!")
    else:
        print("Student not found.")

while True:
    print("\n===== Student Data Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice.")