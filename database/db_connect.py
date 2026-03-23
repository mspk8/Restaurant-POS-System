import sqlite3
from pathlib import Path
def connect_db():
    BASE_DIR=Path(__file__).resolve().parent
    DB_DIR=BASE_DIR/"KababHouseUtills.db"
    conn=sqlite3.connect(DB_DIR)
    conn.row_factory=sqlite3.Row
    return conn