# Contributing to F1 Race Predictor

## Getting Started

1. Fork and clone the repository
2. Create a branch: `git checkout -b feature/your-feature`
3. Set up environment:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

4. Run `python predictor.py --train` to verify setup
5. Apply linting: `ruff check .` and `black .`
6. Open a Pull Request

## Data

If contributing new features, add corresponding columns to the synthetic data generator in `_generate_synthetic_data()` so CI can run without a real dataset.
