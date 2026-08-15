from fastapi import FastAPI
from app.api.onboarding import router as onboarding_router

app = FastAPI(
    title="Hierarchical Agent Coordination Framework",
    version="1.0.0"
)

app.include_router(onboarding_router)

@app.get("/")
def root():
    return {
        "message": "API is running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }