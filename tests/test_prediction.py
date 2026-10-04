from src.prediction import classify_score, predict_score


def test_score_classification():
    assert classify_score(80) == ("Strong", "Low")
    assert classify_score(65) == ("Average", "Medium")
    assert classify_score(50) == ("At Risk", "High")


def test_prediction_pipeline():
    score = predict_score({
        "study_hours": 5,
        "attendance": 85,
        "previous_marks": 75,
        "assignments_completed": 8,
        "internal_marks": 72,
        "sleep_hours": 7,
    })
    assert 0 <= score <= 100
