from db.connection import get_connection
import os
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def fetch_expenses():
    conn = get_connection()
    cur = conn.cursor()
    query = "SELECT * FROM expenses"
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()

    # Convert to DataFrame
    df = pd.DataFrame(rows)
    return df

def clean_expenses(df):
    df = df.dropna(subset=['user_id', 'amount'])  # Drop rows with missing ID/amount
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce')  # Convert amounts
    df = df.dropna(subset=['amount'])  # Drop rows with invalid amounts
    df['category'] = df['category'].fillna('Unknown')  # Fill missing categories
    df['description'] = df['description'].fillna('No Description')  # Fill missing descriptions
    return df

def generate_wordcloud(df, save_path):
    text = ' '.join(df['description'].dropna())
    wc = WordCloud(width=800, height=400, background_color='white').generate(text)
    wc.to_file(save_path)
    print(f"✅ WordCloud saved as {save_path}")

def save_cleaned_csv(df, save_path):
    df.to_csv(save_path, index=False)
    print(f"✅ Cleaned CSV saved as {save_path}")

def main():
    print("📥 Fetching data...")
    df = fetch_expenses()
    if df.empty:
        print("⚠️ No data fetched from the database.")
        return

    print("🧹 Cleaning data...")
    cleaned_df = clean_expenses(df)

    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(current_dir, 'cleaned_expenses.csv')
    img_path = os.path.join(current_dir, 'wordcloud_expenses.png')

    print("💾 Saving cleaned CSV...")
    save_cleaned_csv(cleaned_df, csv_path)

    print("🎨 Generating WordCloud...")
    generate_wordcloud(cleaned_df, img_path)

    print("✅ All done!")

if __name__ == '__main__':
    main()
