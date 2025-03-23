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
import sqlite3
import pandas as pd
import os

db_path = "hotel_bookings.db"
conn = sqlite3.connect(db_path)
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

csv_file = "../data/hotel_bookings.csv"  
df = pd.read_csv(csv_file)

print("CSV Columns:", df.columns.tolist())

if "arrival_date" not in df.columns:
    if {"arrival_date_year", "arrival_date_month", "arrival_date_day_of_month"}.issubset(df.columns):
        df["arrival_date"] = (
            df["arrival_date_year"].astype(str) + "-" + 
            df["arrival_date_month"] + "-" + 
            df["arrival_date_day_of_month"].astype(str)
        )
    else:
        print("Error: Required column 'arrival_date' is missing.")
        exit()

expected_columns = ["hotel", "arrival_date", "adr", "stays_in_week_nights", "is_canceled", "lead_time", "country"]
available_columns = [col for col in expected_columns if col in df.columns]

print("Available Columns:", available_columns)

if len(available_columns) < len(expected_columns):
    print("Warning: Some expected columns are missing. Proceeding with available data.")

df = df[available_columns]

def insert_data(df):
    for _, row in df.iterrows():
        cursor.execute(f'''
            INSERT INTO bookings ({", ".join(available_columns)})
            VALUES ({", ".join(["?"] * len(available_columns))})
        ''', tuple(row[col] for col in available_columns))
    conn.commit()

insert_data(df)

conn.close()
print("Data successfully loaded into the database from 'data/hotel_bookings.csv'.")


