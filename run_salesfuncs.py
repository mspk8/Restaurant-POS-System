from functions.sales_functions import*
from database.db_connect import connect_db


def _resolve_coupon_table(cursor):
    # Keep backward compatibility with the legacy typo table name.
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name IN ('coupon_codes_DB', 'coupoun_codes_DB')")
    tables = {row["name"] for row in cursor.fetchall()}
    if "coupon_codes_DB" in tables:
        return "coupon_codes_DB"
    if "coupoun_codes_DB" in tables:
        return "coupoun_codes_DB"
    return None


def load_coupons():
    coupon_codes = {}
    conn = connect_db()
    cursor = conn.cursor()

    table_name = _resolve_coupon_table(cursor)
    if not table_name:
        conn.close()
        return coupon_codes

    rows = cursor.execute(f"SELECT code, discount FROM {table_name}").fetchall()
    for row in rows:
        coupon_codes[row["code"].upper()] = row["discount"]

    conn.close()
    return coupon_codes


def load_coupouns():
    # Backward-compatible alias for older imports.
    return load_coupons()

def load_menu_categories():
    menu_categories = {}
    conn = connect_db()
    cursor = conn.cursor()
    categories = cursor.execute("SELECT cat_code, cat_name FROM MENU_CATEGORIES_DB ORDER BY cat_code").fetchall()
    for category in categories:
        cat_name = category["cat_name"]
        if cat_name.strip().lower() == "deserts":
            cat_name = "Desserts"
        menu_categories[category["cat_code"]] = cat_name

    conn.close()
    return menu_categories

