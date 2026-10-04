# Student Performance Predictor

A full-stack machine-learning web application that estimates academic performance from study, attendance, assignment, internal-mark, and lifestyle features.

## What it does
- Estimated performance score
- Performance category
- Risk level
- Practical areas to focus on

The prediction uses a Random Forest regression model trained on the included synthetic dataset.

> Important: This is an educational/demo model. It is not an official academic assessment system, and the included dataset is synthetic.

## Web application

The project includes a browser-based web app backed by FastAPI. A user does not need to install Python or run Streamlit when the application is deployed.

### Run locally

    python -m venv .venv
    # Windows: .venv\\Scripts\\activate
    # macOS/Linux: source .venv/bin/activate
    pip install -r requirements.txt
    uvicorn api:app --reload

Open http://127.0.0.1:8000

### Docker

    docker build -t student-performance-predictor .
    docker run -p 8000:8000 student-performance-predictor

Then open http://127.0.0.1:8000

## Developer/ML dashboard

The original Streamlit application is still available:

    streamlit run app.py

## Tech Stack
- Frontend: HTML, CSS, JavaScript
- Backend: FastAPI
- ML: Python, Pandas, Scikit-learn, Random Forest
- Developer dashboard: Streamlit
- Deployment: Docker-ready

## Project Structure

    student-performance-predictor/
    ├── api.py
    ├── app.py
    ├── Dockerfile
    ├── train.py
    ├── requirements.txt
    ├── data/
    │   └── student_performance.csv
    ├── src/
    │   └── prediction.py
    ├── web/
    │   ├── index.html
    │   ├── styles.css
    │   └── app.js
    └── tests/
        └── test_prediction.py

## Model inputs
- Study hours per day
- Attendance
- Previous marks
- Assignments completed
- Internal marks
- Sleep hours

## Local development

The model is trained automatically if the saved model file does not exist. To train it explicitly:

    python train.py

Run the test suite with:

    pytest -q
