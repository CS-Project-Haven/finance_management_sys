from User import User
from DBHandler import *
from Item import Item

from http.server import HTTPServer, CGIHTTPRequestHandler


# TODO: The system must be able to handle and record transactions in a database,
#  add and remove money from balance,
#  record all purchases including their category,
#  plot a pie chart to determine the proportion of purchases of different categories.
#  Integrate CGI to make html for gui

class Main:
    class CGIHandler(CGIHTTPRequestHandler):
        cgi_directories = ["/cgi-bin"]

    def print_data(data):
        all_rows = data.fetchall()
        for row in all_rows:
            for i in row:
                print(i, end='  |   \t')
            print()
        print()

    def balance(self):
        pass

    def main(self):
        user = User(user_id=1, name="John", age=22, balance=100)
        item = Item(1, "Glasses", "Clothing", 12.50, "2022-12-04")
        db_handler = DBHandler()
        db_handler.connect()
        db_handler.create_tables()

        db_handler.db.execute("INSERT INTO user(name, age, balance)\
                                values(?, ?, ?)", (user.name, user.age, user.balance))
        db_handler.db.execute("INSERT INTO item(item_name, category_name, item_price, date)\
                                    values(?, ?, ?, ?)",
                              (item.item_name, item.category_name, item.item_price, item.date))

        # user_data = db_handler.db.execute("SELECT * FROM user")
        # print_data(user_data)
        # item_data = db_handler.db.execute("SELECT * FROM item")
        # print_data(item_data)

        HTTPServer(("", 8081), Main.CGIHandler).serve_forever()

if __name__ == '__main__':
    main = Main()
    main.main()