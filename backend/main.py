import os
import uvicorn
from fastapi import FastAPI
from backend.routes import router

app = FastAPI()
app.include_router(router)

@app.get("/")
def root():
    return {"message": "LLM Booking System API is running!"}

# Ensure FastAPI runs on the correct port
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Use PORT from Render or default to 8000
    print(f"✅ Running FastAPI on PORT: {port}")
    uvicorn.run(app, host="0.0.0.0", port=port)
