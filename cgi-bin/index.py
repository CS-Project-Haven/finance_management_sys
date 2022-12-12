#!/cgi-bin/index
import cgi
import datetime

import matplotlib.pyplot as plt
import numpy as np
import mpld3
from Item import Item
from DBHandler import *

form = cgi.FieldStorage()

name = form.getvalue('user_name')
balance = form.getvalue('balance')

item_name = form.getvalue('item_name')
category = form.getvalue('category')
item_price = form.getvalue('item_price')
date = datetime.datetime.now()
date = date.strftime("%x")

def user_details():
    db_handler = DBHandler()
    db_handler.connect()


def build_pie():
    db_handler = DBHandler()
    db_handler.connect()
    # item = Item(item_name, balance, category, item_price, date)
    db_handler.db.execute("INSERT INTO item(item_name, category_name, item_price, date)\
                                    values(?, ?, ?, ?)",
                          (item_name, category, item_price, date))

    labels = ["Clothing", "Sports", "Leisure", "Foodstuff", "Travel"]
    temp = [1, 1, 1, 1, 1]
    values = []

    category_col = db_handler.db.execute("SELECT category_name, count(category_name)\
                                        FROM item GROUP by category_name")
    for i in category_col:
        temp.append(i)
    for k in values:
        values.append(k[1])

    # plt.draw()
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(values, labels=labels, startangle=90)
    plt_html = mpld3.fig_to_html(fig)
    plt.close(plt_html)
    plt.ion()
    return plt_html


class Index:

    def display_pie(self):
        db_handler = DBHandler()
        db_handler.connect()
        # db_handler.db.execute("SELECT * FROM item")

    def display_table(self):
        pass

    print("Content-type:text/html\n\n")
    print("<html lang='en'>")
    print("<head>")
    print("""
    <link rel="apple-touch-icon" sizes="180x180" href="favicons/apple-touch-icon.png">
    <link rel="icon" type="image/png" sizes="32x32" href="favicons/favicon-32x32.png">
    <link rel="icon" type="image/png" sizes="16x16" href="favicons/favicon-16x16.png">
    <link rel="manifest" href="favicons/site.webmanifest">
    """)
    print("<title>Finance Manager | </title>")
    print("<meta charset='UTF-8'>")
    print("<script src='https://cdn.tailwindcss.com'></script>")
    print("<script>")
    print("""
    tailwind.config = {
       theme: {
          extend: {
             colors: {
                royal_2: '#243b55',
             },
             fontFamily: {
                'righteous': ['Righteous', 'Display'],
             },
         },
       },
    };
    """)
    print("</script>")
    print("<style>")
    print("""
    @import url('https://fonts.googleapis.com/css2?family=Righteous&display=swap');
    @tailwind base;
    @tailwind components;
    @tailwind utilities;
    
    
    """)
    print("</style>")
    print("</head>")

    print("<body>")
    print("<h1 class='text-center text-slate-600 font-righteous text-3xl m-2'>Finance System</h1>")
    print("""
    
    <div class='container mx-auto border-2 border-black w-3/4 flex'>
        <form class='flex flex-col m-3 action='display_pie()' method='POST'>
        
            <div class='pt-4'>
                <h2 class='text-xl m-2 font-bold underline underline-offset-2'>User</h2>
                <label class='text-xl p-2' for=''>Name:</label><br>
                    <input class='m-2 border shadow' type='' id='' name='user_name' required><br>
                <label class='text-xl p-2' for=''>Balance:</label><br>
                    <input class='m-2 border shadow' type='' id='' name='balance' required><br>
            </div>
            
            <div class='pt-4'>
                <h2 class='text-xl m-2 font-bold underline underline-offset-2'>Item</h2>
                <label class='text-xl p-2' for=''>Item Name:</label><br>
                    <input class='m-2 border shadow' type='' id='' name='item_name' required><br>
                <label class='text-xl p-2' for=''>Category:</label><br>
                <select class = 'm-2 text-xl border shadow' id='category' name='category' required>
                    <option value="">None</option>
                    <option value="clothing">Clothing</option>
                    <option value="sports">Sports</option>
                    <option value="leisure">Leisure</option>
                    <option value="foodstuff">Foodstuff</option>
                    <option value="travel">Travel</option>
                    
                </select><br>
                <label class='text-xl p-2' for=''>Price:</label><br>
                    <input class='m-2 border shadow' type='' id='' name='item_price' required><br>
                <div class='text-center'>
                    <input class='border-2 rounded-md p-2 w-auto' href= """ + build_pie() + """ type = 'submit' value = 'Submit'>
                </div>
            </div>
        </form>
        
        <div class='flex flex-wrap items-center justify-center ml-auto m-3'>
            """ +  + """
        </div>
        
        
        
    </div>
    """)

    print("</body>")
    print("</html>")
