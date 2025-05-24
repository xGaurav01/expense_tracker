import pymysql
from db.connection import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME
from models.user_model import CREATE_TABLE_QUERY as CREATE_USERS_TABLE
from models.expense_model import CREATE_TABLE_QUERY as CREATE_EXPENSES_TABLE

def init_db():
    conn = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    cursor.execute(f"USE {DB_NAME}")

    # Create tables from model schema
    cursor.execute(CREATE_USERS_TABLE)
    cursor.execute(CREATE_EXPENSES_TABLE)

    conn.commit()
    cursor.close()
    conn.close()
