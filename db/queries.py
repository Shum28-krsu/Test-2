shopping_table = """
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item TEXT NOT NULL,
    count INTEGER DEFAULT 1,
    bought INTEGER DEFAULT 0
)
"""

insert_item = "INSERT INTO items (item, count) VALUES (?, ?)"

select_all = "SELECT * FROM items"
select_bought = "SELECT * FROM items WHERE bought = 1"
select_not_bought = "SELECT * FROM items WHERE bought = 0"

update_bought = "UPDATE items SET bought = ? WHERE id = ?"
update_item = "UPDATE items SET item = ?, count = ? WHERE id = ?"

delete_item = "DELETE FROM items WHERE id = ?"