from User import *
from DBHandler import *


# TODO: The system must be able to handle and record transactions in a database,
#  add and remove money from balance,
#  record all purchases including their category,
#  plot a pie chart to determine the proportion of purchases of different categories.
#  Integrate CGI to make html for gui


def main():
    user = User("John", 22)
    db_handler = DBHandler()
    db_handler.initiate()


if __name__ == '__main__':
    main()
