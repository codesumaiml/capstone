### Project Title

**Gym Members — Workout Insights & Predicting Calories Burned**

**Author**

Sumeet

#### Executive summary

This project analyzes the Gym Members Exercise Dataset to build regression models that predict `Calories_Burned` from demographic, physiological, and workout-related features. The workflow includes exploratory data analysis, feature engineering, preprocessing, training several regression models, and evaluating their performance using MSE and R².

#### Rationale

- Understanding what drives calorie expenditure during workouts helps trainers, fitness apps, and gym members personalize training plans and set more accurate goals. Predicting calories burned from readily available features (age, session duration, average BPM, workout type, etc.) provides actionable insights without expensive equipment.

- Gym retention and member engagement are critical to long-term business success. Without clear insight into what
drives workout effectiveness, gyms risk offering generic programs that fail to meet member needs. This project
converts workout data into actionable insights that non-technical stakeholders can use to personalize training
programs, optimize resource allocation, reduce member churn, and improve overall satisfaction.

#### Research Question

- Can we predict an individual's calories burned during a gym session using demographic and workout features such as session duration, average BPM, workout type, BMI, and experience level?

- Which workout behaviors and member characteristics most strongly influence gym performance outcomes such as
calories burned and workout consistency, and how can these insights be used to improve member engagement and
retention?

#### Data Sources

- Local file: `data/gym_members_exercise_tracking.csv`
- Original dataset: https://www.kaggle.com/datasets/valakhorasani/gym-members-exercise-dataset

#### Methodology

This project follows the CRISP-DM framework:

- Business Understanding : what drives calorie expenditure during workouts?
- Data Understanding : Exploratory data analysis to understand distributions and relationships between variables.
- Data Preparation | Feature engineering: created `Age_Group`, `BPM_Duration_Index` (Avg_BPM * Session_Duration), and `Intensity` (Avg_BPM / Session_Duration).
- Data Preparation | Preprocessing: numeric imputation (median), scaling (StandardScaler), categorical imputation (most frequent) and one-hot encoding.
- Modeling : Models evaluated: `LinearRegression`, `Ridge`, `Lasso`, `KNeighborsRegressor`, `RandomForestRegressor`, `GradientBoostingRegressor`.
- Evaluation: train/test split and cross-validation using `mean_squared_error` (sklearn returns MSE) and `r2` as scoring metrics. Reported metrics include MSE (negated when using sklearn scorers) and R².

#### Results

- Session duration and average BPM were identified as strong predictors of calories burned.
- Feature engineering (BPM-duration index and intensity) improved interpretability of workout effort.
- Tree-based models (Random Forest / Gradient Boosting) tended to perform better than simple linear models in this dataset, producing lower MSE and higher R² in held-out evaluation. Exact numeric results and model comparisons are available in the notebook `gym_member_exercise.ipynb`.

#### Next steps

- Perform hyperparameter tuning (GridSearchCV or RandomizedSearchCV) for top models.
- Use k-fold cross-validation (with more folds) and report confidence intervals for metrics.
- Try more advanced models (e.g., `HistGradientBoostingRegressor`, XGBoost, LightGBM) and ensembling.
- Calibrate and validate the model on an external dataset if available.
- Build a lightweight web app or notebook widget to let users input session parameters and get predicted calories burned.

#### Outline of project
- [Notebook — Gym Members Exercise Analysis](gym_member_exercise.ipynb)

##### Contact and Further Information

For questions or collaboration, open an issue in this repository or contact the author (Sumeet) via the project GitHub profile. See `gym_member_exercise.ipynb` for code, visualizations, and detailed results.
