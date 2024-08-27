# Changelog

All notable changes are documented here.


### 2022-01-18
- feat: add grid position as primary input feature


### 2022-01-19
- style: fix ruff violations in predictor module


### 2022-01-21
- docs: add model training guide to README setup section


### 2022-01-24
- chore: add .gitignore for model and data files


### 2022-01-26
- chore: add pre-commit hooks for black and ruff


### 2022-01-27
- feat: add safety car laps count as race variable


### 2022-02-09
- chore: pin scikit-learn to 1.3 for API stability


### 2022-02-09
- feat: add circuit-specific encoding as categorical feature


### 2022-02-19
- feat: implement batch prediction from CSV file input


### 2022-02-24
- style: format with black


### 2022-03-04
- chore: add .gitignore for model and data files


### 2022-03-06
- fix: correct model save path creation when models dir missing


### 2022-03-11
- docs: add model selection rationale to architecture.md


### 2022-03-13
- chore: add pre-commit hooks for black and ruff


### 2022-03-16
- feat: add training progress logging to stdout


### 2022-03-16
- feat: add synthetic data generator for demo and CI mode


### 2022-03-17
- feat: implement qualifying time feature in milliseconds


### 2022-03-21
- refactor: move model path to environment variable


### 2022-03-23
- feat: add driver championship points before race feature


### 2022-03-26
- chore: pin scikit-learn to 1.3 for API stability


### 2022-04-01
- feat: add synthetic data generator for demo and CI mode


### 2022-04-06
- feat: implement batch prediction from CSV file input


### 2022-04-06
- style: fix ruff violations in predictor module


### 2022-04-07
- feat: add driver championship points before race feature


### 2022-04-11
- feat: implement classification report with per-class metrics


### 2022-04-11
- feat: implement 80/20 train-test split with random seed


### 2022-04-22
- docs: update architecture.md with ML pipeline diagram


### 2022-04-26
- chore: update requirements.txt with pinned versions


### 2022-04-28
- feat: add example prediction with sample input dictionary


### 2022-05-05
- fix: fix safety car lap count parsing from raw data


### 2022-05-13
- docs: add model selection rationale to architecture.md


### 2022-05-17
- test: add CLI argument parsing tests


### 2022-05-21
- chore: pin scikit-learn to 1.3 for API stability


### 2022-05-25
- feat: add driver championship points before race feature


### 2022-05-30
- docs: document synthetic data schema and generation logic


### 2022-05-30
- feat: add example prediction with sample input dictionary


### 2022-05-31
- refactor: extract evaluation metrics into helper function


### 2022-06-01
- refactor: consolidate model save and load logic


### 2022-06-02
- test: add CLI argument parsing tests


### 2022-06-02
- feat: implement hyperparameter configuration via constants


### 2022-06-03
- style: fix ruff violations in predictor module


### 2022-06-08
- fix: correct model save path creation when models dir missing


### 2022-06-09
- feat: implement 80/20 train-test split with random seed


### 2022-06-13
- feat: add feature importance output after training


### 2022-06-20
- perf: cache fitted label encoder to avoid re-fitting


### 2022-06-22
- fix: handle edge case with zero pit stops in feature


### 2022-06-25
- fix: handle corrupt joblib file with clear error message


### 2022-06-28
- refactor: move model path to environment variable


### 2022-06-30
- refactor: extract feature engineering into sklearn pipeline


### 2022-07-11
- fix: resolve label encoding issue for unseen circuit IDs


### 2022-07-16
- style: normalise imports with isort


### 2022-07-18
- refactor: separate synthetic data into data_utils module


### 2022-07-20
- feat: implement batch prediction from CSV file input


### 2022-07-22
- feat: implement GradientBoostingClassifier for position prediction


### 2022-07-26
- chore: add pre-commit hooks for black and ruff


### 2022-07-26
- fix: correct model save path creation when models dir missing


### 2022-07-26
- refactor: rename feature columns for clarity


### 2022-07-29
- fix: handle missing values in qualifying time column


### 2022-07-29
- chore: add .gitignore for model and data files


### 2022-08-01
- fix: resolve label encoding issue for unseen circuit IDs


### 2022-08-04
- feat: add example prediction with sample input dictionary


### 2022-08-08
- test: add model save and reload round-trip test


### 2022-08-08
- fix: correct model save path creation when models dir missing


### 2022-08-10
- feat: add driver championship points before race feature


### 2022-08-25
- feat: add grid position as primary input feature


### 2022-08-29
- feat: implement qualifying time feature in milliseconds


### 2022-08-30
- perf: use joblib parallel backend for cross-validation


### 2022-08-31
- feat: implement 80/20 train-test split with random seed


### 2022-09-13
- feat: add driver championship points before race feature


### 2022-09-15
- docs: add model training guide to README setup section


### 2022-09-15
- feat: implement qualifying time feature in milliseconds


### 2022-09-16
- fix: correct feature ordering in prediction input dict


### 2022-09-17
- fix: handle missing values in qualifying time column


### 2022-09-18
- refactor: extract feature engineering into sklearn pipeline


### 2022-09-20
- feat: add safety car laps count as race variable


### 2022-09-21
- feat: implement hyperparameter configuration via constants


### 2022-09-29
- refactor: move model path to environment variable


### 2022-10-03
- test: add CLI argument parsing tests


### 2022-10-05
- chore: update requirements.txt with pinned versions


### 2022-10-06
- fix: handle edge case with zero pit stops in feature


### 2022-10-12
- fix: resolve joblib version compatibility with sklearn


### 2022-10-12
- feat: add model persistence with joblib serialisation


### 2022-10-20
- feat: implement batch prediction from CSV file input


### 2022-10-21
- test: add CLI argument parsing tests


### 2022-10-22
- fix: resolve label encoding issue for unseen circuit IDs


### 2022-10-22
- feat: add training progress logging to stdout


### 2022-10-23
- feat: implement pit stop count as strategy proxy feature


### 2022-11-03
- refactor: separate synthetic data into data_utils module


### 2022-11-05
- fix: handle new circuit IDs at prediction time gracefully


### 2022-11-07
- docs: document synthetic data schema and generation logic


### 2022-11-12
- feat: implement classification report with per-class metrics


### 2022-11-19
- test: add CLI argument parsing tests


### 2022-11-22
- fix: fix random state parameter for full reproducibility


### 2022-11-28
- fix: fix safety car lap count parsing from raw data


### 2022-12-05
- feat: implement 80/20 train-test split with random seed


### 2022-12-08
- refactor: extract feature engineering into sklearn pipeline


### 2022-12-11
- docs: add model selection rationale to architecture.md


### 2022-12-18
- chore: pin scikit-learn to 1.3 for API stability


### 2022-12-29
- feat: implement batch prediction from CSV file input


### 2022-12-30
- refactor: rename feature columns for clarity


### 2023-01-03
- feat: implement batch prediction from CSV file input


### 2023-01-07
- feat: add model persistence with joblib serialisation


### 2023-01-09
- refactor: rename feature columns for clarity


### 2023-01-17
- test: add synthetic data generator shape and type tests


### 2023-01-24
- test: add CLI argument parsing tests


### 2023-01-26
- docs: add model training guide to README setup section


### 2023-01-26
- chore: pin scikit-learn to 1.3 for API stability


### 2023-02-04
- test: add regression test for model prediction stability


### 2023-02-05
- feat: add synthetic data generator for demo and CI mode


### 2023-02-15
- feat: add driver championship points before race feature


### 2023-02-16
- feat: implement pit stop count as strategy proxy feature


### 2023-02-23
- feat: add example prediction with sample input dictionary


### 2023-03-02
- refactor: rename feature columns for clarity


### 2023-03-02
- fix: fix random state parameter for full reproducibility


### 2023-03-02
- test: add CLI argument parsing tests


### 2023-03-02
- style: normalise imports with isort


### 2023-03-03
- fix: resolve label encoding issue for unseen circuit IDs


### 2023-03-09
- chore: add .gitignore for model and data files


### 2023-03-10
- chore: pin scikit-learn to 1.3 for API stability


### 2023-03-15
- chore: update requirements.txt with pinned versions


### 2023-03-16
- style: format with black


### 2023-03-23
- feat: add training progress logging to stdout


### 2023-03-25
- feat: implement constructor performance points feature


