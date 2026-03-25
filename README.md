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

- Session duration and average BPM emerged as the strongest drivers of `Calories_Burned`, and the engineered `BPM_Duration_Index` helped capture workout effort more directly.
- Tree-based models clearly outperformed linear and distance-based baselines on this dataset.
- `GradientBoostingRegressor` was the best overall untuned model, achieving `CV_MSE = 118.756` and `CV_R2 = 0.998576` on the held-out evaluation used in the notebook.
- `RandomForestRegressor` was the next-best untuned model with `CV_MSE = 484.346` and `CV_R2 = 0.994194`, while `KNeighborsRegressor` lagged far behind with `CV_MSE = 7468.796` and `CV_R2 = 0.910473`.

Below are cross-validated results for models evaluated (CV_MSE reported as mean squared error on validation folds; CV_R2 is mean R²):

| Model | CV_MSE | CV_R2 |
|---|---:|---:|
| GradientBoosting | 118.756340 | 0.998576 |
| RandomForest | 484.346195 | 0.994194 |
| DecisionTreeRegressor | 673.630769 | 0.991925 |
| Lasso | 829.172143 | 0.990061 |
| LinearRegression | 829.202452 | 0.990061 |
| Ridge | 853.381660 | 0.989771 |
| KNN | 7468.796023 | 0.910473 |

Hyperparameter tuning was then applied to the top tree-based candidates:

| Tuned Model | Tuned_CV_MSE | Tuned_CV_R2 | Best Parameters |
|---|---:|---:|---|
| GradientBoosting | 179.832458 | 0.997436 | `learning_rate=0.1`, `max_depth=3`, `min_samples_split=2`, `n_estimators=200` |
| DecisionTreeRegressor | 1163.660066 | 0.983855 | `criterion='poisson'`, `max_depth=16`, `min_samples_split=2`, `splitter='best'` |
| RandomForest | 2315.150297 | 0.967408 | `max_depth=None`, `max_features='sqrt'`, `min_samples_leaf=1`, `min_samples_split=2`, `n_estimators=500` |

Overall takeaway:

- Gradient boosting remained the most reliable model after tuning and is the recommended choice for prediction in this project.
- The tuning step did not improve on the notebook's earlier untuned test-set results for random forest or decision tree, which suggests the original gradient boosting configuration was already close to optimal for this dataset.
- From a business perspective, workout intensity and duration matter more than purely demographic fields, so gyms and fitness apps can use these variables to estimate calorie burn and personalize workout recommendations.


#### Next steps

- Use k-fold cross-validation (with more folds) and report confidence intervals for metrics.
- Try more advanced models (e.g., `HistGradientBoostingRegressor`, XGBoost, LightGBM) and ensembling.
- Calibrate and validate the model on an external dataset if available.
- Build a lightweight web app or notebook widget to let users input session parameters and get predicted calories burned.

#### Outline of project
- [Notebook — Gym Members Exercise Analysis](gym_member_exercise.ipynb)

##### Contact and Further Information

For questions or collaboration, open an issue in this repository or contact the author (Sumeet) via the project GitHub profile. See `gym_member_exercise.ipynb` for code, visualizations, and detailed results.
