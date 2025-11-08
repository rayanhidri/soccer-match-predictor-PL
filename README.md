# ⚽ Premier League Match Outcome Predictor

Machine Learning system achieving **53% accuracy** on soccer match predictions through intelligent feature engineering and ensemble modeling.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![ML](https://img.shields.io/badge/ML-XGBoost%20%7C%20RandomForest-orange.svg)
![Accuracy](https://img.shields.io/badge/Accuracy-53.29%25-success.svg)

## 🎯 Project Overview

Built an end-to-end machine learning pipeline to predict Premier League match outcomes (Home Win/Draw/Away Win) using 760 matches across 2 seasons. The XGBoost model achieves **53.29% accuracy**, outperforming the baseline by **9.8 points** and matching published academic benchmarks.

### Key Achievements
- ✅ **53.29% prediction accuracy** on **3-class classification**
- ✅ **25 engineered features** from historical match data
- ✅ **+9.87 points** improvement over baseline (43.42%)
- ✅ Matches top academic research benchmarks (50-55%)

**Philosophy: Build a soccer match predictor that achieves **accuracy** through intelligent feature engineering rather than just collecting massive datasets.**

## 📊 Results Summary

| Model | Train Accuracy | Test Accuracy | vs Baseline |
|-------|----------------|---------------|-------------|
| **XGBoost** | 89.14%   | **53.29%**    | **+9.87**   |
| RF | 95.72% | 51.32%   | +7.90         |             |
| LR | 53.45% | 46.05%   | +2.63         |             |


## 🧠 Feature Engineering

Created **25 time-aware features** to capture team performance and momentum:

### 1. Form Analysis (3 features)
- Recent form (last 5 matches points)
- Home/away form differential
- Momentum trends

### 2. Goals Trends (6 features)
- Average goals scored/conceded
- Offensive/defensive strength differentials
- Home vs away goal patterns

### 3. Market Value (3 features)
- Team market value (€78M - €1.28B range)
- Value differential between opponents
- Quality gap indicator

### 4. Performance Metrics (6 features)
- Win rates (home/away specific)
- Cumulative points
- Goal difference trends

### 5. Context Features (7 features)
- Rest days between matches
- Big 6 team indicators
- Season position tracking

**Key Innovation:** All features calculated using only data **before** each match to prevent data leakage.

## 🛠️ Tech Stack

- **Languages:** Python 3.9+
- **ML Libraries:** Scikit-learn, XGBoost, NumPy
- **Data Processing:** Pandas
- **Visualization:** Matplotlib, Seaborn
- **Development:** Jupyter Notebooks, Git
- **Data Source:** Football-Data.org API

## 📁 Project Structure
```
soccer-predictor/
├── data/
│   ├── raw/                    # Original match data (760 matches)
│   └── processed/              # Feature-engineered dataset
├── notebooks/
│   ├── 01_data_exploration.ipynb      # EDA and insights
│   ├── 02_feature_engineering.ipynb   # Feature creation
│   └── 03_model_training.ipynb        # Model comparison
├── src/
│   └── scraping/
│       └── fetch_pl_data.py           # Data collection script
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

### Installation
```bash
# Clone the repository
git clone https://github.com/rayanhidri/soccer-match-predictor-PL.git
cd soccer-predictor

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Running the Notebooks
```bash
# Start Jupyter
jupyter notebook

# Run notebooks in order:
# 1. 01_data_exploration.ipynb
# 2. 02_feature_engineering.ipynb
# 3. 03_model_training.ipynb
```

## 📈 Model Performance Details

### Confusion Matrix (XGBoost)
```
Predicted →    Away  Draw  Home
Actual ↓
Away            32    5    14     (62.7% recall)
Draw            14    4    17     (11.4% recall)
Home            13    8    45     (68.2% recall)
```

### Key Insights
- **Home wins** predicted with 68% accuracy
- **Away wins** predicted with 63% accuracy  
- **Draws** remain challenging (23% of matches, hard to predict)

### Feature Importance (Top 5)
1. **Market Value Differential** - 21.6%
2. **Cumulative Points (Home)** - 11.9%
3. **Win Rate Differential** - 11.2%
4. **Cumulative Points (Away)** - 11.0%
5. **Form Differential** - 10.3%

## 🎓 Learning Outcomes

### Technical Skills Developed
- End-to-end ML pipeline design
- Time-series feature engineering
- Handling class imbalance (43%/34%/23% distribution)
- Hyperparameter optimization
- Model evaluation and comparison

### Key Challenges Solved
1. **Data Leakage Prevention:** Implemented strict temporal validation
2. **Class Imbalance:** Used class weighting and ensemble methods
3. **Overfitting:** Reduced through regularization (40% → 36% train-test gap)

## 📊 Dataset

- **Source:** Football-Data.org API
- **League:** Premier League (England)
- **Seasons:** 2022-23, 2023-24
- **Matches:** 760 total
- **Teams:** 23 (including promoted/relegated)

## 🔮 Future Improvements

- [ ] Incorporate betting odds as features (+3-5% accuracy potential)
- [ ] Add player-level data (injuries, ratings)
- [ ] Implement deep learning models (LSTM for sequences)
- [ ] Expand to multiple leagues
- [ ] Real-time prediction API
- [ ] Dynamic market value updates

## 📝 Project Timeline

**Nov 5, 2024:** Project setup, data collection, EDA  
**Nov 7, 2024:** Feature engineering (25 features)  
**Nov 8, 2024:** Model training, optimization, final results

**Total Development Time:** ~15-20 hours

## 🤝 Contributing

This is a portfolio project, but suggestions and feedback are welcome! Feel free to open an issue or reach out!

## 📬 Contact

**Rayan Hidri**  
- LinkedIn: [https://www.linkedin.com/in/rayan-hidri/]
- Email: [rayan.hidri@umontreal.ca]

## 📄 License

MIT License - feel free to use this project for learning purposes.

---
⭐ **If you found this project interesting, please star the repo!**

