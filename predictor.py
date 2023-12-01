"""
F1 Race Predictor
Trains a gradient-boosted model on historical F1 race data to predict race outcomes.
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
import joblib
import os

MODEL_PATH = "models/f1_predictor.joblib"
DATA_PATH = "data/races.csv"


FEATURE_COLS = [
    "grid_position",
    "qualifying_time_ms",
    "driver_points_before_race",
    "constructor_points_before_race",
    "circuit_id",
    "weather_code",   # 0=dry, 1=wet, 2=mixed
    "safety_car_laps",
    "pit_stop_count",
]
TARGET_COL = "finish_position"


def load_data(path: str = DATA_PATH) -> pd.DataFrame:
    if not os.path.exists(path):
        print(f"[INFO] No data file at {path}. Generating synthetic demo data.")
        return _generate_synthetic_data()
    return pd.read_csv(path)


def _generate_synthetic_data(n: int = 5000) -> pd.DataFrame:
    rng = np.random.default_rng(42)
    grid = rng.integers(1, 21, n)
    # Finish position correlated with grid but with noise
    noise = rng.integers(-5, 6, n)
    finish = np.clip(grid + noise, 1, 20)
    return pd.DataFrame(
        {
            "grid_position": grid,
            "qualifying_time_ms": rng.integers(75000, 95000, n),
            "driver_points_before_race": rng.integers(0, 400, n),
            "constructor_points_before_race": rng.integers(0, 700, n),
            "circuit_id": rng.integers(0, 24, n),
            "weather_code": rng.integers(0, 3, n),
            "safety_car_laps": rng.integers(0, 10, n),
            "pit_stop_count": rng.integers(1, 4, n),
            "finish_position": finish,
        }
    )


def train(df: pd.DataFrame):
    X = df[FEATURE_COLS]
    y = df[TARGET_COL]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = GradientBoostingClassifier(
        n_estimators=200, max_depth=4, learning_rate=0.05, random_state=42
    )
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred, zero_division=0))

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")
    return model


def predict(features: dict):
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("Train the model first: python predictor.py --train")
    model = joblib.load(MODEL_PATH)
    df = pd.DataFrame([features])[FEATURE_COLS]
    return int(model.predict(df)[0])


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="F1 Race Predictor")
    parser.add_argument("--train", action="store_true", help="Train the model")
    parser.add_argument("--predict", action="store_true", help="Run example prediction")
    args = parser.parse_args()

    if args.train or not args.predict:
        df = load_data()
        train(df)

    if args.predict:
        example = {
            "grid_position": 3,
            "qualifying_time_ms": 78500,
            "driver_points_before_race": 210,
            "constructor_points_before_race": 380,
            "circuit_id": 5,
            "weather_code": 0,
            "safety_car_laps": 2,
            "pit_stop_count": 2,
        }
        result = predict(example)
        print(f"Predicted finish position: P{result}")
