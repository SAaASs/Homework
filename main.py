import  psycopg2
import random
connection1 = psycopg2.connect(
            database="SHAD112_V9",
            user="shad112_V9",
            password="123",
            host="91.190.239.132",
            port="5432"
        )


cur = connection1.cursor()

def init():
    cur.execute('''
            DROP TABLE IF EXISTS EXAMS CASCADE
            ''')
    cur.execute('''
            CREATE TABLE EXAMS (
              exam_id INT NOT NULL GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
              exam_name VARCHAR(100) NOT NULL,
              exam_info VARCHAR(10000)
           );
            ''')
    cur.execute('''
            DROP TABLE IF EXISTS STUDENTS CASCADE
            ''')
    cur.execute('''
            CREATE TABLE STUDENTS (
              student_id INT NOT NULL GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
              student_name VARCHAR(100) NOT NULL,
              student_info VARCHAR(10000)
           );
            ''')
    cur.execute('''
            DROP TABLE IF EXISTS EXAM_LIST
            ''')
    cur.execute('''
            CREATE TABLE EXAM_LIST (
              id INT NOT NULL GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
              exam_id INT REFERENCES EXAMS (exam_id),
              student_id INT REFERENCES STUDENTS (student_id),
              result INT
           );
            ''')
    connection1.commit()
def createStudent(student_name, student_info):
    cur.execute('''
            INSERT INTO STUDENTS (student_name, student_info) VALUES
            ('{}', '{}')
            '''.format(str(student_name), str(student_info)))
    connection1.commit()
def createExam(exam_name, exam_info):
    cur.execute('''
            INSERT INTO EXAMS (exam_name, exam_info) VALUES
            ('{}', '{}')
            '''.format(str(exam_name), str(exam_info)))
    connection1.commit()

def getStudents():
    cur.execute('''SELECT * FROM STUDENTS''')
    return cur.fetchall()
def getExams():
    cur.execute(('''SELECT * FROM EXAMS'''))
    return cur.fetchall()
def Session():
    students=getStudents()
    exams=getExams()
    for i in range(0,len(students)):
        for u in range(0,len(exams)):
            cur.execute('''
            INSERT INTO EXAM_LIST (exam_id, student_id, result) VALUES
            ('{}', '{}', '{}')
            '''.format(students[i][0], exams[u][0], random.randint(2,5)))
    cur.execute('''SELECT * FROM EXAM_LIST''')
    connection1.commit()
    return cur.fetchall()
def fillStudents(amount):
    for i in range(0,amount):
        createStudent("name"+str(i), "testStudentInfo")
def fillExams(amount):
    for i in range(0,amount):
        createExam("exam"+str(i), "testExamInfo")


def getStudentExams(student_id):
    cur.execute('''SELECT student_name, exam_name, result FROM EXAM_LIST JOIN STUDENTS ON STUDENTS.student_id = EXAM_LIST.student_id JOIN EXAMS ON EXAM_LIST.exam_id = EXAMS.exam_id WHERE EXAM_LIST.student_id = {}'''.format(student_id))
    return cur.fetchall()


print('--------------------------')
print(getStudentExams(1))
print(getStudentExams(2))
print(getStudentExams(3))