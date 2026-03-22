import sqlite3

connection=sqlite3.connect("KababHouseutills.db")
cursor=connection.cursor()

menu_categories_db_MAKE="""CREATE TABLE IF NOT EXISTS
MENU_CATEGORIES_DB(cat_code INTEGER ,
cat_name TEXT PRIMARY KEY)"""


coupon_codes_db_MAKE="""CREATE TABLE IF NOT EXISTS
coupon_codes_DB(code TEXT PRIMARY KEY,
discount INTEGER)"""

menu_db_MAKE="""
CREATE TABLE IF NOT EXISTS
menu_DB(cat_code INTEGER , code TEXT primary key, name TEXT, price REAL,
FOREIGN KEY(cat_code) REFERENCES MENU_CATEGORIES_DB(cat_code))"""

# cursor.execute(menu_categories_db_MAKE)
# cursor.execute(coupon_codes_db_MAKE)
cursor.execute(menu_db_MAKE)
connection.commit()


connection.close()