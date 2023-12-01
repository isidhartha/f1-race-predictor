# Module API — F1 Race Predictor

---

## `load_data(path: str) → pd.DataFrame`

Loads training data from a CSV file. If the file doesn't exist, generates a synthetic dataset of 5,000 rows.

**Columns required:** `grid_position`, `qualifying_time_ms`, `driver_points_before_race`, `constructor_points_before_race`, `circuit_id`, `weather_code`, `safety_car_laps`, `pit_stop_count`, `finish_position`

---

## `train(df: pd.DataFrame) → GradientBoostingClassifier`

Trains the model on the provided DataFrame, prints a classification report, saves the model to `MODEL_PATH`, and returns the fitted estimator.

---

## `predict(features: dict) → int`

Loads the saved model and predicts the finishing position for a single race.

**Parameters:** `features` — dict with keys matching `FEATURE_COLS`

**Returns:** predicted finishing position (1–20)

**Raises:** `FileNotFoundError` if model has not been trained yet

---

## `_generate_synthetic_data(n: int) → pd.DataFrame`

Generates `n` synthetic race records for demo/CI use. Finish position is correlated with grid position plus uniform noise.
