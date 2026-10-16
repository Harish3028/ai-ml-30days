- [x] Day 0: Environment setup
- [x] Day 1: Python for Java developers
  - Functions (`def`), list / dict / tuple / set
  - Comprehensions: `[item.upper() for item in my_items]`
  - Exceptions: `try`, `except`, `finally`, `raise ValueError`
  - File handling: reading and writing with `open`
  - Classes, inheritance, and `__str__`
  - Modules: `__name__ == "__main__"`
  - Mini-project: Grade Tracker (`src/mini-projects/Day01/student-grade-tracker`)
    - Reads a messy score file, skips invalid lines with reasons, and writes a grade report
    - Uses validation with `raise ValueError`, plus new tools `lambda` and `strip()`
    - Run: `python src\mini-projects\Day01\student-grade-tracker\grade_tracker.py`
  - Practice project: Expense Tracker (`src/mini-projects/Day01/expenses-tracker`)
    - Reads a messy expenses file, skips invalid lines with reasons, and writes an expense report
    - Same pipeline as the Grade Tracker, plus `float()` for amounts and a dict for category totals
    - Run: `python src\mini-projects\Day01\expenses-tracker\expense_tracker.py`

- [x] Day 2: NumPy foundations
  - Arrays vs Python lists, and vectorized math
  - Reproducible randomness: `np.random.default_rng(42)`
  - Array attributes: `shape`, `size`, `ndim`, `dtype`
  - Indexing and slicing (slices are views, not copies)
  - Boolean masks and `np.where`
  - `reshape` and the `axis` argument
  - Broadcasting
  - Mini-project: Exam Analyzer (`src/mini-projects/Day02/exam-analyzer`)
    - Analyzes a matrix of student scores and saves a text report
    - Uses `axis`, `argmax`, `argmin`, `argsort`, `np.where` and `np.minimum`
    - Run: `python src\mini-projects\Day02\exam-analyzer\exam_analyzer.py`
  - Practice project: Sales Analyzer (`src/mini-projects/Day02/sales-analyzer`)
    - Analyzes units sold per product and month, with revenue, tiers, growth and a saved report
    - Uses broadcasting with a `(6, 1)` column, `np.diff`, `np.cumsum`, `keepdims=True`, `any` and `all`
    - Run: `python src\mini-projects\Day02\sales-analyzer\sales_analyzer.py`
    
- [x] Day 3: Pandas
  - `Series`, `DataFrame` and reading CSV files
  - Selecting with `.loc` and `.iloc`, filtering with boolean masks, `sort_values`
  - `groupby` with named aggregation, and `merge` (`left`, `inner`, `outer`)
  - Missing values: `isna`, `dropna(subset=...)`, `fillna`
  - Duplicates: `duplicated` and `drop_duplicates`
  - Cleaning text with `.str.strip().str.title()`
  - Fixing types with `pd.to_numeric` and `pd.to_datetime` (`errors="coerce"`)
  - Mini-project: Messy Orders Cleaner (`src/mini-projects/Day03/orders-cleaner`)
    - Cleans a messy orders CSV step by step, logs how many rows each step removes, and saves
      `orders_clean.csv` and `report.txt` 
    - Uses text cleaning, `errors="coerce"`, duplicate and outlier removal, `groupby` summaries and a
      category `merge`
    - Run: `python src\mini-projects\Day03\orders-cleaner\orders_cleaner.py`

- [x] Day 4: Data cleaning and EDA
    - EDA health check: shape, types, `isna`, `duplicated`, `describe`, `value_counts`
    - Imputation distorts distributions (the Titanic age spike), and an outlier is not always an error
    - Distributions and outliers with histograms, boxplots and the IQR rule
    - Comparing groups with `groupby` and `pd.crosstab`; `groupby(B)[A].mean()` gives P(A | B)
    - Encoding text as numbers (`is_female`), the correlation matrix and heatmap (`.corr()` works only on 
      numbers)
    - Rates vs counts, and Simpson's paradox (bill length vs bill depth)
    - Mini-project: Penguins EDA (`src/mini-projects/Day04/`)
      - Health check, cleaning decisions, distributions, group comparisons, relationships and written findings
        with numbers
      - Uses Matplotlib and Seaborn charts, `crosstab`, `groupby`, a correlation heatmap and a Findings cell
      - Run: Open `src\mini-projects\Day04\penguins-eda\penguins_eda.ipynb` and Run All

- [x] Day 5: Statistics and probability
    - Mean, median, mode, variance and std (`n` in NumPy vs `n - 1` in pandas)
    - Percentiles (`np.percentile`, `.quantile`), percentile rank, Q1 / Q3 and the IQR fences
    - Covariance, correlation, z-score and the normal distribution (68-95-99.7 rule)
    - Probability basics: law of large numbers, "not" / "and" rules, conditional probability
    - Why the 3-std rule needs enough data, and how an outlier inflates its own mean and std
    - Mini-project: Diamonds Outliers (`src/mini-projects/Day05/`)
      - Compares the IQR rule and the z-score rule on 53,940 diamonds across 7 columns
      - Uses my own `iqr_mask` and `z_mask` functions, fences for price, and a check of errors vs real extreme
        values
      - Run: Open `src\mini-projects\Day05\diamond-outliers\diamond_outliers.ipynb` and Run All

- [x] Day 6: Math for ML (vectors, derivatives, gradient descent)
    - Scalars, vectors and matrices; the dot product as a weighted sum (`x @ w + b`)
    - Matrix multiplication and its shape rule `(a, b) @ (b, c) -> (a, c)`
    - Derivatives, partial derivatives and the gradient
    - Gradient descent: `w = w - lr * dw`, `b = b - lr * db`
    - Mini-project: Linear Regression from Scratch (`src/mini-projects/Day06/`)
      - Fits `y = w*x + b` to 50 noisy points with NumPy only, then checks the result against `np.polyfit`
      - Uses `predict`, `mse`, `gradients` and `train`, learning rate experiments (too small, right, too big)
        and a loss curve
      - Run: Open `src\mini-projects\Day06\linear-gradientDescent\linear_gradientDescent.ipynb` and Run All

- [x] Day 7: ML workflow and data leakage
    - Features and label, and the train / validation / test split
    - `train_test_split` with `random_state` and `stratify`
    - Baseline model with `DummyClassifier`
    - Filling missing values with `SimpleImputer`, using numbers from the training data only
    - `Pipeline`, and how to spot data leakage (target leakage and preprocessing leakage)
    - Mini-project: Leakage-safe ML Workflow on Titanic (`src/mini-projects/Day07/`)
      - Runs the full workflow: split, baseline, model, evaluation, Pipeline and a deliberate leak check
      - Uses scikit-learn's `LogisticRegression` as a black box (studied on Day 9)
      - Run: Open `src\mini-projects\Day07\ml-workflow\ml_workflow_titanic.ipynb` and Run All

- [x] Day 8: Regression & Linear Regression
  - Regression vs classification; `LinearRegression` with `.fit`, `.predict`, `.coef_` and `.intercept_`
  - Regression metrics: MAE, MSE, RMSE and R² (R² below 0 means worse than the baseline)
  - Text categories as numbers with `pd.get_dummies` (one-hot encoding), and feature engineering with ratio
    columns.
  - Polynomial regression with `PolynomialFeatures` and `StandardScaler`, and how overfitting shows up (train
    score keeps rising while validation score gets worse)
  - Train / validation / test split: compare models on validation, score the chosen model on test once
  - Residual analysis: error by group, impossible (negative) predictions, and why one extreme row can wreck
    the average error
  - Mini-project: House-Price Regression (`src/mini-projects/Day08/`)
    - Cleans 20,640 California housing districts (965 capped prices removed), adds 3 ratio features and
      compares 4 models on validation
    - Uses `Pipeline`, `SimpleImputer`, `PolynomialFeatures`, a `report` helper, a baseline and a residual
      study of the final model
    - Run: open `src\mini-projects\Day08\house-price-regression\house_price_regression.ipynb` and Run All

- [x] Day 9: Classification and logistic regression
  - Sigmoid, `LogisticRegression`, `predict_proba` vs `predict`, and the decision threshold
  - Odds ratios with `np.exp(coef_)`, multiclass classification, and why `LinearRegression` is not a
    good fit for classification
  - Confusion matrix (TN, FP, FN, TP), accuracy, precision, recall and F1
  - ROC-AUC, class imbalance, and the precision / recall trade-off when the threshold changes
  - Mini-project: Telecom Churn Classifier (`src/mini-projects/Day09/churn-classifier/`)
    - Predicts which of 7,043 customers will leave, then chooses the threshold on validation and scores the
      chosen model on test once
    - Uses `get_dummies`, `Pipeline` with `StandardScaler`, `confusion_matrix`, `roc_auc_score`, odds ratios
      and a threshold table
    - Run: open `src\mini-projects\Day09\churn-classifier\churn_classifier.ipynb` and Run All

- [x] Day 10: Decision trees and Random Forest
  - Decision tree: Gini impurity and entropy, information gain, greedy splits, and a leaf as the majority
    class
  - Why an unlimited tree memorises the training data, and how `max_depth`, `min_samples_split` and
    `min_samples_leaf` limit it
  - Random Forest: bootstrap samples, a random subset of features per split, and voting (bagging)
  - Out-of-bag (OOB) score, `n_estimators`, and why more trees steady the forest but do not make it overfit
  - Feature importance vs permutation importance, and why neither proves what causes churn
  - Fair model comparison: same split and metric, choose on validation, score the test set once
  - Mini-project: Random Forest vs Logistic Regression on Churn 
                  (`src/mini-projects/Day10/churn-random-forest`)
    - Reuses the Day 9 churn data and splits, then compares a baseline, one tree, a default forest, a tuned
      forest and logistic regression
    - Uses `RandomForestClassifier`, a `make_forest` helper, a parameter grid on validation, a threshold table
      and `permutation_importance`
    - Run: open `src\mini-projects\Day10\churn-random-forest\churn_random_forest.ipynb` and Run All

- [x] Day 11: Overfitting and underfitting
  - Underfitting (high bias) vs overfitting (high variance), and how to read the train vs validation gap
  - Bias-variance tradeoff, the complexity curve and the learning curve ("would more data help?")
  - Regularization: Ridge `alpha` (big alpha = strong penalty), and why it rescues an overfit model without
    beating a simpler one
  - The best complexity depends on how much data you have (rows per feature)
  - Mini-project: Overfitting Detective (`src/mini-projects/Day11/overfitting-detective/`)
    - Compares polynomial degrees 1 to 5 on 200 rows vs 11,805 rows of California housing, then a learning
      curve, a Ridge sweep and a variance test
    - Uses `PolynomialFeatures`, `StandardScaler`, `LinearRegression`, `Ridge`, a `take` helper and repeated
      sampling
    - Run: open `src\mini-projects\Day11\overfitting-detective\overfitting_detective.ipynb` and Run All
