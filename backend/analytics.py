from database import get_sql_data

def revenue_trends():
    result = get_sql_data("SELECT strftime('%Y-%m', arrival_date), SUM(adr * stays_in_week_nights) FROM bookings GROUP BY 1")
    return {row[0]: row[1] for row in result}

def cancellation_rate():
    result = get_sql_data("SELECT AVG(is_canceled) * 100 FROM bookings")
    return float(result[0][0]) if result else 0.0 

def geo_distribution():
    return dict(get_sql_data("SELECT country, COUNT(*) FROM bookings GROUP BY country"))

def booking_lead_time():
    result = get_sql_data("SELECT AVG(lead_time), MIN(lead_time), MAX(lead_time) FROM bookings")
    avg_lead, min_lead, max_lead = result[0]
    return {
        "average_lead_time": avg_lead,
        "minimum_lead_time": min_lead,
        "maximum_lead_time": max_lead
    }

