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


### 2023-03-30
- feat: add model persistence with joblib serialisation


### 2023-03-31
- feat: add feature importance output after training


### 2023-03-31
- refactor: extract evaluation metrics into helper function


### 2023-04-05
- feat: add example prediction with sample input dictionary


### 2023-04-05
- test: add regression test for model prediction stability


### 2023-04-13
- feat: implement batch prediction from CSV file input


### 2023-04-13
- fix: fix random state parameter for full reproducibility


### 2023-04-16
- feat: add safety car laps count as race variable


### 2023-04-18
- test: add unit tests for feature engineering correctness


### 2023-04-25
- feat: add model persistence with joblib serialisation


### 2023-05-01
- refactor: consolidate model save and load logic


### 2023-05-03
- feat: add training CLI flag via argparse


### 2023-05-03
- docs: add model training guide to README setup section


### 2023-05-04
- docs: add model selection rationale to architecture.md


### 2023-05-08
- docs: document all eight feature definitions and rationale


### 2023-05-24
- style: format with black


### 2023-05-25
- feat: implement qualifying time feature in milliseconds


### 2023-05-29
- docs: add model selection rationale to architecture.md


### 2023-05-31
- chore: add .gitignore for model and data files


### 2023-06-02
- feat: implement pit stop count as strategy proxy feature


### 2023-06-02
- perf: cache fitted label encoder to avoid re-fitting


### 2023-06-08
- docs: document synthetic data schema and generation logic


### 2023-06-14
- refactor: rename feature columns for clarity


### 2023-06-15
- chore: add .gitignore for model and data files


### 2023-06-15
- feat: add training progress logging to stdout


### 2023-06-22
- refactor: rename feature columns for clarity


### 2023-06-23
- feat: add driver championship points before race feature


### 2023-06-24
- docs: add model selection rationale to architecture.md


### 2023-06-30
- refactor: extract evaluation metrics into helper function


### 2023-07-10
- chore: add pre-commit hooks for black and ruff


### 2023-07-14
- feat: implement hyperparameter configuration via constants


### 2023-07-21
- feat: add training progress logging to stdout


### 2023-08-01
- feat: implement hyperparameter configuration via constants


### 2023-08-02
- test: add model save and reload round-trip test


### 2023-08-15
- refactor: separate synthetic data into data_utils module


### 2023-08-16
- test: add regression test for model prediction stability


### 2023-08-21
- chore: pin scikit-learn to 1.3 for API stability


### 2023-08-22
- style: fix ruff violations in predictor module


### 2023-08-22
- feat: add model persistence with joblib serialisation


### 2023-08-25
- fix: correct feature ordering in prediction input dict


### 2023-09-06
- fix: handle missing values in qualifying time column


### 2023-09-07
- feat: add driver championship points before race feature


### 2023-09-07
- feat: add grid position as primary input feature


### 2023-09-12
- test: add unit tests for feature engineering correctness


### 2023-09-12
- docs: document prediction input dict schema


### 2023-09-18
- test: add regression test for model prediction stability


### 2023-09-21
- feat: add circuit-specific encoding as categorical feature


### 2023-09-22
- fix: fix random state parameter for full reproducibility


### 2023-09-25
- feat: add synthetic data generator for demo and CI mode


### 2023-09-26
- chore: add .gitignore for model and data files


### 2023-09-30
- docs: document prediction input dict schema


### 2023-09-30
- test: add unit tests for feature engineering correctness


### 2023-10-02
- feat: add safety car laps count as race variable


### 2023-10-02
- feat: add synthetic data generator for demo and CI mode


### 2023-10-03
- feat: implement classification report with per-class metrics


### 2023-10-05
- docs: add model training guide to README setup section


### 2023-10-07
- fix: fix safety car lap count parsing from raw data


### 2023-10-12
- fix: handle edge case with zero pit stops in feature


### 2023-10-14
- refactor: separate synthetic data into data_utils module


### 2023-10-19
- docs: document all eight feature definitions and rationale


### 2023-10-21
- style: format with black


### 2023-10-27
- feat: implement 80/20 train-test split with random seed


### 2023-10-29
- refactor: extract feature engineering into sklearn pipeline


### 2023-10-30
- chore: add .gitignore for model and data files


### 2023-11-02
- docs: document prediction input dict schema


### 2023-11-06
- feat: implement pit stop count as strategy proxy feature


### 2023-11-09
- docs: add model training guide to README setup section


### 2023-11-13
- feat: add example prediction with sample input dictionary


### 2023-11-14
- feat: add feature importance output after training


### 2023-11-16
- fix: handle corrupt joblib file with clear error message


### 2023-11-21
- docs: document synthetic data schema and generation logic


### 2023-11-22
- feat: implement qualifying time feature in milliseconds


### 2023-11-22
- docs: document prediction input dict schema


### 2023-11-23
- feat: implement qualifying time feature in milliseconds


### 2023-11-26
- perf: cache fitted label encoder to avoid re-fitting


### 2023-11-29
- feat: implement batch prediction from CSV file input


### 2023-12-01
- refactor: extract evaluation metrics into helper function


### 2023-12-04
- fix: handle new circuit IDs at prediction time gracefully


### 2023-12-08
- chore: add pre-commit hooks for black and ruff


### 2023-12-09
- feat: implement weather condition code as ordinal feature


### 2023-12-12
- test: add regression test for model prediction stability


### 2023-12-13
- fix: handle missing values in qualifying time column


### 2023-12-15
- test: add model save and reload round-trip test


### 2023-12-27
- feat: implement batch prediction from CSV file input


### 2023-12-28
- chore: update requirements.txt with pinned versions


### 2023-12-29
- chore: add .gitignore for model and data files


### 2023-12-29
- docs: add model training guide to README setup section


### 2024-01-04
- docs: add model selection rationale to architecture.md


### 2024-01-05
- feat: add feature importance output after training


### 2024-01-09
- docs: document prediction input dict schema


### 2024-01-11
- refactor: rename feature columns for clarity


### 2024-01-11
- perf: use joblib parallel backend for cross-validation


### 2024-01-19
- feat: implement pit stop count as strategy proxy feature


### 2024-01-24
- refactor: extract feature engineering into sklearn pipeline


### 2024-01-30
- refactor: separate synthetic data into data_utils module


### 2024-01-31
- feat: implement weather condition code as ordinal feature


### 2024-02-02
- fix: handle edge case with zero pit stops in feature


### 2024-02-13
- test: add model save and reload round-trip test


### 2024-02-13
- fix: resolve label encoding issue for unseen circuit IDs


### 2024-02-18
- feat: implement weather condition code as ordinal feature


### 2024-02-21
- chore: pin scikit-learn to 1.3 for API stability


### 2024-02-22
- feat: add safety car laps count as race variable


### 2024-03-01
- feat: implement prediction CLI flag for inference


### 2024-03-05
- refactor: separate synthetic data into data_utils module


### 2024-03-05
- fix: resolve joblib version compatibility with sklearn


### 2024-03-07
- feat: implement qualifying time feature in milliseconds


### 2024-03-08
- test: add CLI argument parsing tests


### 2024-03-12
- test: add model save and reload round-trip test


### 2024-03-14
- fix: handle edge case with zero pit stops in feature


### 2024-03-14
- feat: add driver championship points before race feature


### 2024-03-18
- refactor: extract evaluation metrics into helper function


### 2024-03-25
- perf: use joblib parallel backend for cross-validation


### 2024-03-31
- fix: resolve joblib version compatibility with sklearn


### 2024-04-03
- style: format with black


### 2024-04-05
- feat: implement prediction CLI flag for inference


### 2024-04-10
- fix: fix random state parameter for full reproducibility


### 2024-04-12
- style: normalise imports with isort


### 2024-04-13
- test: add model save and reload round-trip test


### 2024-04-14
- feat: add training CLI flag via argparse


### 2024-04-19
- chore: update requirements.txt with pinned versions


### 2024-04-22
- perf: use joblib parallel backend for cross-validation


### 2024-04-29
- docs: document all eight feature definitions and rationale


### 2024-04-30
- refactor: rename feature columns for clarity


### 2024-05-10
- feat: implement qualifying time feature in milliseconds


### 2024-05-15
- feat: implement weather condition code as ordinal feature


### 2024-05-21
- feat: implement 80/20 train-test split with random seed


### 2024-05-25
- fix: correct model save path creation when models dir missing


### 2024-06-05
- fix: handle missing values in qualifying time column


### 2024-06-07
- feat: add circuit-specific encoding as categorical feature


### 2024-06-10
- docs: document all eight feature definitions and rationale


### 2024-06-11
- perf: use joblib parallel backend for cross-validation


### 2024-06-15
- refactor: extract feature engineering into sklearn pipeline


### 2024-06-20
- docs: update architecture.md with ML pipeline diagram


### 2024-06-27
- feat: implement GradientBoostingClassifier for position prediction


### 2024-06-27
- feat: implement pit stop count as strategy proxy feature


### 2024-07-08
- fix: fix random state parameter for full reproducibility


### 2024-07-12
- perf: cache fitted label encoder to avoid re-fitting


### 2024-07-12
- chore: pin scikit-learn to 1.3 for API stability


### 2024-07-21
- fix: handle missing values in qualifying time column


### 2024-07-21
- test: add CLI argument parsing tests


### 2024-07-21
- feat: add example prediction with sample input dictionary


### 2024-07-25
- feat: implement prediction CLI flag for inference


### 2024-07-27
- test: add regression test for model prediction stability


### 2024-08-01
- feat: implement batch prediction from CSV file input


### 2024-08-01
- feat: add example prediction with sample input dictionary


### 2024-08-05
- feat: implement batch prediction from CSV file input


### 2024-08-09
- perf: use joblib parallel backend for cross-validation


### 2024-08-12
- chore: add .gitignore for model and data files


### 2024-08-12
- feat: implement GradientBoostingClassifier for position prediction


### 2024-08-14
- feat: add training CLI flag via argparse


### 2024-08-15
- test: add unit tests for feature engineering correctness


### 2024-08-16
- refactor: extract feature engineering into sklearn pipeline


### 2024-08-17
- test: add synthetic data generator shape and type tests


### 2024-09-05
- feat: add driver championship points before race feature


### 2024-09-05
- perf: use joblib parallel backend for cross-validation


### 2024-09-21
- feat: implement 80/20 train-test split with random seed


### 2024-10-02
- feat: add grid position as primary input feature


### 2024-10-03
- refactor: rename feature columns for clarity


### 2024-10-07
- feat: implement GradientBoostingClassifier for position prediction


### 2024-10-08
- refactor: extract feature engineering into sklearn pipeline


### 2024-10-08
- style: format with black


### 2024-10-09
- fix: handle new circuit IDs at prediction time gracefully


### 2024-10-09
- refactor: extract evaluation metrics into helper function


### 2024-10-11
- test: add model save and reload round-trip test


### 2024-10-12
- fix: correct model save path creation when models dir missing


### 2024-10-16
- style: format with black


### 2024-10-20
- fix: correct feature ordering in prediction input dict


### 2024-10-22
- fix: correct model save path creation when models dir missing


### 2024-10-24
- style: normalise imports with isort


### 2024-10-25
- test: add regression test for model prediction stability


### 2024-10-26
- feat: implement hyperparameter configuration via constants


### 2024-10-30
- fix: handle corrupt joblib file with clear error message


### 2024-10-31
- test: add model save and reload round-trip test


### 2024-10-31
- fix: handle missing values in qualifying time column


### 2024-11-01
- feat: implement GradientBoostingClassifier for position prediction


### 2024-11-01
- docs: update architecture.md with ML pipeline diagram


### 2024-11-06
- style: fix ruff violations in predictor module


### 2024-11-09
- docs: update architecture.md with ML pipeline diagram


### 2024-11-13
- docs: document synthetic data schema and generation logic


### 2024-11-14
- docs: add model selection rationale to architecture.md


### 2024-11-15
- docs: update architecture.md with ML pipeline diagram


### 2024-11-28
- feat: implement prediction CLI flag for inference


### 2024-11-30
- test: add CLI argument parsing tests


### 2024-12-06
- docs: document all eight feature definitions and rationale


### 2024-12-20
- refactor: extract evaluation metrics into helper function


### 2024-12-20
- docs: document all eight feature definitions and rationale


### 2024-12-21
- fix: correct feature ordering in prediction input dict


### 2024-12-26
- chore: add pre-commit hooks for black and ruff


### 2024-12-26
- test: add model save and reload round-trip test


### 2025-01-06
- refactor: move model path to environment variable


### 2025-01-14
- feat: add training progress logging to stdout


### 2025-01-17
- fix: resolve label encoding issue for unseen circuit IDs


### 2025-01-23
- feat: implement batch prediction from CSV file input


### 2025-01-30
- chore: add pre-commit hooks for black and ruff


### 2025-02-05
- style: normalise imports with isort


### 2025-02-05
- test: add unit tests for feature engineering correctness


### 2025-02-11
- docs: document all eight feature definitions and rationale


### 2025-02-15
- feat: implement constructor performance points feature


### 2025-02-16
- fix: correct model save path creation when models dir missing


### 2025-02-17
- refactor: extract evaluation metrics into helper function


### 2025-02-17
- feat: implement classification report with per-class metrics


### 2025-02-19
- feat: add training progress logging to stdout


### 2025-02-26
- fix: resolve label encoding issue for unseen circuit IDs


### 2025-02-26
- style: format with black


### 2025-02-26
- feat: add training progress logging to stdout


### 2025-03-02
- test: add CLI argument parsing tests


### 2025-03-03
- style: normalise imports with isort


### 2025-03-14
- docs: document prediction input dict schema


### 2025-03-16
- chore: pin scikit-learn to 1.3 for API stability


### 2025-03-16
- fix: correct feature ordering in prediction input dict


### 2025-03-20
- chore: add pre-commit hooks for black and ruff


### 2025-03-27
- perf: use joblib parallel backend for cross-validation


### 2025-04-03
- test: add unit tests for feature engineering correctness


### 2025-04-05
- docs: document prediction input dict schema


### 2025-04-11
- test: add regression test for model prediction stability


### 2025-04-14
- feat: implement prediction CLI flag for inference


### 2025-04-18
- fix: fix safety car lap count parsing from raw data


### 2025-04-19
- perf: use joblib parallel backend for cross-validation


### 2025-04-29
- perf: cache fitted label encoder to avoid re-fitting


### 2025-04-30
- feat: implement qualifying time feature in milliseconds


### 2025-05-07
- feat: implement constructor performance points feature


### 2025-05-20
- docs: add model selection rationale to architecture.md


### 2025-05-23
- feat: add training CLI flag via argparse


### 2025-05-23
- test: add unit tests for feature engineering correctness


### 2025-05-24
- feat: add example prediction with sample input dictionary


### 2025-05-27
- fix: resolve label encoding issue for unseen circuit IDs


### 2025-05-28
- fix: handle missing values in qualifying time column


### 2025-05-30
- perf: use joblib parallel backend for cross-validation


### 2025-06-09
- docs: document synthetic data schema and generation logic


### 2025-06-11
- docs: update architecture.md with ML pipeline diagram


### 2025-06-23
- style: fix ruff violations in predictor module


### 2025-06-23
- fix: fix safety car lap count parsing from raw data


### 2025-06-24
- feat: implement GradientBoostingClassifier for position prediction


### 2025-06-26
- docs: document synthetic data schema and generation logic


### 2025-07-09
- feat: implement GradientBoostingClassifier for position prediction


### 2025-07-10
- chore: add pre-commit hooks for black and ruff


### 2025-07-11
- feat: add safety car laps count as race variable


### 2025-07-17
- fix: correct feature ordering in prediction input dict


### 2025-07-17
- feat: implement 80/20 train-test split with random seed


### 2025-07-24
- style: normalise imports with isort


### 2025-07-27
- docs: add model selection rationale to architecture.md


### 2025-08-02
- docs: document prediction input dict schema


### 2025-08-13
- feat: add feature importance output after training


### 2025-08-15
- feat: implement 80/20 train-test split with random seed


### 2025-08-15
- feat: implement hyperparameter configuration via constants


### 2025-08-18
- style: normalise imports with isort


### 2025-08-19
- feat: implement prediction CLI flag for inference


### 2025-08-20
- feat: implement pit stop count as strategy proxy feature


### 2025-08-22
- style: normalise imports with isort


### 2025-08-22
- feat: implement constructor performance points feature


### 2025-09-12
- feat: implement qualifying time feature in milliseconds


### 2025-09-13
- test: add synthetic data generator shape and type tests


### 2025-09-16
- feat: add model persistence with joblib serialisation


### 2025-09-19
- fix: resolve label encoding issue for unseen circuit IDs


### 2025-09-28
- fix: fix random state parameter for full reproducibility


### 2025-10-02
- feat: implement qualifying time feature in milliseconds


### 2025-10-02
- docs: add model selection rationale to architecture.md


### 2025-10-05
- feat: add example prediction with sample input dictionary


### 2025-10-07
- feat: add training CLI flag via argparse


### 2025-10-11
- fix: resolve label encoding issue for unseen circuit IDs


### 2025-10-13
- feat: add safety car laps count as race variable


### 2025-10-15
- feat: add training progress logging to stdout


### 2025-10-17
- feat: implement prediction CLI flag for inference


### 2025-10-21
- fix: fix safety car lap count parsing from raw data


### 2025-10-22
- feat: add feature importance output after training


### 2025-10-23
- docs: add model training guide to README setup section


### 2025-10-23
- perf: cache fitted label encoder to avoid re-fitting


### 2025-10-24
- fix: fix random state parameter for full reproducibility


### 2025-10-29
- test: add model save and reload round-trip test


### 2025-10-31
- feat: implement pit stop count as strategy proxy feature


### 2025-11-06
- feat: add synthetic data generator for demo and CI mode


### 2025-11-08
- feat: implement GradientBoostingClassifier for position prediction


### 2025-11-09
- style: normalise imports with isort


### 2025-11-12
- docs: add model selection rationale to architecture.md


### 2025-11-13
- test: add CLI argument parsing tests


### 2025-11-14
- feat: implement prediction CLI flag for inference


### 2025-11-15
- feat: implement pit stop count as strategy proxy feature


### 2025-11-17
- chore: add pre-commit hooks for black and ruff


### 2025-11-18
- feat: add model persistence with joblib serialisation


### 2025-11-20
- refactor: move model path to environment variable


### 2025-11-20
- fix: handle edge case with zero pit stops in feature


### 2025-11-26
- fix: fix safety car lap count parsing from raw data


### 2025-11-27
- refactor: separate synthetic data into data_utils module


### 2025-11-30
- docs: update architecture.md with ML pipeline diagram


### 2025-12-02
- docs: document synthetic data schema and generation logic


### 2025-12-02
- docs: add model selection rationale to architecture.md


### 2025-12-04
- fix: handle edge case with zero pit stops in feature


### 2025-12-04
- fix: resolve label encoding issue for unseen circuit IDs


### 2025-12-07
- feat: implement qualifying time feature in milliseconds


### 2025-12-17
- feat: add safety car laps count as race variable


### 2025-12-20
- docs: document all eight feature definitions and rationale


### 2025-12-23
- docs: add model training guide to README setup section


### 2025-12-31
- perf: use joblib parallel backend for cross-validation


### 2026-01-08
- test: add CLI argument parsing tests


### 2026-01-16
- feat: add example prediction with sample input dictionary


### 2026-01-22
- perf: cache fitted label encoder to avoid re-fitting


### 2026-02-02
- test: add unit tests for feature engineering correctness


### 2026-02-10
- docs: add model training guide to README setup section


### 2026-02-11
- perf: cache fitted label encoder to avoid re-fitting


### 2026-02-13
- test: add model save and reload round-trip test


### 2026-02-14
- docs: add model training guide to README setup section


### 2026-02-18
- feat: add driver championship points before race feature


### 2026-02-22
- fix: resolve label encoding issue for unseen circuit IDs


