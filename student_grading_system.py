"""
Student Grading System 🎓
👤 Author: PJ (@pjprogrammers)
📄 License: MIT
🔗 GitHub Profile: https://github.com/pjprogrammers
🔗 GitHub Repo: https://github.com/pjprogrammers/python
Description: A simple interactive program that asks for student names and marks,
then assigns grades based on the marks using standard grading criteria.
"""

def main():
    """
    Main function to run the grading system.
    It asks how many students there are, takes each student's name and marks,
    then prints their grade accordingly.
    """

    # Ask the user for the total number of students
    try:
        n = int(input("Enter Number Of Students ➟ "))
    except ValueError:
        print("⚠️ Invalid input. Please enter a valid integer for the number of students.")
        return  # Exit if input is invalid

    # Loop through each student to get their name and marks
    for i in range(1, n + 1):
        # Ask for the student's name
        student_name = input(f"Enter Name Of Student {i} ➟ ").strip()

        # Ask for the student's marks, expecting a floating point number
        try:
            marks = float(input(f"Enter Marks Of Student {i} ➟ "))
        except ValueError:
            print("⚠️ Invalid marks. Please enter a valid number.")
            continue  # Skip to next student if marks input is invalid

        # Determine and print the grade based on the marks
        if 80 <= marks <= 100:
            print(f"{student_name} - Grade A 🏆")
        elif 70 <= marks < 80:
            print(f"{student_name} - Grade B 🎉")
        elif 50 <= marks < 70:
            print(f"{student_name} - Grade C 👍")
        elif 35 <= marks < 50:
            print(f"{student_name} - Grade D")
        elif 0 <= marks < 35:
            print(f"{student_name} - Reappear 🔄")
        else:
            # Marks outside 0-100 range are invalid
            print(f"⚠️ Invalid marks for {student_name}. Please enter marks between 0 and 100.")

if __name__ == "__main__":
    main()
