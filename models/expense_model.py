# models/expenses.py

from .user_model import USERS_TABLE_NAME

TABLE_NAME = "expenses"

CREATE_TABLE_QUERY = f"""
CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    amount DECIMAL(10, 2),
    category VARCHAR(100),
    description TEXT,
    date DATE,
    FOREIGN KEY (user_id) REFERENCES {USERS_TABLE_NAME}(id) ON DELETE CASCADE
);
"""
