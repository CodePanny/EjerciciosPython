import sqlite3

conn = sqlite3.connect('alumnos.db')
cursor = conn.cursor()

rows = cursor.execute('SELECT * FROM alumnos2 WHERE nombre="Lando"')
for row in rows:
    print(row)

cursor.close()
conn.close()
