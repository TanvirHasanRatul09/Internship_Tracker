import pyodbc

def get_connection():
    try:
        conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=DESKTOP-69P1AIV\\SQLEXPRESS;"
            "DATABASE=InternshipTrackerProject;"
            "Trusted_Connection=yes;"
        )

        return conn

    except pyodbc.Error as e:
        print("Database Error:", e)
        return None