import sqlite3
import os

db_path = 'instance/site.db'
if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    try:
        conn.execute("ALTER TABLE user ADD COLUMN subscription_tier VARCHAR(50) DEFAULT 'Free'")
        print("Added subscription_tier")
    except Exception as e: print(e)
    try:
        conn.execute("ALTER TABLE user ADD COLUMN profile_pic VARCHAR(500)")
        print("Added profile_pic")
    except Exception as e: print(e)
    try:
        conn.execute("ALTER TABLE user ADD COLUMN theme_color VARCHAR(50) DEFAULT '#E50914'")
        print("Added theme_color")
    except Exception as e: print(e)
    conn.commit()
    conn.close()
