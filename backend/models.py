from pydantic import BaseModel
from typing import Dict, Any

class QueryRequest(BaseModel):
    query: str

class BookingAnalyticsResponse(BaseModel):
    revenue_trends: Dict[str, float]
    cancellation_rate: float
    geo_distribution: Dict[str, int]
    booking_lead_time: Dict[str, Any]

class QAResponse(BaseModel):
    faiss_response: Dict[str, Any]
    llm_response: str
