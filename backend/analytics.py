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
import pandas as pd
import os
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(BASE_DIR, "data", "hotel_bookings.csv")

def load_data():
    try:
        return pd.read_csv(CSV_PATH)
    except pd.errors.EmptyDataError:
        logging.error("The CSV file is empty.")
        return pd.DataFrame()
    except pd.errors.ParserError as e:
        logging.error(f"Failed to parse the CSV file. Error: {e}")
        return pd.DataFrame()

def revenue_trends(df):
    df["arrival_date"] = pd.to_datetime(df["arrival_date_year"].astype(str) + "-" + df["arrival_date_month"])
    trends = df.groupby(df["arrival_date"].dt.to_period("M")).apply(lambda x: (x["adr"] * x["stays_in_week_nights"]).sum()).to_dict()
    logging.info("Retrieved revenue trends data")
    return trends

def cancellation_rate(df):
    rate = df["is_canceled"].mean() * 100
    logging.info("Retrieved cancellation rate data")
    return rate

def geo_distribution(df):
    distribution = df["country"].value_counts().to_dict()
    logging.info("Retrieved geo distribution data")
    return distribution

def booking_lead_time(df):
    lead_time_data = {
        "average_lead_time": df["lead_time"].mean(),
        "minimum_lead_time": df["lead_time"].min(),
        "maximum_lead_time": df["lead_time"].max(),
    }
    logging.info("Retrieved booking lead time data")
    return lead_time_data

