from pathlib import Path

import joblib
import pandas as pd

FEATURES = [
    "study_hours",
    "attendance",
    "previous_marks",
    "assignments_completed",
    "internal_marks",
    "sleep_hours",
]

MODEL_PATH = Path(__file__).resolve().parents[1] / "models" / "random_forest.joblib"


def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            "Model not found. Run 'python train.py' before starting the app."
        )
    return joblib.load(MODEL_PATH)


def predict_score(values: dict) -> float:
    model = load_model()
    row = pd.DataFrame([[values[f] for f in FEATURES]], columns=FEATURES)
    return float(model.predict(row)[0])


def classify_score(score: float) -> tuple[str, str]:
    if score >= 75:
        return "Strong", "Low"
    if score >= 60:
        return "Average", "Medium"
    return "At Risk", "High"
