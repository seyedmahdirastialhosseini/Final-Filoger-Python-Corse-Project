import mysql.connector
from mysql.connector import errorcode

mydb = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="Abtin.abtin1",
    database="databasename",
    auth_plugin="mysql_native_password"
)
mycursor = mydb.cursor()

student = """CREATE TABLE IF NOT EXISTS student (
    student_id INT AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    PRIMARY KEY (student_id)
);"""

teacher = """CREATE TABLE IF NOT EXISTS teacher (
    teacher_id INT AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(255) NOT NULL,
    lesson VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    PRIMARY KEY (teacher_id)
);"""

course = """CREATE TABLE IF NOT EXISTS course (
    course_id INT AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    time VARCHAR(255) NOT NULL,
    teacher_id INT,
    PRIMARY KEY (course_id),
    FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id)
);"""

mycursor.execute(student)
mycursor.execute(teacher)
mycursor.execute(course)

class Student:
    def __init__(self, name, age, email, phone, address):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone
        self.address = address

    def add(self):
        sql = "INSERT INTO student (name, age, email, phone, address) VALUES (%s, %s, %s, %s, %s)"
        val = (self.name, self.age, self.email, self.phone, self.address)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Student inserted.")

    def delete(self, rname):
        sql = "DELETE FROM student WHERE name = %s"
        val = (rname,)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Student deleted.")

    def update(self):
        sql = ("UPDATE student SET name = %s, age = %s, email = %s, phone = %s, address = %s")
        val = (self.name, self.age, self.email, self.phone, self.address)
        mycursor.execute(sql, val)
        mydb.commit()

    def show(self):
        mycursor.execute("SELECT * FROM student")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)

    def advance_search_with_query(self, query):
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)

class Teacher:
    def __init__(self, name, age, email, phone, lesson, address):
        self.name = name
        self.age = age
        self.email = email
        self.phone = phone
        self.lesson = lesson
        self.address = address

    def add(self):
        sql = "INSERT INTO teacher (name, age, email, phone, lesson, address) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (self.name, self.age, self.email, self.phone, self.lesson, self.address)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Teacher inserted.")

    def delete(self, rname):
        sql = "DELETE FROM teacher WHERE name = %s"
        val = (rname,)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Teacher deleted.")

    def update(self):
        sql = ("UPDATE teacher SET name = %s, age = %s, email = %s, phone = %s, lesson = %s, address = %s")
        val = (self.name, self.age, self.email, self.phone, self.lesson, self.address)
        mycursor.execute(sql, val)
        mydb.commit()

    def show(self):
        mycursor.execute("SELECT * FROM teacher")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)

    def advance_search_with_query(self, query):
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)

class Course:
    def __init__(self, name, time, teacher_id):
        self.name = name
        self.time = time
        self.teacher_id = teacher_id

    def add(self):
        sql = "INSERT INTO course (name, time, teacher_id) VALUES (%s, %s, %s)"
        val = (self.name, self.time, self.teacher_id)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Course inserted.")

    def delete(self, rname):
        sql = "DELETE FROM course WHERE name = %s"
        val = (rname,)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Course deleted.")

    def update(self):
        sql = ("UPDATE course SET name = %s, time = %s, teacher_id = %s")
        val = (self.name, self.time, self.teacher_id)
        mycursor.execute(sql, val)
        mydb.commit()

    def show(self):
        mycursor.execute("SELECT * FROM course")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)

    def advance_search_with_query(self, query):
        mycursor.execute(query)
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)

def panel():
    while True:
        print("choose what do you want to do ")
        print('1. Student')
        print('2. Teacher')
        print('3. Course')
        print('4. Exit')
        choice = input("Enter your choice: ")
        if choice == '1':
            print('what do you want to do with student?')
            print('1. Add')
            print('2. Delete')
            print('3. Update')
            print('4. Show')
            print('5. Advance Search')
            print('6. Back')
            choice = input("Enter your choice: ")
            if choice == '1':
                name = input("Enter name: ")
                age = input("Enter age: ")
                email = input("Enter email: ")
                phone = input("Enter phone: ")
                address = input("Enter address: ")
                student = Student(name, age, email, phone, address)
                student.add()
            elif choice == '2':
                name = input("Enter name: ")
                student.delete(rname)

            elif choice == '3':
                name = input("Enter name: ")
                age = input("Enter age: ")
                email = input("Enter email: ")
                phone = input("Enter phone: ")
                address = input("Enter address: ")
                student = Student(name, age, email, phone, address)
                student.update()
            elif choice == '4':
                student = Student('', '', '', '', '')
                student.show()
            elif choice == '5':
                query = input("Enter your query: ")
                student = Student('', '', '', '', '')
                student.advance_search_with_query(query)
            elif choice == '6':
                panel()
            else:
                print("Invalid choice")

        elif choice == '2':
            print('what do you want to do with teacher?')
            print('1. Add')
            print('2. Delete')
            print('3. Update')
            print('4. Show')
            print('5. Advance Search')
            print('6. Back')
            choice = input("Enter your choice: ")
            if choice == '1':
                name = input("Enter name: ")
                age = input("Enter age: ")
                email = input("Enter email: ")
                phone = input("Enter phone: ")
                lesson = input("Enter lesson: ")
                address = input("Enter address: ")
                teacher = Teacher(name, age, email, phone, lesson, address)
                teacher.add()
            elif choice == '2':
                name = input("Enter name: ")
                teacher = Teacher(name, '', '', '', '', '')
                teacher.delete()
            elif choice == '3':
                name = input("Enter name: ")
                age = input("Enter age: ")
                email = input("Enter email: ")
                phone = input("Enter phone: ")
                lesson = input("Enter lesson: ")
                address = input("Enter address: ")
                teacher = Teacher(name, age, email, phone, lesson, address)
                teacher.update()
            elif choice == '4':
                teacher = Teacher('', '', '', '', '', '')
                teacher.show()
            elif choice == '5':
                query = input("Enter your query: ")
                teacher = Teacher('', '', '', '', '', '')
                teacher.advance_search_with_query(query)
            elif choice == '6':
                panel()
            else:
                print("Invalid choice")






panel()

