from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

app = FastAPI(
    title="Daniel Backend API",
    description="Backend service for Daniel / MindBloom integration",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "status": "Daniel backend running",
        "service": "daniel-backend",
        "version": "1.0.0"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat()
    }

@app.get("/api/test")
def api_test():
    return {
        "success": True,
        "message": "API connection works",
        "source": "Railway FastAPI backend"
    }

@app.get("/api/mindbloom")
def mindbloom_status():
    return {
        "platform": "MindBloom",
        "status": "connected",
        "message": "MindBloom backend bridge is ready"
    }

@app.post("/api/contact")
def contact_form(data: dict):
    return {
        "success": True,
        "message": "Contact form received",
        "received_data": data
    }