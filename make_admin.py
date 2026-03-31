import sqlite3
import sys
import os

def make_admin(username):
    db_path = 'instance/site.db'
    if not os.path.exists(db_path):
        print("Database not found! Please run the app and register a user first.")
        return

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Check if user exists
        cursor.execute('SELECT id, name FROM user WHERE username = ?', (username,))
        user = cursor.fetchone()
        
        if user:
            # Update user to be admin
            cursor.execute('UPDATE user SET is_admin = 1 WHERE username = ?', (username,))
            conn.commit()
            print(f"Success! '{username}' (ID: {user[0]}) is now an admin.")
            print("You can now log in and click the 'Upload' button in the navigation bar, or visit /admin directly.")
        else:
            print(f"Error: User '{username}' not found. Please register this account in the app first.")
            
        conn.close()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python make_admin.py <username>")
        print("Example: python make_admin.py myadminuser")
    else:
        make_admin(sys.argv[1])
