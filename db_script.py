import sqlite3
connection = sqlite3.connect('data.db')

cursor = connection.cursor()

cursor.execute('''CREATE TABLE orders
             (order_date, order_number, order_email, food, qty, status)''')

orders = [('2021-11-18', 456,'tony@gmail.com','pizza','large','cooking'),
          ('2021-11-18',457,'bob@gmail.com','burger', 'small', 'queue still'),
          ('2021-11-18',458,'me@gmail.com','boba', 'regular', 'out for delivery'),
          ]

cursor.executemany('INSERT INTO orders VALUES (?,?,?,?,?,?)', orders)

cursor.execute('''CREATE TABLE inventory
                    (qty, food)''')

inventory = [('large', 'pizza'),('regular', 'boba'),('small', 'burger')]

cursor.executemany('INSERT INTO inventory VALUES (?,?)', inventory)

connection.commit()

connection.close()