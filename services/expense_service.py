from db.connection import get_connection
from models.expense_model import TABLE_NAME

def add_expense(user_id, amount, category, description, date):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        f"INSERT INTO {TABLE_NAME} (user_id, amount, category, description, date) VALUES (%s, %s, %s, %s, %s)",
        (user_id, amount, category, description, date)
    )
    conn.commit()
    expense_id = cur.lastrowid
    cur.close()
    conn.close()
    return expense_id

def update_expense(expense_id, user_id, amount, category, description, date):
    conn = get_connection()
    with conn.cursor() as cursor:
        # Check if the expense belongs to this user
        cursor.execute("SELECT * FROM expenses WHERE id=%s AND user_id=%s", (expense_id, user_id))
        expense = cursor.fetchone()
        if not expense:
            conn.close()
            return False

        cursor.execute("""
            UPDATE expenses
            SET amount=%s, category=%s, description=%s, date=%s
            WHERE id=%s
        """, (amount, category, description, date, expense_id))
        conn.commit()
    conn.close()
    return True

def get_expenses_by_user(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {TABLE_NAME} WHERE user_id=%s", (user_id,))
    expenses = cur.fetchall()
    cur.close()
    conn.close()
    return expenses

def delete_expense(expense_id, user_id):
    conn = get_connection()
    with conn.cursor() as cursor:
        # Make sure the expense belongs to the user
        cursor.execute("SELECT * FROM expenses WHERE id=%s AND user_id=%s", (expense_id, user_id))
        expense = cursor.fetchone()
        if not expense:
            conn.close()
            return False

        cursor.execute("DELETE FROM expenses WHERE id=%s", (expense_id,))
        conn.commit()
    conn.close()
    return True

