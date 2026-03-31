import sqlite3
import os

db_path = 'instance/site.db'
if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    try:
        conn.execute('ALTER TABLE user ADD COLUMN is_admin BOOLEAN DEFAULT 0')
        print("Column added successfully.")
    except Exception as e:
        print("Column may already exist:", e)
    conn.commit()
    conn.close()
else:
    print("Database does not exist yet. It will be created on first run.")
