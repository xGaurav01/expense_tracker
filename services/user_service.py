from db.connection import get_connection
from models.user_model import USERS_TABLE_NAME

def create_user(name, email, password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"INSERT INTO {USERS_TABLE_NAME} (name, email, password) VALUES (%s, %s, %s)", (name, email, password))
    conn.commit()
    user_id = cur.lastrowid
    cur.close()
    conn.close()
    return user_id

def get_user_by_email(email):
    conn = get_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT id, name, email, password FROM users WHERE email=%s", (email,))
        user = cursor.fetchone()
    conn.close()
    return user

def get_user_by_id(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"SELECT id, name, email FROM {USERS_TABLE_NAME} WHERE id=%s", (user_id,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    return user

def get_all_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"SELECT id, name, email FROM {USERS_TABLE_NAME}")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return users

def delete_user(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"DELETE FROM {USERS_TABLE_NAME} WHERE id=%s", (user_id,))
    conn.commit()
    affected = cur.rowcount
    cur.close()
    conn.close()
    return affected > 0
