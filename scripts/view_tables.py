import sqlite3

conn = sqlite3.connect("database/nifty100.db")

tables = conn.execute(
    "SELECT name FROM sqlite_master WHERE type='table';"
).fetchall()

print("Tables in the database:")
for table in tables:
    print(table[0])

conn.close()