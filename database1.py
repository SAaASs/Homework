import sqlite3
from sqlite3 import Error
import random

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successfull")
    except Error as e:
        print(f"The error '{e}' occured")
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")

genders = ["male", "female"]
names = ["James","Robert","John","Michael","David","Mary","Patricia","Jennifer","Linda","Elizabeth","Richard","Joseph","Charles","Sarah","Karen","Nancy",]
def main():
    connection = create_connection("C:\\Programs\MIIT2022\sm_app.sqlite")

    create_student_table = """
    CREATE TABLE IF NOT EXISTS students (
      student_id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      department TEXT,
      mark1 INTEGER,
      mark2 INTEGER,
      mark3 INTEGER
    );
    """
    delete_students = """
    DELETE FROM students
    """
    delete_bad = """
    DELETE FROM students
    WHERE (mark1 + mark2 + mark3)/3 < 3.5
    """
    execute_query(connection,delete_students)
    "execute_query(connection, create_student_table)"
    for i in range(0, 14):
        create_student = """
        INSERT INTO
        students (name, department, mark1, mark2, mark3)
        VALUES
        ('{}', '{}', {}, {}, {})
        """.format(names[random.randint(1,len(names)-1)], "vish", random.randint(1,5),random.randint(1,5),random.randint(1,5))
        print(create_student)
        execute_query(connection, create_student)

        for line in execute_read_query(connection, "select * from students"):
            print(line)
    execute_query(connection,delete_bad)
    for line in execute_read_query(connection, "select * from students"):
        print(line)



if __name__ == "__main__":
    main()