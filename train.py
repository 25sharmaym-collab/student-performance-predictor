from pathlib import Path

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

FEATURES = [
    "study_hours",
    "attendance",
    "previous_marks",
    "assignments_completed",
    "internal_marks",
    "sleep_hours",
]

ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "student_performance.csv"
MODEL_DIR = ROOT / "models"


def main():
    df = pd.read_csv(DATA_PATH)
    X = df[FEATURES]
    y = df["final_score"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest": RandomForestRegressor(
            n_estimators=200, random_state=42
        ),
    }

    MODEL_DIR.mkdir(exist_ok=True)

    for name, model in models.items():
        model.fit(X_train, y_train)
        predictions = model.predict(X_test)
        print(
            f"{name}: MAE={mean_absolute_error(y_test, predictions):.2f}, "
            f"R2={r2_score(y_test, predictions):.3f}"
        )

    final_model = models["Random Forest"]
    joblib.dump(final_model, MODEL_DIR / "random_forest.joblib")
    print(f"Saved model to {MODEL_DIR / 'random_forest.joblib'}")


if __name__ == "__main__":
    main()
