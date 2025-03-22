import sqlite3

db_path = "hotel_bookings.db"
conn = sqlite3.connect(db_path, check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS bookings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        hotel TEXT,
        arrival_date TEXT,
        adr REAL,
        stays_in_week_nights INTEGER,
        is_canceled INTEGER,
        lead_time INTEGER,
        country TEXT
    )
''')
conn.commit()

def get_sql_data(query):
    cursor.execute(query)
    return cursor.fetchall()
