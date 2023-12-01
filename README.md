# F1 Race Predictor

A machine learning model that predicts Formula 1 race finishing positions from pre-race features — qualifying times, driver/constructor championship standings, circuit characteristics, weather, and strategy data.

Built with scikit-learn's Gradient Boosting Classifier, trained on historical race data (or a synthetic dataset for demo purposes).

## Features

- Gradient Boosting Classifier (200 estimators, depth 4)
- Feature set: grid position, qualifying time, driver points, constructor points, circuit ID, weather code, safety car laps, pit stop count
- Synthetic demo data generated automatically when no CSV is provided
- Train/predict CLI with `--train` and `--predict` flags
- Model persistence via joblib — train once, predict forever
- Full classification report with per-position precision/recall

## Tech Stack

| Layer | Technology |
|-------|-----------|
| ML | scikit-learn (GradientBoostingClassifier) |
| Data | Pandas, NumPy |
| Persistence | joblib |
| Runtime | Python 3.11+ |

## Setup

```bash
git clone https://github.com/ramsidhartha/f1-race-predictor
cd f1-race-predictor
pip install -r requirements.txt

# Train (uses synthetic data if no data/races.csv present)
python predictor.py --train

# Predict
python predictor.py --predict
```

## Architecture

```mermaid
flowchart LR
    A[CSV / Synthetic Data] --> B[Feature Engineering]
    B --> C[Train/Test Split]
    C --> D[GradientBoostingClassifier]
    D --> E[joblib Model File]
    E --> F[Predict Finish Position]
```

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `DATA_PATH` | `./data/races.csv` | Path to training data CSV |
| `MODEL_PATH` | `./models/f1_predictor.joblib` | Where to save/load the model |

## Screenshots

> 📸 Screenshots coming soon

## Author

Ram Sidhartha
