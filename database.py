import os
import sqlite3
from flask import g


def connect_db():
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "food_log.db")
    sql = sqlite3.connect(db_path)
    sql.row_factory = sqlite3.Row
    return sql


def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db
