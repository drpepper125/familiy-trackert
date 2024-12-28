import sqlite3

con = sqlite3.connect("new_table_1.db")
cur = con.cursor()
query = cur.execute("SELECT name FROM sqlite_master")
print(query.fetchone())