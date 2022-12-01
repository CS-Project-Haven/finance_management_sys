import sqlite3
from sqlite3 import Error


class DBHandler:

    @staticmethod
    def create_connection(db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

        return conn

    @staticmethod
    def create_table(conn, create_table_sql):
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    @staticmethod
    def initiate():
        database = r"D:\PycharmProjects\finance_management_sys\resources\database.db"

        sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                            id integer PRIMARY KEY,
                                            name text NOT NULL,
                                            begin_date text,
                                            end_date text
                                        ); """

        sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                            id integer PRIMARY KEY,
                                            name text NOT NULL,
                                            priority integer,
                                            status_id integer NOT NULL, 
                                            project_id integer NOT NULL, 
                                            begin_date text NOT NULL, 
                                            end_date text NOT NULL,
                                            FOREIGN KEY (project_id) REFERENCES projects (id)     
                                        );"""

        conn = DBHandler.create_connection(database)

        if conn is not None:

            DBHandler.create_table(conn, sql_create_projects_table)

            DBHandler.create_table(conn, sql_create_tasks_table)
        else:
            print("Error!\nCannot create the database connection.")

    if __name__ == '__DB_Handler__':
        initiate()
