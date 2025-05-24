# models/users.py

# Users table schema

USERS_TABLE_NAME = "users"

CREATE_TABLE_QUERY = f"""
CREATE TABLE IF NOT EXISTS {USERS_TABLE_NAME} (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100)
);
"""
