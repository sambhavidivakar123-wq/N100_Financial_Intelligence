import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("database/nifty100.db")

# Read schema.sql
with open("db/schema.sql", "r") as f:
    schema = f.read()

# Execute SQL
conn.executescript(schema)

conn.commit()
conn.close()

print("Database created successfully!")