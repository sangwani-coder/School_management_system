import sqlite3

STUDENT_DB = "student.db"


# create a database connection to the SQLITE database
def create_connect():
    conn = None
    try:
        conn = sqlite3.connect(STUDENT_DB)
        return conn
    except Exception as s:
        print(s)
    finally:
        print("connected to sqlite: ", sqlite3.version)

    return conn


# function to create tables
def create_table(create_table_sql):
    """ create a table from the create_table_sql statement
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        conn = sqlite3.connect(STUDENT_DB)
        c = conn.cursor()
        c.execute(create_table_sql)
    except Exception as o:
        print(o)
        print("something wrong in table create table function")


# function to INSERT into rows
def insert_data(data, values):
    try:
        conn = sqlite3.connect(STUDENT_DB)
        # insert into student table
        if data == "student":
            sql = """ INSERT INTO students(parent_id, class_id, firstname, surname, DoB, gender, address, class)
                        VALUES(?,?,?,?,?,?,?,?) """
        # insert into teacher table
        elif data == "teacher":
            sql = """ INSERT INTO teachers(title, class_id, firstname, surname, mobile, email, class)
                                VALUES(?,?,?,?,?,?,?) """

        # insert into parent table
        elif data == "parent":
            sql = """ INSERT INTO parents(title, names, tel_home, tel_work, email, relationship)
                                        VALUES(?,?,?,?,?,?) """

        # insert into classes table
        elif data == "classes":
            sql = """ INSERT INTO classes(grade, block, room, tuition) VALUES(?,?,?,?) """

        # insert into class table
        elif data == "class":
            sql = """INSERT INTO class(class_id, student_id, firstname, surname, DoB, gender, tuition) 
                        VALUES(?,?,?,?,?,?,?,?) """

        # insert into account table
        elif data == "account":
            sql = """ INSERT INTO accounts(student_id, std_name, class, tuition, paid, paid_date)
                        VALUES(?,?,?,?,?,?) """
        cur = conn.cursor()
        cur.execute(sql, values)
        conn.commit()

    except Exception as t:
        print(t)
        print("error in inserting data")


def main():
    try:
        # create students table
        sql_create_student_table = """CREATE TABLE IF NOT EXISTS students (
                                            id INTEGER PRIMARY KEY,
                                            parent_id INTEGER NOT NULL,
                                            class_id INTEGER NOT NULL,
                                            firstname TEXT NOT NULL,
                                            surname TEXT NOT NULL,
                                            DoB TEXT,
                                            gender TEXT,
                                            address TEXT,
                                            class TEXT,
                                            FOREIGN KEY (parent_id) REFERENCES parents(id),    
                                            FOREIGN KEY (class_id) REFERENCES classes(id) 
                                            )"""

        # create parents table
        sql_create_parent_table = """CREATE TABLE IF NOT EXISTS parents (
                                            id INTEGER PRIMARY KEY,
                                            title TEXT,
                                            names TEXT,
                                            tel_home TEXT,
                                            tel_work TEXT,
                                            email TEXT,
                                            relationship TEXT                                    
                                            )"""

        # create teacher table
        sql_create_teacher_table = """CREATE TABLE IF NOT EXISTS teachers (
                                                id INTEGER PRIMARY KEY,
                                                class_id INTEGER,
                                                title TEXT,
                                                firstname TEXT,
                                                surname TEXT,
                                                mobile TEXT,
                                                email TEXT,
                                                class TEXT,
                                                FOREIGN KEY (class_id) REFERENCES classes(id)                                      
                                                )"""

        # create accounts table
        sql_create_accounts_table = """CREATE TABLE IF NOT EXISTS accounts (
                                                id INTEGER PRIMARY KEY,
                                                student_id INTEGER NOT NULL,
                                                std_name TEXT,
                                                class TEXT,
                                                tuition FLOAT,
                                                paid FLOAT,
                                                paid_date TEXT NOT NULL,    
                                                FOREIGN KEY (student_id) REFERENCES students(id)    
                                                )"""

        # create classes table
        sql_create_classes_table = """ CREATE TABLE IF NOT EXISTS classes (
                                            id INTEGER PRIMARY KEY,
                                            grade TEXT,
                                            teacher TEXT,
                                            block TEXT,
                                            room TEXT,   
                                            tuition INTEGER  
                                            )"""

        # create class table
        sql_create_class_table = """ CREATE TABLE IF NOT EXISTS class (
                                                id PRIMARY KEY,
                                                class_id INTEGER NOT NULL,
                                                student_id INTEGER NOT NULL,
                                                teacher_id INTEGER NOT NULL,
                                                firstname TEXT NOT NULL,
                                                surname TEXT NOT NULL,
                                                DoB TEXT,
                                                gender TEXT,   
                                                tuition TEXT,
                                                FOREIGN KEY (student_id) REFERENCES students(id),
                                                FOREIGN KEY (teacher_id) REFERENCES teachers(id),
                                                FOREIGN KEY (class_id) REFERENCES classes(id)                                  
                                                )"""

        # create a database connection
        create_connect()
        # create tables
        # create students table
        create_table(f"{sql_create_student_table}")

        # create parents table
        create_table(sql_create_parent_table)

        # create teachers table
        create_table(sql_create_teacher_table)

        # create accounts table
        create_table(sql_create_accounts_table)

        # create classes table
        create_table(sql_create_classes_table)

        # create class table
        create_table(sql_create_class_table)

    except Exception as p:
        print(p)
        print("something went wrong")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
