from fastapi import APIRouter
from backend.analytics import revenue_trends, cancellation_rate, geo_distribution, booking_lead_time
from backend.faiss_index import query_faiss
from backend.llm import query_llm
from backend.models import QueryRequest, BookingAnalyticsResponse, QAResponse

router = APIRouter()

@router.post("/analytics", response_model=BookingAnalyticsResponse)
def get_analytics():
    return {
        "revenue_trends": revenue_trends(),
        "cancellation_rate": cancellation_rate(),
        "geo_distribution": geo_distribution(),
        "booking_lead_time": booking_lead_time()
    }

@router.post("/ask", response_model=QAResponse)
def ask_question(request: QueryRequest):
    return {
        "faiss_response": query_faiss(request.query),
        "llm_response": query_llm(request.query)
    }
