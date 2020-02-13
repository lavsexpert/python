import sqlite3

def reg(phone, email, password):
    conn = sqlite3.connect('site.db')
    cursor = conn.cursor()
    if is_reg(phone, password) or is_reg(email, password):
        conn.close()
        return False
    cursor.execute("""
    INSERT INTO users VALUES(?,?,?)
    """, (phone, email, password))
    conn.commit()
    conn.close()
    return True

def is_reg(login, password):
    conn = sqlite3.connect('site.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM users
    WHERE (users.phone = ? OR users.email = ?) AND users.password = ?
    """, (login, login, password))
    if len(cursor.fetchall()) == 0:
        conn.close()
        return False
    else:
        conn.close()
        return True

def print_db():
    conn = sqlite3.connect('site.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM users
    """)
    print(cursor.fetchall())

