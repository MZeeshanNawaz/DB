import sqlite3
print(sqlite3.sqlite_version)

conn = sqlite3.connect("zeeshan.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER)
""")
conn.commit()
cursor.execute('INSERT INTO users(name,age) VALUES(?,?)',("Zeeshan",20))
cursor.execute('INSERT INTO users(name,age) VALUES(?,?)',("Nawaz",25))

cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
print("After data insertion")
for data in rows:
    print(data)

cursor.execute('UPDATE users SET age=? WHERE name=?',(21,"Zeeshan"))
conn.commit()
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
print("After data Updation:")
for data in rows:
    print(data)

cursor.execute('DELETE FROM users WHERE name=?',("Nawaz",))
conn.commit()
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
print("After data Delete:")
for data in rows:
    print(data)

conn.close()
