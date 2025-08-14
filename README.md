# NBA Game Predictor

A machine learning-based application that predicts NBA game outcomes using historical game statistics, served via a FastAPI backend and an interactive dashboard.

## Features
- **FastAPI Backend** – Serves prediction endpoints for NBA games.
- **Machine Learning Model** – Trained using historical NBA data to estimate game results.
- **Interactive Dashboard** – Visual interface for inputting data and viewing predictions.
- **Model Persistence** – Uses `joblib` for saving and loading models efficiently.

## Tech Stack
- **Python** – Core programming language  
- **FastAPI** – Backend API framework  
- **Pandas / NumPy** – Data manipulation and analysis  
- **Scikit-learn / XGBoost** – Machine learning  
- **Dash / Plotly** – Interactive visualization dashboard  
- **Joblib** – Model serialization  

## Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/NBA-Game-Predictor.git
cd NBA-Game-Predictor

# Install dependencies
pip install -r requirements.txt
```

## Running the Application
1. **Start the API Backend**  
```bash
uvicorn main:app --reload
```

2. **Launch the Dashboard**  
In another terminal:
```bash
python nba_game_predictor_dashboard.py
```

3. Open your browser to the dashboard’s local address (default: `http://127.0.0.1:8050`).

## Project Structure
```
NBA-Game-Predictor/
│-- data/                # Dataset files
│-- models/              # Saved model files
│-- main.py               # FastAPI backend
│-- nba_game_predictor_dashboard.py # Dashboard application
│-- requirements.txt
│-- README.md
```