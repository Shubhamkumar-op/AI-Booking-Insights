import pandas as pd
import numpy as np

filrpath=data_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "bookings_data.csv")

def load_data(filepath):
    try:
        df = pd.read_csv(filepath)
        df.dropna(inplace=True)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame() 


def revenue_trends(df):
    try:
        df['arrival_date'] = pd.to_datetime(df['arrival_date'], errors='coerce')
        df['month_year'] = df['arrival_date'].dt.to_period('M')
        df['revenue'] = df['adr'] * df['stays_in_week_nights']
        revenue_data = df.groupby('month_year')['revenue'].sum().reset_index()

        return revenue_data.set_index('month_year')['revenue'].to_dict() 
        print(f"Error calculating revenue trends: {e}")
        return {}

def cancellation_rate(df):
    try:
        cancellation_rate = (df['is_canceled'].mean()) * 100 
        return cancellation_rate
    except Exception as e:
        print(f"Error calculating cancellation rate: {e}")
        return 0.0

def geo_distribution(df):
    try:
        geo_data = df.groupby('country').size().reset_index(name='bookings_count')
        return geo_data.set_index('country')['bookings_count'].to_dict() 
    except Exception as e:
        print(f"Error calculating geo distribution: {e}")
        return {}

def booking_lead_time(df):
    try:
        avg_lead_time = df['lead_time'].mean()
        min_lead_time = df['lead_time'].min()
        max_lead_time = df['lead_time'].max()

        return {
            "average_lead_time": avg_lead_time,
            "minimum_lead_time": min_lead_time,
            "maximum_lead_time": max_lead_time
        }
    except Exception as e:
        print(f"Error calculating booking lead time: {e}")
        return {"average_lead_time": 0, "minimum_lead_time": 0, "maximum_lead_time": 0}
