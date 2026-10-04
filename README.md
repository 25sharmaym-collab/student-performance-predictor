# Student Performance Predictor

A machine-learning application that predicts a student's academic score from study, attendance, assignment, internal-mark, and lifestyle features.

## Features
- Data cleaning and exploratory analysis
- Linear Regression and Random Forest comparison
- Score prediction
- Performance category and risk level
- Interactive Streamlit dashboard

## Tech Stack
Python, Pandas, NumPy, Scikit-learn, Matplotlib, Streamlit

## Project Structure
```
student-performance-predictor/
├── app.py
├── train.py
├── requirements.txt
├── data/
│   └── student_performance.csv
├── models/
│   └── .gitkeep
├── src/
│   └── prediction.py
└── tests/
    └── test_prediction.py
```

## Run locally
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python train.py
streamlit run app.py
```

The training script creates the model file under `models/`.

## Note
The included dataset is synthetic and is intended for demonstration and learning. Model metrics should not be interpreted as a real educational assessment system.
