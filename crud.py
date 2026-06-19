from interview import Interview
from database import get_connection


def add_student(student):
    if not student.validate():
        return

    conn = get_connection()

    try:
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO Student(Name, Email)
            VALUES (?, ?)
            """,
            student.name,
            student.email
        )

        conn.commit()

        print("Student added successfully.")

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()


def get_all_students():
    conn = get_connection()

    try:

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM Student
            """
        )

        rows = cursor.fetchall()

        if not rows:
            print("No students found.")
            return

        for row in rows:
            print(
                f"ID:{row.StudentID} | "
                f"Name:{row.Name} | "
                f"Email:{row.Email}"
            )

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()


def update_student(student_id, name, email):
    conn = get_connection()

    try:

        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE Student
            SET Name=?,
                Email=?
            WHERE StudentID = ?
            """,
            name,
            email,
            student_id
        )

        conn.commit()

        print("Student updated.")

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()


def delete_student(student_id):
    conn = get_connection()

    try:

        cursor = conn.cursor()

        cursor.execute(
            """
            DELETE
            FROM Student
            WHERE StudentID = ?
            """,
            student_id
        )

        conn.commit()

        print("Student deleted.")

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()


def add_interview(interview):

        if not interview.validate():
            return

        conn = get_connection()

        try:
            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO Interview
                    (ApplicationID, InterviewDate, Result)
                VALUES (?, ?, ?)
                """,
                interview.application_id,
                interview.interview_date,
                interview.result
            )

            conn.commit()

            print("Interview added successfully.")

        except Exception as e:
            print("Error:", e)

        finally:
            conn.close()

def view_interviews():

        conn = get_connection()

        try:

            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT *
                FROM Interview
                """
            )

            rows = cursor.fetchall()

            if not rows:
                print("No interviews found.")
                return

            for row in rows:
                print(
                    f"InterviewID: {row.InterviewID} | "
                    f"ApplicationID: {row.ApplicationID} | "
                    f"Date: {row.InterviewDate} | "
                    f"Result: {row.Result}"
                )

        except Exception as e:
            print("Error:", e)

        finally:
            conn.close()



