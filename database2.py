import psycopg2
import random
import datetime
names = ["name1","name2","name3","name4","name5","name6","name7","name8","name9","name10","name11","name12","name13","name14","name15","name16"]
specializations = ["spec1","spec2","spec3","spec4","spec5","spec6","spec7","spec8","spec9","spec10","spec11","spec12","spec13","spec14","spec15","spec16"]
def rand_date(switch):
    if switch > 0:
        return datetime.datetime.now().replace(month = 1, day = 1) + datetime.timedelta(days=random.randint(1,730))
    else:
        return datetime.datetime.now().replace(month = 1, day = 1) - datetime.timedelta(days=random.randint(1,730))

class Employee:
    def __init__(self, name, age, specialization, list_of_jobs, id):
        self.name = name
        self.age = age
        self.specialization = specialization
        self.list_of_jobs = list_of_jobs
        self.id = id
    @staticmethod
    def create_random():
        new_worker = Employee(names[random.randint(len(names))], random.randint(18,65), specializations[random.randint(len(specializations))], [], random.randint(0,11111111111))
        return new_worker


class Registry:
    def __init__(self, reg_name):
        self.name = reg_name

    def main(self):
        connection = psycopg2.connect(
            database="SHAD112_V9",
            user="shad112_V9",
            password="123",
            host="91.190.239.132",
            port="5432"
        )
        print("Database opened successfully")

        cur = connection.cursor()
        cur.execute('''
        DROP TABLE IF EXISTS companies
        ''')
        cur.execute('''
        CREATE TABLE companies (
          company_id INT NOT NULL GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
          company_name VARCHAR(100) NOT NULL,
          company_desc VARCHAR(10000)
       );
        ''')
        cur.execute('''
        INSERT INTO companies (company_name, company_desc) VALUES
        ('rzhd', 'trains, railroads'),
        ('aeroflot', 'planes, clouds'),
        ('yandex go', 'cars, roads')
        ''')
        print(cur.execute("select * from companies"))
        cur.execute('''
        DROP TABLE IF EXISTS work_sessions
        ''')
        cur.execute('''
        CREATE TABLE work_sessions (
        employee_id INTEGER,
        company_id INTEGER REFERENCES companies (company_id),
        start_date DATE,
        speciality VARCHAR(1000),
        salary REAL,
        end_date DATE
        );
        ''')
        connection.close()
    def comp_mass(self):
        connection = psycopg2.connect(
            database="SHAD112_V9",
            user="shad112_V9",
            password="123",
            host="91.190.239.132",
            port="5432"
        )
        cur = connection.cursor()
        print(cur.execute("select * from companies"))
        connection.close()
    def add_employee(self, current_employee):
        connection = psycopg2.connect(
            database="SHAD112_V9",
            user="shad112_V9",
            password="123",
            host="91.190.239.132",
            port="5432"
        )
        cur = connection.cursor()



        cur.execute('''
        INSERT INTO work_sessions (employee_id, company_id, start_date, speciality, salary, end_date) VALUES
        ('{}', '{}', '{}', '{}', '{}', '{}')
        '''.format(current_employee.id, "", rand_date(-1), current_employee.specialization, random.randint(16242, 999999), rand_date(1)))




        connection.close()
Register = Registry("First")
Register.main()
