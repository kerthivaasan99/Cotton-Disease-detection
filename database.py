import sqlite3

# Function to create the required database structure
def create_db():
    conn = sqlite3.connect('cotton_disease.db')
    cursor = conn.cursor()

    # Create table for storing test results
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS test_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        disease TEXT
    )
    """)

    # Create table for storing consultancy requests
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS consultancy_requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        phone TEXT,
        message TEXT
    )
    """)

    conn.commit()
    conn.close()

# Run the function to create the database and tables
if __name__ == "__main__":
    create_db()
    print("Database created successfully.")
