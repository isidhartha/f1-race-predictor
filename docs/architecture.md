# Architecture — F1 Race Predictor

## Overview

A classical supervised learning pipeline that frames finishing position prediction as a multi-class classification problem (classes 1–20, one per grid slot).

## Feature Engineering

Raw features were selected for causal relevance to race outcome:

| Feature | Rationale |
|---------|-----------|
| `grid_position` | Strongest predictor — track position at race start |
| `qualifying_time_ms` | Raw pace indicator |
| `driver_points_before_race` | Season form / experience |
| `constructor_points_before_race` | Car competitiveness |
| `circuit_id` | Some drivers/teams excel at specific tracks |
| `weather_code` | Wet races produce more variable results |
| `safety_car_laps` | Safety car periods compress the field |
| `pit_stop_count` | Strategy proxy |

No feature scaling is required — GBM is tree-based and invariant to monotonic transforms.

## Model Selection

Gradient Boosting was chosen over:
- **Random Forest**: GBM generally achieves lower bias at the cost of longer training — acceptable for this dataset size
- **XGBoost/LightGBM**: Would be the next step for production; sklearn GBM chosen here for zero extra dependencies
- **Neural network**: Tabular data with <10k rows doesn't benefit from deep learning

## Train/Test Split

80/20 random split with `random_state=42` for reproducibility. No time-series split is applied in this version — a future improvement would be to use season-based splits to prevent data leakage.

## Model Persistence

`joblib.dump` serialises the fitted estimator to `models/f1_predictor.joblib`. `joblib` is preferred over `pickle` for scikit-learn objects due to better handling of large NumPy arrays.
