import sqlite3

def init_db():
    connection = sqlite3.connect("app.db")
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        )
    """)
    connection.commit()
    connection.close()
    return connection, cursor

init_db()
