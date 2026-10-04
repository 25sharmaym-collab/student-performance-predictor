from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

from src.prediction import classify_score, predict_score

ROOT = Path(__file__).resolve().parent
WEB_DIR = ROOT / "web"

app = FastAPI(title="Student Performance Predictor API", version="1.0.0")


class PredictionInput(BaseModel):
    study_hours: float = Field(ge=0, le=12)
    attendance: float = Field(ge=0, le=100)
    previous_marks: float = Field(ge=0, le=100)
    assignments_completed: int = Field(ge=0, le=10)
    internal_marks: float = Field(ge=0, le=100)
    sleep_hours: float = Field(ge=0, le=12)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/api/predict")
def predict(payload: PredictionInput):
    score = predict_score(payload.model_dump())
    category, risk = classify_score(score)

    if risk == "Low":
        advice = [
            "Maintain your current attendance and study consistency.",
            "Keep completing assignments on time.",
        ]
    elif risk == "Medium":
        advice = [
            "Increase study consistency and protect regular sleep.",
            "Focus on improving internal marks and assignment completion.",
        ]
    else:
        advice = [
            "Prioritize consistent daily study sessions.",
            "Improve attendance and complete more assignments.",
            "Review weak subjects before the next assessment.",
        ]

    return {
        "predicted_score": round(score, 1),
        "performance": category,
        "risk": risk,
        "advice": advice,
    }


@app.get("/")
def home():
    return FileResponse(WEB_DIR / "index.html")


@app.get("/styles.css")
def styles():
    return FileResponse(WEB_DIR / "styles.css", media_type="text/css")


@app.get("/app.js")
def javascript():
    return FileResponse(WEB_DIR / "app.js", media_type="application/javascript")
