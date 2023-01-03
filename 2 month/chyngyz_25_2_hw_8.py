import sqlite3


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as b:
        print(b)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


database = 'hw.db'
sql_create_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price DOUBLE(10,2) NOT NULL DEFAULT 0.0,
quantity DOUBLE(10) NOT NULL DEFAULT 0
)
'''


def create_products(conn, products):
    try:
        sql = '''INSERT INTO products (product_title, price, quantity) 
        VALUES (?, ?, ?)'''
        cursor = conn.cursor()
        cursor.execute(sql, products)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def update_quantity(conn, products):
    try:
        sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, products)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def update_price(conn, products):
    try:
        sql = '''UPDATE products SET price = ? WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, products)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def delete_products(conn, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def select_all_products(conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def select_products_by_limits(conn, price_limit, quantity_limit):
    try:
        sql = '''SELECT * FROM products WHERE price <= ? and quantity >= ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (price_limit, quantity_limit))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


def select_products_by_product_title(conn, select):
    try:
        sql = '''SELECT * FROM products WHERE product_title = ?'''
        cursor = conn.cursor()
        cursor.execute(sql, (select,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as e:
        print(e)


connection = create_connection(database)
if connection is not None:
    # create_table(connection, sql_create_products_table)
    # create_products(connection, ('Сахар ', 43.99, 17))
    # create_products(connection, ('Соль', 30.99, 27))
    # create_products(connection, ('Мука', 524.99, 57))
    # create_products(connection, ('Рис', 112.99, 67))
    # create_products(connection, ('Кефир', 59.99, 93))
    # create_products(connection, ('Картофель', 25.99, 63))
    # create_products(connection, ('Жидкое мыло', 49.99, 27))
    # create_products(connection, ('Бананы', 74.99, 28))
    # create_products(connection, ('Сгущенка', 125.99, 27))
    # create_products(connection, ('Творог', 174.99, 27))
    # create_products(connection, ('Лук', 19.99, 46))
    # create_products(connection, ('Яблоки', 72.99, 47))
    # create_products(connection, ('Молоко ', 59.99, 83))
    # create_products(connection, ('Шоколад ', 74.99, 36))
    # create_products(connection, ('Чай', 65.99, 13))
    # update_quantity(connection, (45, 5))
    # update_price(connection, (76, 5))
    # delete_products(connection, 5)
    # select_products_by_limits(connection, 100, 50)
    # select_all_products(connection)
    # select_products_by_product_title(connection, ('Мука'))
    print('Done')
    connection.close()
