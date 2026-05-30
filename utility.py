import sqlite3

def add_student():
    conn = sqlite3.connect("database.db")

    curr = conn.cursor()

    id = int(input("enter a uniqe id for the student: "))
    name = input("enter the name of the stduent: ")
    while True:
        class_ = int(input("enter the class of the student:  "))
        if 4<class_ <11:
            break
        else:
            print("enter class between 5 and 10")

    email = input("enter email for the student: ")
    

    curr.execute(f"""
INSERT INTO students(id,name,class,email)
VALUES(?,?,?,?)
""",
(id,name,class_,email))
    
    conn.commit()
    
def view_all():
    conn = sqlite3.connect("database.db")

    curr = conn.cursor()

    curr.execute("SELECT * FROM students")
    rows = curr.fecthall()

    for row in rows:
        print(row)

def view_by_class():
    conn = sqlite3.connect("database.db")

    curr = conn.cursor()
    get_class = int(input("enter the class to veiw all studets of the class:  "))

    curr.execute(f"""SELECT * FROM students
                 WHERE class = {get_class}""")
    
    rows = curr.fecthall()

    for row in rows:
        print(row)

def delete_student():
    conn = sqlite3.connect("database.db")

    curr = conn.cursor()

    id_ = int(input("enter the id of the student you want o delete: "))

    curr.execute(f"""DELETE FROM students 
                 WHERE id = {id_}""")
    
    conn.commit()