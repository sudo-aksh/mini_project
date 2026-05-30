import sqlite3

def set_database():
    conn = sqlite3.connect("database.db")

    curr = conn.cursor()


    curr.execute(f"""CREATE TABLE IF NOT EXISTS students
    (id INTEGER PRIMANRY KEY,
    name TEXT NOT NULL,
    class INTEGER NOT NULL CHECK,
    email TEXT UNIQUE NOT NULL)""")

    conn.commit()
    conn.close()