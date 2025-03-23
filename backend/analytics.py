# import sqlite3
# import os


# DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "hotel_bookings.csv")

# def get_sql_data(query):
#     try:
#         with sqlite3.connect(DB_PATH) as conn:
#             cursor = conn.cursor()
#             cursor.execute(query)
#             result = cursor.fetchall()
#             logging.info(f"Successfully executed query: {query}")
#             return result
#     except sqlite3.Error as e:
#         logging.error(f"Failed to execute query: {query}. Error: {e}")
#         return []

# def revenue_trends():
#     query = "SELECT strftime('%Y-%m', arrival_date), SUM(adr * stays_in_week_nights) FROM bookings GROUP BY 1"
#     result = get_sql_data(query)
#     logging.info(f"Retrieved revenue trends data")
#     return {row[0]: row[1] for row in result} if result else {}

# def cancellation_rate():
#     query = "SELECT AVG(is_canceled) * 100 FROM bookings"
#     result = get_sql_data(query)
#     logging.info(f"Retrieved cancellation rate data")
#     return float(result[0][0]) if result and result[0][0] is not None else 0.0

# def geo_distribution():
#     query = "SELECT country, COUNT(*) FROM bookings GROUP BY country"
#     result = get_sql_data(query)
#     logging.info(f"Retrieved geo distribution data")
#     return {row[0]: row[1] for row in result} if result else {}

# def booking_lead_time():
#     query = "SELECT AVG(lead_time), MIN(lead_time), MAX(lead_time) FROM bookings"
#     result = get_sql_data(query)
#     logging.info(f"Retrieved booking lead time data")
#     avg_lead, min_lead, max_lead = result[0] if result and result[0] is not None else (0, 0, 0)
#     return {"average_lead_time": avg_lead, "minimum_lead_time": min_lead, "maximum_lead_time": max_lead}

import pandas as pd
import os

<<<<<<< HEAD
CSV_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "hotel_bookings.csv")
df = pd.read_csv(CSV_PATH)
=======
filepath=data_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "bookings_data.csv")
>>>>>>> af59f911be2d9340bb2b5cf59ac6ab8750d45912

def revenue_trends():
    df["arrival_date"] = pd.to_datetime(df["arrival_date_year"].astype(str) + "-" + df["arrival_date_month"])
    trends = df.groupby(df["arrival_date"].dt.to_period("M")).apply(lambda x: (x["adr"] * x["stays_in_week_nights"]).sum()).to_dict()
    return trends

def cancellation_rate():
    return df["is_canceled"].mean() * 100

def geo_distribution():
    return df["country"].value_counts().to_dict() 

def booking_lead_time():
    return {
        "average_lead_time": df["lead_time"].mean(),
        "minimum_lead_time": df["lead_time"].min(),
        "maximum_lead_time": df["lead_time"].max(),
    }
