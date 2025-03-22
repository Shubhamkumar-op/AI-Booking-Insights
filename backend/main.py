from fastapi import FastAPI
from backend.routes import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def root():
    return {"message": "LLM Booking System API is running!"}
