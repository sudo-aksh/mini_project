import sqlite3

def add_student():

    ans = input("""are you confirm with your action?
enter OK of ok for yes, else type anoythong else : """)

    if ans not in ("OK","ok"):
        return
    else:

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
    ans = input("""are you confirm with your action?
enter OK of ok for yes, else type anoythong else : """)

    if ans not in ("OK","ok"):
        return
    else:

        conn = sqlite3.connect("database.db")

        curr = conn.cursor()

        curr.execute("SELECT * FROM students")
        rows = curr.fetchall()

        for row in rows:
            print(row)

def view_by_class():
    ans = input("""are you confirm with your action?
enter OK of ok for yes, else type anoythong else : """)

    if ans not in ("OK","ok"):
        return
    else:

        conn = sqlite3.connect("database.db")

        curr = conn.cursor()

        while True:
            class_ = int(input("enter the class of the student:  "))
            if 4<class_ <11:
                break
            else:
                print("enter class between 5 and 10")

        curr.execute(f"""SELECT * FROM students
                    WHERE class = {class_}""")
        
        rows = curr.fetchall()

        for row in rows:
            print(row)

def delete_student():
    ans = input("""are you confirm with your action?
enter OK of ok for yes, else type anoythong else : """)

    if ans not in ("OK","ok"):
        return
    else:

        conn = sqlite3.connect("database.db")

        curr = conn.cursor()

        id_ = int(input("enter the id of the student you want o delete: "))

        curr.execute(f"""DELETE FROM students 
                    WHERE id = {id_}""")
        
        conn.commit()

def update_student():
    ans = input("""are you confirm with your action?
enter OK of ok for yes, else type anoythong else : """)

    if ans not in ("OK","ok"):
        return
    else:

        conn = sqlite3.connect("database.db")

        curr = conn.cursor()

        id = int(input("enter id of the student:"))

        name = input("enter the name:")

        while True:
            class_ = int(input("enter the class of the student:  "))
            if 4<class_ <11:
                break
            else:
                print("enter class between 5 and 10")

        email = input("enter email for the student:")

        conn.execute(f"""
    UPDATE students
    SET name= ?, class = ?,email = ?
    WHERE id = ?""",
    (name,class_,email,id))

        conn.commit()