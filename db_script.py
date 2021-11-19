import sqlite3
connection = sqlite3.connect('data.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE orders
             (order_date, order_number, order_email, brand, model, status)''')

orders = [('2021-11-18', 123,'tony@gmail.com','iphone',12,'shipped')]

cursor.executemany('INSERT INTO orders VALUES (?,?,?,?,?,?)', orders)

cursor.execute('''CREATE TABLE inventory
                    (brand, model)''')

inventory = [(6, 'iphone'),(7, 'iphone'),(8, 'iphone'),(9, 'iphone')]

cursor.executemany('INSERT INTO inventory VALUES (?,?)', inventory)

connection.commit()

connection.close()