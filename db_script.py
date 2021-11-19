import sqlite3
connection = sqlite3.connect('data.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE orders
             (order_date, order_number, order_email, food, qty, status)''')

orders = [('2021-11-18', 123,'tony@gmail.com','pizza',2,'cooking')]

cursor.executemany('INSERT INTO orders VALUES (?,?,?,?,?,?)', orders)

cursor.execute('''CREATE TABLE inventory
                    (qty, food)''')

inventory = [(3, 'pizza'),(3, 'boba'),(1, 'biriyani'),(1, 'ramen')]

cursor.executemany('INSERT INTO inventory VALUES (?,?)', inventory)

connection.commit()

connection.close()