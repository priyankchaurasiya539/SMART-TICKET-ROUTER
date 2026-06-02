import sqlite3
conn = sqlite3.connect("ticket_system.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM resolved_tickets")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
