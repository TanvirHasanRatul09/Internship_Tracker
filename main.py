from crud import (
    add_student,
    get_all_students,
    update_student,
    delete_student,
    add_interview,
    view_interviews
)
from report import generate_report
from search import search_by_status
from student import Student
from interview import Interview


def main():

    while True:

        print("\n===== INTERNSHIP TRACKER =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Applications By Status")
        print("6. Generate Report")
        print("7. Add or Update Interview")
        print("8. View Interviews")
        print("9. Exit")

        choice = input("Enter Choice: ")

        # Add Student
        if choice == "1":

            name = input("Name: ")
            email = input("Email: ")

            student = Student(name, email)

            add_student(student)

        # View Students
        elif choice == "2":

            get_all_students()

        # Update Student
        elif choice == "3":

            try:

                student_id = int(
                    input("Student ID: ")
                )

                name = input("New Name: ")
                email = input("New Email: ")

                update_student(
                    student_id,
                    name,
                    email
                )

            except ValueError:

                print("Invalid ID.")

        # Delete Student
        elif choice == "4":

            try:

                student_id = int(
                    input("Student ID: ")
                )

                delete_student(student_id)

            except ValueError:

                print("Invalid ID.")

        # Search Application By Status
        elif choice == "5":

            print("\nAvailable Statuses:")
            print("Applied")
            print("Under Review")
            print("Interview")
            print("Accepted")
            print("Rejected")
            print("Withdrawn")

            status = input(
                "\nEnter Status: "
            )

            search_by_status(status)

        # Generate Report
        elif choice == "6":

            generate_report()
        #Add interview
        elif choice == "7":

            try:

                application_id = int(
                    input("Application ID: ")
                )

                interview_date = input(
                    "Interview Date (YYYY-MM-DD): "
                )

                print("\nValid Results:")
                print("Pending")
                print("Passed")
                print("Failed")

                result = input("Result: ")

                interview = Interview(
                    application_id,
                    interview_date,
                    result
                )

                add_interview(interview)

            except ValueError:

                print("Invalid input.")

        #view interview
        elif choice == "8":

            view_interviews()

        # Exit
        elif choice == "9":

            print("Goodbye.")
            break

        else:

            print("Invalid Choice.")


if __name__ == "__main__":
    main()