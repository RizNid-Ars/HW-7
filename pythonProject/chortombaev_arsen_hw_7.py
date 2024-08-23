import sqlite3


def create_table(db_file, sql):
    with sqlite3.connect(db_file) as connection:
        try:
            cursor = connection.cursor()
            cursor.execute(sql)
        except sqlite3.Error as error:
            print(error)


def insert_product(db_file, product):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = '''INSERT INTO products (product_title, price, quantity) 
                        VALUES (?, ?, ?)
            '''
            cursor = connection.cursor()
            cursor.execute(sql, product)
            connection.commit()
        except sqlite3.Error as error:
            print(error)


def update_quantity(db_file, product):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
            cursor = connection.cursor()
            cursor.execute(sql, product)
            connection.commit()
        except sqlite3.Error as error:
            print(error)


def update_price(db_file, product):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = '''UPDATE products SET price = ? WHERE id = ?'''
            cursor = connection.cursor()
            cursor.execute(sql, product)
            connection.commit()
        except sqlite3.Error as error:
            print(error)


def delete_product(db_file, id):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = '''DELETE FROM products WHERE id = ?'''
            cursor = connection.cursor()
            cursor.execute(sql, (id,))
            connection.commit()
        except sqlite3.Error as error:
            print(error)


def select_all_products(db_file):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = '''SELECT * FROM products'''
            cursor = connection.cursor()
            cursor.execute(sql)
            rows_list = cursor.fetchall()
            for row in rows_list:
                print(row)
        except sqlite3.Error as error:
            print(error)


def select_products_by_price_and_quantity(db_file, price_limit, quantity_limit):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = '''SELECT * FROM products WHERE price <= ? and quantity >= ?'''
            cursor = connection.cursor()
            cursor.execute(sql, (price_limit, quantity_limit,))
            rows_list = cursor.fetchall()
            for row in rows_list:
                print(row)
        except sqlite3.Error as error:
            print(error)


def select_bread(db_file):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = '''SELECT * FROM products WHERE product_title like "_%Хлеб"'''
            cursor = connection.cursor()
            cursor.execute(sql)
            rows_list = cursor.fetchall()
            for row in rows_list:
                print(row)
        except sqlite3.Error as error:
            print(error)


def select_milk(db_file):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = '''SELECT * FROM products WHERE product_title like "_%Молоко"'''
            cursor = connection.cursor()
            cursor.execute(sql)
            rows_list = cursor.fetchall()
            for row in rows_list:
                print(row)
        except sqlite3.Error as error:
            print(error)


def select_tea(db_file):
    with sqlite3.connect(db_file) as connection:
        try:
            sql = '''SELECT * FROM products WHERE product_title like "_%Чая" or "_&Чая%_"'''
            cursor = connection.cursor()
            cursor.execute(sql)
            rows_list = cursor.fetchall()
            for row in rows_list:
                print(row)
        except sqlite3.Error as error:
            print(error)


db_name = 'hw.db'
sql_to_create_products_table = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price FLOAT(10, 2) NOT NULL DEFAULT 0,
    quantity NOT NULL DEFAULT 0)
'''


# my_connection = sqlite3.connect(db_name)
# if my_connection is not None:
#     print('Connected to database')
#     create_table(db_name, sql_to_create_products_table)
#     my_connection.close()

# insert_product(db_name, ('Белый Хлеб', 40, 50))
# insert_product(db_name, ('Ржаной Хлеб', 35, 60))
# insert_product(db_name, ('Резанный Хлеб', 55, 30))
# insert_product(db_name, ('Зерновой Хлеб', 50, 45))
# insert_product(db_name, ('Пшеничный Хлеб', 45, 50))
# insert_product(db_name, ('Коровье Молоко', 80, 30))
# insert_product(db_name, ('Соевое Молоко', 85, 25))
# insert_product(db_name, ('Миндальное Молоко', 90, 25))
# insert_product(db_name, ('Кокосовое Молоко', 95, 20))
# insert_product(db_name, ('Овсяное Молоко', 75, 30))
# insert_product(db_name, ('Рисовое Молоко', 70, 35))
# insert_product(db_name, ('Пачка Черного Чая', 180, 20))
# insert_product(db_name, ('Пачка Зеленого Чая', 170, 20))
# insert_product(db_name, ('Пачка Чая Улун', 240, 15))
# insert_product(db_name, ('Пачка Чая Пуэр', 255, 15))

# update_quantity(db_name, (40, 4))
# update_price(db_name, (250, 14))
# delete_product(db_name, 15)
# select_all_products(db_name)
# select_products_by_price_and_quantity(db_name, 100, 50)
# select_bread(db_name)
# select_milk(db_name)
# select_tea(db_name)