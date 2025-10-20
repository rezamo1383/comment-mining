# Comment Mining - NLP - scikit-learn

This repository contains a reproducible NLP project for **comment mining** using a Jupyter Notebook and CSV datasets.

**Task:** Binary Sentiment Classification / Comment Mining.

## What this project covers
- Clean, structured NLP notebook for comment mining
- Classical ML baselines with TF-IDF + scikit-learn

## Repository structure
```
.
├── data
│   ├── raw
│   │   ├── train.csv
│   │   └── test.csv
│   └── processed/
├── notebooks
│   └── comment_mining.ipynb
├── reports
│   └── figures/
├── src
│   └── quick_check.py
├── requirements.txt
└── .gitignore
```

## Datasets
- Train rows: **40000**
- Test rows: **8000**
- Candidate text column: **comment**
- Candidate label column: **price_value**

**Train columns:**
- `comment`
- `price_value`

**Test columns:**
- `comment`

## Getting started
```bash
python -m venv .venv
# activate env ...
pip install -r requirements.txt
jupyter notebook notebooks/comment_mining.ipynb
```

Quick sanity check:
```bash
python -m src.quick_check
```
