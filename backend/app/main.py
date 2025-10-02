from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.interfaces.schemas import InsightRequest, InsightResponse
from app.services.insight_service import InsightService


app = FastAPI(title="Astrological Insight Generator")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],  # Frontend URLs
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

insight_service = InsightService()


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/predict", response_model=InsightResponse)
async def predict(body: InsightRequest):
    return insight_service.generate_insight(body)


