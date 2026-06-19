from database import get_connection


def generate_report():

    conn = get_connection()

    try:

        cursor = conn.cursor()

        #passed applicants
        cursor.execute(
            """
            SELECT COUNT(*)
            FROM Interview
            WHERE result = 'Passed'
            """
        )

        passed = cursor.fetchone()[0]

        #pending applicants
        cursor.execute(
            """
            SELECT COUNT(*)
            FROM Interview
            WHERE result = 'Pending'
            """
        )

        pending = cursor.fetchone()[0]

        #failed applicants
        cursor.execute(
            """
            SELECT COUNT(*)
            FROM Interview
            WHERE result = 'Failed'
            """
        )

        failed = cursor.fetchone()[0]

        print("\n===== REPORT =====")
        print(f"Passed           : {passed}")
        print(f"Pending          :{pending}")
        print(f"Failed           :{failed}")

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()