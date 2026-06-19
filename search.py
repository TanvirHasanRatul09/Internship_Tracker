from database import get_connection


def search_by_status(status):

    conn = get_connection()

    try:

        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM Application
            WHERE Status = ?
            """,
            status
        )

        rows = cursor.fetchall()

        if not rows:
            print(f"No applications found with status '{status}'.")
            return

        print(f"\n===== APPLICATIONS : {status} =====")

        for row in rows:

            print(
                f"ApplicationID: {row.ApplicationID} | "
                f"StudentID: {row.StudentID} | "
                f"CompanyID: {row.CompanyID} | "
                f"Position: {row.Position} | "
                f"Status: {row.Status}"
            )

    except Exception as e:
        print("Error:", e)

    finally:
        conn.close()