from src.prediction import classify_score


def test_score_classification():
    assert classify_score(80) == ("Strong", "Low")
    assert classify_score(65) == ("Average", "Medium")
    assert classify_score(50) == ("At Risk", "High")
