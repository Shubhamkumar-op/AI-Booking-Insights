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

import sqlite3
import logging
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Database connection
db_path = "hotel_bookings.db"

def get_sql_data(query):
    try:
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result
    except sqlite3.Error as e:
        logging.error(f"Failed to execute query: {query}. Error: {e}")
        return []

def revenue_trends():
    query = """
        SELECT strftime('%Y-%m', arrival_date), SUM(adr * stays_in_week_nights)
        FROM bookings
        GROUP BY 1
    """
    result = get_sql_data(query)
    return {row[0]: row[1] for row in result} if result else {}

def cancellation_rate():
    query = "SELECT AVG(is_canceled) * 100 FROM bookings"
    result = get_sql_data(query)
    return float(result[0][0]) if result and result[0][0] is not None else 0.0

def geo_distribution():
    query = "SELECT country, COUNT(*) FROM bookings GROUP BY country"
    result = get_sql_data(query)
    return {row[0]: row[1] for row in result} if result else {}

def booking_lead_time():
    query = "SELECT AVG(lead_time), MIN(lead_time), MAX(lead_time) FROM bookings"
    result = get_sql_data(query)
    if result and result[0] is not None:
        avg_lead, min_lead, max_lead = result[0]
        return {"average_lead_time": avg_lead, "minimum_lead_time": min_lead, "maximum_lead_time": max_lead}
    return {"average_lead_time": 0, "minimum_lead_time": 0, "maximum_lead_time": 0}

# Additional analytics
def most_popular_hotel():
    query = "SELECT hotel, COUNT(*) FROM bookings GROUP BY hotel ORDER BY COUNT(*) DESC LIMIT 1"
    result = get_sql_data(query)
    return result[0][0] if result else "No Data"

def average_adr_per_hotel():
    query = "SELECT hotel, AVG(adr) FROM bookings GROUP BY hotel"
    result = get_sql_data(query)
    return {row[0]: row[1] for row in result} if result else {}
