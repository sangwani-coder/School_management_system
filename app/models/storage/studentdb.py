#!/usr/bin/env python3
"""DB class"""
import sqlite3
import os 


class DB():
    """ DB class"""

    def __init__(self):
        """constructor"""
        try:
            path = 'db.sqlite3'
            dbdir = os.path.dirname(__file__)
            db_path = os.path.join(dbdir, path)
            os.makedirs(os.path.dirname(db_path), exist_ok=True)
            self.engine = sqlite3.connect(db_path)

        except Exception as e:
            print('failed to initialize DB', e)

    # create a database connection to the SQLITE database
    def create_connection(self):
        conn = None
        try:
            conn = self.engine
            print("connected to sqlite: ", sqlite3.version)
            return conn
        except Exception as s:
            print('Error: failed to connect to DB', s)    
        return conn

    # function to create tables
    def create_table(self, create_table_sql):
        """ create a table from the create_table_sql statement
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            conn = self.engine
            c = conn.cursor()
            c.execute(create_table_sql)
        except Exception as o:
            print("something wrong in table create table function", o)
                    
    # function to INSERT into rows
    def insert_data(self, data, values):
        try:
            conn = self.engine
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
            print("error in inserting data", t)