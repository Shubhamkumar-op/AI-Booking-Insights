from pydantic import BaseModel
from typing import Dict, Any

class QueryRequest(BaseModel):
    query: str

class BookingAnalyticsResponse(BaseModel):
    revenue_trends: dict
    cancellation_rate: float
    geo_distribution: dict
    booking_lead_time: dict
    most_popular_hotel: str
    average_adr_per_hotel: dict
    
class QAResponse(BaseModel):
    faiss_response: Dict[str, Any]
    llm_response: str
