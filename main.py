import os, sqlite3
from User import *


# TODO: The system must be able to handle and record transactions in a database,
#  add and remove money from balance,
#  record all purchases including their category,
#  plot a pie chart to determine the proportion of purchases of different categories.
#  Integrate CGI to make html for gui


def start():
    user = User("John", 22)

    print(f"{user.name}, {user.age}")


if __name__ == '__main__':
    start()
