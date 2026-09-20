import sqlite3
from datetime import datetime

conn = sqlite3.connect('histtory.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS requests(id INTEGER PRIMARY KEY AUTOINCREMENT,
date TEXT,
count INTEGER)""")
conn.commit()

def save(count):
    cursor.execute("""INSERT INTO requests(date, count) VALUES(?,?)""", (datetime.now().strftime("%d.%m.%Y %H:%M:%S:"), count))
    conn.commit()