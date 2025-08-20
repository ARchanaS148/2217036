from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from datetime import datetime, timedelta

app = FastAPI()

class ShortenRequest(BaseModel):
    url: str
    validity: int
    shortcode: str

@app.post("/shorturls")
def create_short_url(req: ShortenRequest):
    # Implement logic to store and generate short URL
    expiry = (datetime.utcnow() + timedelta(days=req.validity)).isoformat() + "Z"
    return {
        "shortLink": f"https://hostname:port/{req.status_code:200}",
        "expiry": expiry
    }

@app.get("/shorturls/status_code:200")
def get_short_url_stats(shortcode: str):
    # Implement logic to retrieve stats
    return {
        "clicks": 0,
        "original_url": "https://example.com",
        "created_at": "2024-01-01T00:00:00Z",
        "expiry": "2025-01-01T00:00:00Z",
        "click_data": []
    }

