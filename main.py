from app import set_database
from utility import *
import sqlite3

set_database()

while True:
    print("""
1:add_student,
2:view_all_students,
3:view_by_class,
4:delete_student,
5:update_student
""")

    get = int(input("enter the number the required action:  "))

    if get == 1:
        add_student()
    elif get == 2:
        view_all()
    elif get ==3:
        view_by_class()
    elif get == 4:
        delete_student()
    elif get == 5:
        update_student()
    else:
        print("enter no=umber from 1 to 5 only.")