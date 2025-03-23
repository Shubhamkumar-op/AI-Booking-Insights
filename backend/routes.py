from fastapi import APIRouter
from analytics import revenue_trends, cancellation_rate, geo_distribution, booking_lead_time
from faiss_index import query_faiss
from llm import query_llm
from models import QueryRequest, BookingAnalyticsResponse, QAResponse

router = APIRouter()

@router.post("/analytics", response_model=BookingAnalyticsResponse)
def get_analytics():
    try:
        return BookingAnalyticsResponse(
            revenue_trends=revenue_trends(),
            cancellation_rate=cancellation_rate(),
            geo_distribution=geo_distribution(),
            booking_lead_time=booking_lead_time()
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

@router.post("/ask", response_model=QAResponse)
def ask_question(request: QueryRequest):
    return {
        "faiss_response": query_faiss(request.query),
        "llm_response": query_llm(request.query)
    }
