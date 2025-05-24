# 💼 Expense Tracker Backend

This is the backend of an **Expense Tracker** application built with **Python**, **Flask**, and **MySQL**.

## 🚀 Features

- 🔐 **User Authentication**
  - User registration and login
  - Secure session management
- 📊 **Expense Management**
  - Add and view expenses
  - Filter expenses by user
- 🧹 **Data Processing**
  - Fetches expense data from MySQL
  - Cleans and formats the data
  - Saves cleaned data as a CSV file (`process_data/cleaned_expenses.csv`)
- ☁️ **WordCloud Generation**
  - Generates a WordCloud from the `description` column of expenses
  - Saved as an image file (`process_data/wordcloud_expenses.png`)

## 📁 Project Structure


## 🔧 Tech Stack

- Python
- Flask
- MySQL (via `pymysql`)
- Pandas
- Matplotlib
- WordCloud

## 🛠️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/expense_tracker.git
   cd expense_tracker
   
2. **Create a virtual environment**
   ```bash
    python -m venv expense
    source expense/bin/activate
   
4. **Install dependencies**
    ```bash
    pip install -r requirements.txt

5. **Set up .env file**
   
     - DB_HOST=localhost
     - DB_USER=your_db_user
     - DB_PASSWORD=your_db_password
     - DB_NAME=expense_db
     - SECRET_KEY=your-secret-key



