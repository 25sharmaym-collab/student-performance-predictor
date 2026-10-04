from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

FEATURES = [
    "study_hours",
    "attendance",
    "previous_marks",
    "assignments_completed",
    "internal_marks",
    "sleep_hours",
]

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "student_performance.csv"
MODEL_PATH = ROOT / "models" / "random_forest.joblib"


def train_model():
    df = pd.read_csv(DATA_PATH)
    model = RandomForestRegressor(n_estimators=200, random_state=42)
    model.fit(df[FEATURES], df["final_score"])
    MODEL_PATH.parent.mkdir(exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    return model


def load_model():
    if not MODEL_PATH.exists():
        return train_model()
    return joblib.load(MODEL_PATH)


def predict_score(values: dict) -> float:
    row = pd.DataFrame([[values[f] for f in FEATURES]], columns=FEATURES)
    return float(load_model().predict(row)[0])


def classify_score(score: float) -> tuple[str, str]:
    if score >= 75:
        return "Strong", "Low"
    if score >= 60:
        return "Average", "Medium"
    return "At Risk", "High"
