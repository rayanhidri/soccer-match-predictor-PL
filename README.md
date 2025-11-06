# ⚽ Soccer Match Predictor

Machine Learning model predicting Premier League match outcomes with high accuracy.

## 🎯 Goal
Build an end-to-end ML pipeline to predict football match results using historical data.

## 🔧 Tech Stack
- Python 3.9
- Pandas, NumPy (data processing)
- Scikit-learn, XGBoost (ML models)
- Matplotlib, Seaborn (visualization)

## 📊 Progress

### ✅ Completed (Nov 5, 2024)
- [x] Project setup (structure, venv, Git)
- [x] Data collection via football-data.org API (760 matches, 2 seasons)
- [x] Exploratory Data Analysis (EDA)
  - Home advantage: 43.4% vs 33.6%
  - Average 3.11 goals per match
  - Top teams identified (Man City, Liverpool, Arsenal)
  - Visualizations created

### 🚧 Next Steps
- [ ] Pandas fundamentals bootcamp (master the basics!)
- [ ] Feature engineering (form, market value, head-to-head)
- [ ] Model training (Random Forest, XGBoost)
- [ ] Model evaluation and optimization

## 📂 Project Structure
```
soccer-predictor/
├── data/
│   ├── raw/              # 760 PL matches (CSV)
│   └── processed/        # Cleaned data (coming soon)
├── notebooks/            # Jupyter notebooks
│   └── 01_data_exploration.ipynb  ✅ Complete
├── src/
│   ├── scraping/        # Data fetching scripts ✅
│   ├── preprocessing/   # Data cleaning (coming soon)
│   └── models/          # ML models (coming soon)
└── results/             # Graphs, metrics (coming soon)
```

## 📝 License
MIT