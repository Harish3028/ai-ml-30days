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

- [x] Day 12: Model improvement
  - K-fold and stratified K-fold cross-validation: `cross_val_score`, `cross_validate` and
    `cross_val_predict`, mean +- std, and the tie rule (one standard error)
  - Scaling: who needs it (KNN yes, logistic regression barely, forests no), and feature selection with
    `SelectKBest` inside the `Pipeline` so it never sees the validation rows
  - Hyperparameters (`max_depth`, `min_samples_leaf`, `n_estimators`, `max_features`),
    `GridSearchCV` vs `RandomizedSearchCV`, and `best_estimator_`
  - Choosing a threshold on out-of-fold predictions and scoring the test set once
  - Mini-project: Forest Tuning Lab (`src/mini-projects/Day12/forest-tuning-lab/`)
    - Rules written before any search, then a 16-setting grid, one-at-a-time checks and a random search on
      the churn data; the forest vs logistic regression ends in a tie, so logistic regression is shipped
    - Uses `StratifiedKFold`, `GridSearchCV`, `RandomizedSearchCV`, a `cv` helper, a tie band and a
      bootstrap check of the test AUC gap
    - Run: open `src\mini-projects\Day12\forest-tuning-lab\forest_tuning_lab.ipynb` and Run All
  - Recall project: Adult Playbook (`src/mini-projects/recall/recall-day1-day12/`)
    - Takes the Adult Census data from raw file to a tested model in 10 stages: clean, decide columns,
      split, encode, compare, tune and test once
    - Uses `Pipeline`, `cross_validate`, `GridSearchCV`, `permutation_importance` and a check of results
      by sex
    - Run: open `src\mini-projects\recall\recall-day1-day12\adult_playbook.ipynb` and Run All

- [x] Day 13: PyTorch fundamentals
  - Tensors: `shape`, `dtype` and `device`, creating them (`torch.tensor`, `zeros`, `arange`, `linspace`,
    `rand`), `reshape`, indexing, broadcasting and `@` (matrix multiply)
  - The three checks on every tensor (shape, dtype, device) and the error each one causes; CPU vs GPU with
    `.to(device)`; the NumPy bridge (`from_numpy` shares memory, `.clone()` makes a copy)
  - Autograd: `requires_grad`, `backward()` and `.grad`, why gradients accumulate (`zero_()`),
    `torch.no_grad()` and `detach()`; gradient descent by hand on a line, checked against `np.polyfit`
  - `Dataset` (`__len__` and `__getitem__`) and `DataLoader` (`batch_size`, `shuffle`, `drop_last`), and
    what an epoch and a batch are
  - Mini-project: Churn DataLoader Lab (`src/mini-projects/Day13/dataloader-lab/`)
    - Turns the 7,043-customer churn table into float32 tensors (train-only median and `StandardScaler`),
      wraps them in a `Dataset` and serves 89 training batches of 64 with a `DataLoader`
    - Uses `StandardScaler`, `torch.tensor`, a `PairDataset` class, `DataLoader`, a rows-and-churners
      check every epoch and one `backward()` on a real batch
    - Run: open `src\mini-projects\Day13\dataloader-lab\dataloader_lab.ipynb` in Google Colab and Run All

- [x] Day 14: Neural networks with PyTorch
  - A neuron (weighted sum + bias + activation), a layer as many neurons side by side, and `nn.Linear` weight
    shape `(out_features, in_features)`
  - Activation functions: ReLU, sigmoid and softmax, and why layers need an activation (two linear layers
    in a row collapse into one)
  - Forward pass, loss (`MSELoss`, `BCEWithLogitsLoss` on raw logits) and backpropagation checked by hand
    (`p - y` at the output)
  - `nn.Module` and `nn.Sequential`, an optimizer (`SGD`, `Adam`), and the five-line training step
    (`zero_grad`, forward, loss, `backward`, `step`)
  - A straight line cannot fit a curve, a hidden layer with ReLU can, and an unlucky random start can leave
    the ReLU units dead
  - Mini-project: Churn Neural Classifier (`src/mini-projects/Day14/churn-nn-classifier/`)
    - Compares a single neuron (24 parameters), one hidden layer (401) and a bigger network (1,601) on the
      churn data with a 60/20/20 split; the validation loss shows the bigger networks overfitting, so the
      single neuron is chosen and the test set is opened once (AUC 0.832)
    - Uses `nn.Linear`, `nn.Sequential`, `nn.ReLU`, `BCEWithLogitsLoss`, `Adam`, a `fit` helper and an
      `evalm` helper, with the median and `StandardScaler` fitted on the training rows only
    - Run: open `src\mini-projects\Day14\churn-nn-classifier\churn_nn_classifier.ipynb` in Google Colab and
      Run All

- [x] Day 15: Training neural networks
  - Epoch, batch and batch size (updates per epoch = ceil(rows / batch size), e.g. 4,225 rows with batch
    size 64 gives 67 updates), and mini-batch vs full-batch training
  - Learning rate as the size of each weight update (too big overshoots, too small is slow), and how
    SGD, SGD with momentum, Adam and AdamW differ
  - The training loop (`model.train()`, `zero_grad`, `backward`, `step`) vs the validation loop
    (`model.eval()`, `torch.no_grad()`, no weight updates), written as one `run_epoch` function that
    weights each batch loss by `len(yb)` and returns loss and AUC
  - A `train_model` helper that keeps a history of train loss, validation loss and validation AUC
  - Reading loss curves: train loss falls while validation loss turns up (overfitting); best epoch 11
    (validation loss 0.4367, then 0.4545 by epoch 40), a preview of early stopping on Day 17
  - Checking a metric that looks too good: a validation AUC computed on only the last batch because
    the prediction lists were emptied every batch

- [x] Day 16: PyTorch project: image classification
  - Multiclass classification: 10 logits, softmax, `CrossEntropyLoss` on raw logits with `long` labels of
    shape `(N,)`, and an untrained model starting near ln(10) = 2.3026
  - `model.train()`, `model.eval()` and `torch.no_grad()`; accuracy with `argmax`, a confusion matrix and
    per-class recall
  - `state_dict`: `torch.save` and `load_state_dict` into the same architecture, and the trap that
    `state_dict()` returns references (use `copy.deepcopy` to keep the best epoch)
  - Mini-project: Digit Classifier (`src/mini-projects/Day16/digit-classifier/`)
    - Classifies the 1,797 handwritten 8x8 digit images (60/20/20 split, pixels divided by 16) with a custom
      `Dataset` and `DataLoader`; compares a single layer (650 parameters), one hidden layer (4,810) and two
      hidden layers (17,226); the tie rule chooses the one-hidden-layer model (validation accuracy 0.975),
      which is saved and reloaded, then the test set is opened once (accuracy 0.9639)
    - Uses `Dataset`, `DataLoader`, `nn.Linear`, `nn.ReLU`, `CrossEntropyLoss`, `Adam`, `run_epoch` and
      `train_model` helpers, `confusion_matrix` and a plot of the misclassified images
    - Run: open `src\mini-projects\Day16\digit-classifier\digit_classifier.ipynb` in Google Colab and Run All

- [x] Day 17: Deep learning problems
  - Overfitting in a network vs a forest: capacity (rows per parameter), time (epochs) and many knobs,
    judged by loss curves
  - Dropout (`nn.Dropout`, switched off by `model.eval()`), weight decay (`AdamW` shrinks the weights
    separately from Adam's step), early stopping (patience, restore the best weights), learning-rate
    schedulers (`StepLR`, `ReduceLROnPlateau`) and data augmentation (noise and shifts, training set only)
  - Mini-project: Regularisation Lab (`src/mini-projects/Day17/regularisation-lab/`)
    - Takes the overfitting two-hidden-layer digit network from Day 16 and changes one thing at a time; a
      change counts only if the best validation loss is more than 10% below the baseline (0.0731); noise 0.1
      wins (0.0388), dropout 0.3 and AdamW 0.1 help, the wrap-around shift and weight decay 1.0 hurt, and
      stacking regularisers did not add up; the test set stays closed
    - Uses `nn.Dropout`, `AdamW`, `StepLR`, `ReduceLROnPlateau`, an `AugDataset` class and a `train_model2`
      helper with patience and a scheduler
    - Run: open `src\mini-projects\Day17\regularisation-lab\regularisation_lab.ipynb` in Google Colab and
      Run All
  - Recall project: House Prices (`src/mini-projects/recall2/recall-day1-day17/`)
    - Takes the house prices data (1,460 houses) from raw file to a tested model in 11 stages: clean and decide
      which missing values are real, split and remove two outliers from the training part only, compare
      Ridge, a forest, XGBoost and a PyTorch regression network, and open the test set once (Ridge chosen by
      the tie rule; RMSE 0.1278 on the log price, R2 0.912, typical error 5.5%)
    - Uses `Pipeline`, `SimpleImputer`, `Ridge`, `RandomForestRegressor`, `XGBRegressor` (early stopping and
      importances), `KFold`, a tie rule, `nn.Sequential` with `MSELoss`, `AdamW` and dropout, and an error
      table by house quality
    - Run: open `src\mini-projects\recall2\recall-day1-day17\house_prices_playbook.ipynb` and Run All; the
      network stage is `house_prices_playbook_stage_10.ipynb` in Google Colab

- [x] Day 18: CNN and transfer learning
  - Convolution as a sliding window of shared weights: a kernel on a window (multiply and add), padding,
    stride, the output-size formula `floor((n + 2p - k) / s) + 1`, max pooling, and the CNN recipe
    (Conv, ReLU, Pool, Flatten, Linear) on tensors of shape `(N, C, H, W)`, with parameter counts checked by
    hand (`Conv2d(1, 8, 3)` has 80)
  - A `conv2d` function written with two loops in NumPy and checked against hand-computed tables
  - A small CNN on the Day 16 digits (1,370 parameters) ties the 4,810-parameter network (test accuracy
    0.9667 against 0.9639, a difference of one image)
  - Mini-project: Ants or Bees (`src/mini-projects/Day18/cnn-project/`)
    - Compares a pretrained ResNet-18 used as a feature extractor (1,026 trainable parameters), the same
      network fine-tuned (`layer4` and `fc`, 8.4 million) and a copy without pretraining, on 244 training
      and 153 validation photos; the first two tie (0.9608 and 0.9542), the run without pretraining reaches
      only 0.6536 (always guessing the majority class gives 0.5425), so the feature extractor is chosen
    - Uses `ImageFolder`, `transforms` (ImageNet mean and std, random crop and flip for training only),
      `models.resnet18`, freezing with `requires_grad`, `Adam` with two learning rates, and a `run_epoch`
      helper that keeps BatchNorm in eval mode
    - Run: open `src\mini-projects\Day18\cnn-project\cnn_project.ipynb` in Google Colab (T4 GPU) and Run All

- [x] Day 19: NLP foundations
  - Text to numbers: preprocessing, tokenization (word, character, subword), a vocabulary with `<PAD>` and
    `<UNK>`, Bag of Words with cosine similarity, TF-IDF (`tf x ln(N / df)`), embeddings as a learned table
    (`nn.Embedding`), padding with an attention mask, and the idea of attention (softmax, then a weighted sum),
    all worked by hand on a four-sentence corpus
  - `build_vocab`, `to_ids` and `bow` written with loops and dictionaries
  - Mini-project: Spam or Ham (`src/mini-projects/Day19/text-classifier/`)
    - Takes 5,572 SMS messages (13.4% spam) from raw text to a tested spam detector; accuracy is misleading
      (always guessing ham scores 0.866), so F1 on the spam class is used; five TF-IDF + logistic regression
      variants are compared by cross-validation with the tie rule, next to an embedding-average network in
      PyTorch; `tfidf + LR balanced, C=10` is chosen before the test set is opened (test F1 0.9485, precision
      0.9718, recall 0.9262)
    - Uses `TfidfVectorizer`, `CountVectorizer`, `Pipeline`, `StratifiedKFold`, `cross_validate`,
      `nn.Embedding` with `padding_idx`, a masked average and `BCEWithLogitsLoss`
    - Run: open `src\mini-projects\Day19\text-classifier\text_classifier.ipynb` and Run All (an internet
      connection is needed to read the data)

- [x] Day 20: Transformers
  - Self-attention with query, key and value (`softmax(Q K^T / sqrt(d_k)) V`), why the scores are divided by
    `sqrt(d_k)`, multi-head attention, positional encoding (sinusoidal and learned), the transformer block
    (attention, add and norm, feed-forward, add and norm), encoder versus decoder and the causal mask; the
    parameters of one block counted by hand (872)
  - Attention and positional encoding written in NumPy and checked against hand-computed tables, including a
    shuffle test
  - Mini-project: Tiny Transformer (`src/mini-projects/Day20/tiny-transformer/`)
    - Builds one self-attention block in PyTorch (checked against the hand-computed attention; 115,329
      parameters), trains it on the same SMS data and compares it with the Day 19 models on the validation
      split; it does not beat the averaging network or TF-IDF (F1 0.895 to 0.911, validation loss 0.083 to
      0.108), so the Day 19 choice stands and the test set stays closed; one empty message turned the softmax
      into `nan` until `encode` was fixed
    - Uses a `SelfAttention` layer, a `Block` with `nn.LayerNorm` and a feed-forward network, position
      vectors from `nn.Embedding`, and the attention table to see which words a spam message attended to
    - Run: open `src\mini-projects\Day20\tiny-transformer\tiny_transformer.ipynb` and Run All (an internet
      connection is needed to read the data)
