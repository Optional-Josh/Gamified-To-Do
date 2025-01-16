import json
import sqlite3

# Define file paths
json_file = "Joshua.json"  # Replace with your JSON file path
sqlite_db = "Joshua.db"   # SQLite database file name

# Load JSON data
with open(json_file, 'r') as f:
    data = json.load(f)

# Connect to SQLite database (or create it)
conn = sqlite3.connect(sqlite_db)
cursor = conn.cursor()

# Create a table (adjust schema as per JSON structure)
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS tasks (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     category TEXT,
#     difficulty INTEGER,
#     description TEXT,
#     points INTEGER,
#     date TEXT,
#     status TEXT
# )
# ''')

# Insert JSON data into the SQLite table
# for item in data:
#     cursor.execute('''
#     INSERT INTO tasks (category, difficulty, description, points, date, status)
#     VALUES (?, ?, ?, ?, ?, ?)
#     ''', (item['category'], item['difficulty'], item['description'], item['points'], item['date'], item['status']))

# Commit changes and close connection
# conn.commit()
# conn.close()

def view_db():
     # Execute query to fetch all rows from the tasks table
    cursor.execute('SELECT * FROM tasks;')

    # Fetch all rows
    rows = cursor.fetchall()

    # Check if there are any rows and display them
    for row in rows:
        print(f"ID: {row[0]}, Category: {row[1]}, Difficulty: {row[2]}, Description: {row[3]}, Points: {row[4]}, Date: {row[5]}, Status: {row[6]}")



# print("JSON data has been successfully converted to SQLite!")

if __name__ == '__main__':
    view_db()