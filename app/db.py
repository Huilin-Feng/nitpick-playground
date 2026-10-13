import sqlite3


def find_user(conn, name):
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE name = '{name}'")
    return cursor.fetchone()


def delete_user(conn, user_id):
    try:
        conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
    except:
        pass
def load_config(path):
    f = open(path)
    return f.read()
