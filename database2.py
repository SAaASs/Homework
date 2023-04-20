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
print(rand_date(1))
class Employee:
    def __init__(self, name, age, specialization, list_of_jobs, id):
        self.name = name
        self.age = age
        self.specialization = specialization
        self.list_of_jobs = list_of_jobs
        self.id = id
    @staticmethod
    def create_random():
        new_worker = Employee(names[random.randint(0, len(names))-1], random.randint(18, 65), specializations[random.randint(0, len(specializations))-1], [], random.randint(0,11111))
        return new_worker
connection1 = psycopg2.connect(
            database="SHAD112_V9",
            user="shad112_V9",
            password="123",
            host="91.190.239.132",
            port="5432"
        )

class Registry:
    def __init__(self, connection, reg_name):
        self.name = reg_name
        self.connection = connection
        print("Database opened successfully")
    def main(self):
        cur = self.connection.cursor()
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
    def close_con(self):
        self.connection.close()
    def comp_mass(self):
        cur = self.connection.cursor()
        cur.execute("select * from companies")
        return cur.fetchall()
    def select_comp_emps2(self):
        current_table = self.work_sessions()
        mass1= []
        mass2 = []
        mass3 = []
        for i in range(0, len(current_table)):
            if (current_table[i][1] == 1) and datetime.datetime.now().date() < current_table[i][5]:
                mass1.append(employees[current_table[i][1]].name)
            if (current_table[i][1] == 2) and datetime.datetime.now().date() < current_table[i][5]:
                mass2.append(employees[current_table[i][1]].name)
            if (current_table[i][1] == 3) and datetime.datetime.now().date() < current_table[i][5]:
                mass3.append(employees[current_table[i][1]].name)
        print(mass1)
        print(mass2)
        print(mass3)
    def select_comp_emps(self, comp_num):
        for row in self.work_sessions():
            if int(row[1]) == comp_num:
                print(row)
    def work_sessions(self):
        cur = self.connection.cursor()
        cur.execute("select * from work_sessions")
        return cur.fetchall()
    def add_employment(self, current_employee):
        cur = self.connection.cursor()
        cur.execute('''
        INSERT INTO work_sessions (employee_id, company_id, start_date, speciality, salary, end_date) VALUES
        ('{}', '{}', '{}', '{}', '{}', '{}')
        '''.format(current_employee.id, self.comp_mass()[random.randint(0,2)][0], rand_date(-1), current_employee.specialization, random.randint(16242, 999999), rand_date(1)))
employees= []
for i in range(0,7):
    employees.append(Employee.create_random())




Register = Registry(connection1 ,"First")

Register.main()
print(Register.comp_mass())
print("------------------------")
Register.add_employment(employees[0])
Register.add_employment(employees[1])
Register.add_employment(employees[2])
Register.add_employment(employees[3])
Register.add_employment(employees[4])
Register.add_employment(employees[5])
Register.add_employment(employees[6])
for row in Register.work_sessions():
    print(row)
print("---------------")
Register.select_comp_emps(1)
print("---------------")
Register.select_comp_emps(2)
print("---------------")
Register.select_comp_emps(3)


Register.select_comp_emps2()

Register.close_con()
