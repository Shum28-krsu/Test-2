import sqlite3
from config import path_db
from db import queries


def init_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.shopping_table)
    conn.commit()
    conn.close()


def add_item(name, count):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.insert_item, (name, count))
    conn.commit()
    item_id = cursor.lastrowid
    conn.close()
    return item_id


def get_items(filter_type):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()

    if filter_type == "all":
        cursor.execute(queries.select_all)
    elif filter_type == "done":
        cursor.execute(queries.select_bought)
    else:
        cursor.execute(queries.select_not_bought)

    items = cursor.fetchall()
    conn.close()
    return items


def toggle_item(item_id, done):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.update_bought, (done, item_id))
    conn.commit()
    conn.close()


def delete_item(item_id):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.delete_item, (item_id,))
    conn.commit()
    conn.close()


def update_item(item_id, name, count):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.update_item, (name, count, item_id))
    conn.commit()
    conn.close()