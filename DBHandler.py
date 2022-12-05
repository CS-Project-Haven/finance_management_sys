import sqlite3


class DBHandler:

    def __init__(self):
        self.db = None
        self.conn = None

    def connect(self):
        db_file = r"D:\PycharmProjects\finance_management_sys\resources\database.db"
        self.conn = sqlite3.connect(db_file)
        self.db = self.conn.cursor()

    def close(self):
        self.conn.close()

    def create_tables(self):
        self.db.execute("""CREATE TABLE IF NOT EXISTS user (
                            user_id INTEGER PRIMARY KEY NOT NULL,
                            name TEXT NOT NULL,
                            age INTEGER,
                            balance INTEGER
                        );""")

        self.db.execute("""CREATE TABLE IF NOT EXISTS item (
                            item_id INTEGER PRIMARY KEY NOT NULL,
                            item_name TEXT NOT NULL,
                            category_name TEXT NOT NULL,
                            item_price FLOAT,
                            date DATE,
                            FOREIGN KEY (item_id) REFERENCES user (user_id)     
                        );""")
