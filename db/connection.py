import pymysql

DB_HOST = 'localhost'
DB_USER = 'pythonuser'
DB_PASSWORD = 'Python@1234'
DB_NAME = 'expense_db'

def get_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )
