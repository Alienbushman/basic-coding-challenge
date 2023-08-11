import os
import sqlite3

if os.path.exists('sessions.db'):
    os.remove('sessions.db')
conn = sqlite3.connect('sessions.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE sessions (
        id INTEGER PRIMARY KEY,
        userId INTEGER NOT NULL,
        duration DECIMAL NOT NULL
    )
''')

cursor.execute('INSERT INTO sessions (userId, duration) VALUES (1, 30.5)')
cursor.execute('INSERT INTO sessions (userId, duration) VALUES (2, 20.3)')
cursor.execute('INSERT INTO sessions (userId, duration) VALUES (1, 45.2)')
cursor.execute('INSERT INTO sessions (userId, duration) VALUES (3, 15.7)')
cursor.execute('INSERT INTO sessions (userId, duration) VALUES (2, 50.0)')
cursor.execute('INSERT INTO sessions (userId, duration) VALUES (4, 10.2)')
cursor.execute('INSERT INTO sessions (userId, duration) VALUES (1, 25.8)')

conn.commit()

cursor.execute('SELECT userid, avg(duration) FROM sessions GROUP BY userid HAVING COUNT(userid) > 1;')
results = cursor.fetchall()
print(results)
conn.close()
