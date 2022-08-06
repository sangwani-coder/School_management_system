#!/usr/bin/env python3
""" db schema"""

from .studentdb import DB


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

def create_schema():
    """ creates database and tables"""
    db = DB()
    try: 
        # create a database connection
        db.create_connection()
        # create students table
        db.create_table(f"{sql_create_student_table}")
        # create parents table
        db.create_table(sql_create_parent_table)
        # create teachers table
        db.create_table(sql_create_teacher_table)
        # create accounts table
        db.create_table(sql_create_accounts_table)
        # create classes table
        db.create_table(sql_create_classes_table)
        # create class table
        db.create_table(sql_create_class_table)
        print("Datebase tables created successfully")
    except Exception as e:
        print("Error in schema:", e)

if __name__ == "__main__":
    create_schema()