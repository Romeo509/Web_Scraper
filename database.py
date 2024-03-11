import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('news_data.db')

# Create a table for news data
conn.execute('''
CREATE TABLE IF NOT EXISTS news (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    headline TEXT
);
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
