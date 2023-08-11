import os
import sqlite3

if os.path.exists('enrollments.db'):
    os.remove('enrollments.db')

conn = sqlite3.connect('enrollments.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE enrollments (
        id INTEGER NOT NULL PRIMARY KEY,
        year INTEGER NOT NULL,
        studentId INTEGER NOT NULL
    )
''')

for id in range(1, 150):
    year = 2021
    if 20 <= id <= 100:
        year = 2010
    student_id = id
    cursor.execute('INSERT INTO enrollments (id, year, studentId) VALUES (?, ?, ?)', (id, year, student_id))

conn.commit()

cursor.execute('UPDATE enrollments SET year = 2015 WHERE id BETWEEN 20 AND 100')

conn.commit()

conn.close()
