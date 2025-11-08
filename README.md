# ⚽ Soccer Match Predictor - Premier League

Machine Learning project to predict Premier League match outcomes with 72%+ accuracy using intelligent feature engineering.

## 📊 Project Status: 50% Complete
```
████████████░░░░░░░░░░░░ 50%
```

### ✅ Completed
- [x] Project setup & structure (Nov 5, 2024)
- [x] Data collection - 760 matches from 2023-24 season (Nov 5, 2024)
- [x] Exploratory Data Analysis (Nov 5, 2024)
  - Home advantage confirmed: 43.4% wins vs 33.6% away
  - Average 3.11 goals per match
  - Top performers: Man City, Liverpool, Arsenal
- [x] **Pandas Bootcamp - Mastered 10 essential functions** (Nov 7, 2024)
- [x] **Feature Engineering - 10 ML-ready features created** (Nov 7, 2024)

### 🚧 In Progress
- [ ] Model Training (Logistic Regression, Random Forest, XGBoost)
- [ ] Model Evaluation & Optimization
- [ ] Final deployment & documentation

## 🎯 Goal

Build a soccer match predictor that achieves **accuracy** through intelligent feature engineering rather than just collecting massive datasets.

**Philosophy:** 760 matches + smart features > 5000 matches + basic features

## 🧠 Feature Engineering Highlights

### 10 Features Created (Nov 7, 2024)

**1. Recent Form Analysis**
- `home_form`: Points from last 5 home matches
- `away_form`: Points from last 5 away matches  
- `form_diff`: Form difference (key predictor!)

**2. Goals Trends**
- `home_goals_scored_avg`: Average goals scored at home
- `home_goals_conceded_avg`: Average goals conceded at home
- `away_goals_scored_avg`: Average goals scored away
- `away_goals_conceded_avg`: Average goals conceded away

**3. Strength Differentials**
- `offensive_strength_diff`: Who has better attack?
- `defensive_strength_diff`: Who has better defense?

**4. Target Variable**
- `result`: Match outcome (Home Win / Away Win / Draw)

### Key Insights from Features
- Form difference ranges from -12 to +15 points
- Man City averages 2.47 goals/match at home (league best)
- Home teams concede 0.21 fewer goals on average
- Features capture momentum, attacking prowess, and defensive solidity

## 🗂️ Project Structure
```
soccer-predictor/
├── data/
│   ├── raw/                           # Original API data (760 matches)
│   └── processed/                     # Feature-engineered dataset ✅
│       └── matches_with_features.csv
├── notebooks/
│   ├── 01_data_exploration.ipynb      ✅ Complete
│   ├── 02_feature_engineering.ipynb   ✅ Complete  
│   ├── pandas_practice.ipynb          ✅ Complete
│   └── 03_model_training.ipynb        🚧 Next
├── src/
│   └── scraping/
│       └── fetch_pl_data.py           ✅ Complete
└── README.md
```

## 🛠️ Tech Stack

- **Data Collection:** Football-Data.org API
- **Data Processing:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn, XGBoost (coming soon)
- **Development:** Jupyter Notebooks, Git, Python 3.9+

## 📊 Dataset

- **Source:** Football-Data.org API
- **League:** Premier League 2023-24 Season
- **Matches:** 760 (full season)
- **Teams:** 20 Premier League clubs
- **Features:** 10 engineered features
- **Target:** Match result (H/D/A)

*Note: Raw and processed data are stored locally following ML best practices.*

## 🚀 Next Steps

1. ✅ ~~Master pandas fundamentals~~
2. ✅ ~~Engineer intelligent features~~
3. 🚧 Train baseline model (Logistic Regression)
4. 🚧 Implement ensemble models (Random Forest, XGBoost)
5. 🚧 Compare model performances & feature importance
6. 🚧 Hyperparameter tuning
7. 🚧 Final evaluation and documentation

## 📝 Learning Journey

This project emphasizes:
- **Quality over quantity:** Smart features beat big data
- **Feature engineering first:** Models are only as good as the features
- **Domain knowledge:** Soccer understanding informs better features
- **Time-aware features:** Avoiding data leakage in time-series data
- **Iterative improvement:** Build, test, learn, repeat

## 🎓 Skills Demonstrated

- REST API integration and data collection
- Exploratory Data Analysis with visualization
- Feature engineering for time-series/sports data
- Pandas data manipulation (groupby, filtering, aggregations)
- Machine Learning pipeline design
- Git version control workflow
- Technical documentation

## 📈 Progress Timeline

- **Nov 5, 2024:** Project setup, data collection, EDA
- **Nov 7, 2024:** Pandas bootcamp, feature engineering (10 features)
- **Coming Next:** Model training and evaluation

---

**Current Status:** Feature engineering complete, ready for ML training
**Target Accuracy:** 72%+
**Next Session:** Build and train prediction models

## 📝 License
MIT
