from functions.sales_functions import*
from database.db_connect import connect_db
import pandas as pd


def load_coupouns():
    coupoun_codes={}
    conn=connect_db()
    cursor=conn.cursor()
    coupouns=cursor.execute("SELECT* FROM coupoun_codes_DB")
    c=coupouns.fetchall()
    for x in c:
        coupoun_codes.update({x["code"]:x["discount"]})
    return coupoun_codes

def load_menu_categories():
    menu_categories={}
    conn=connect_db()
    cursor=conn.cursor()
    categories=cursor.execute("SELECT* FROM MENU_CATEGORIES_DB")
    c=categories.fetchall()
    for x in c:
        menu_categories.update({x["cat_code"]:x["cat_name"]})
    return menu_categories

