# 03 · Classic Machine Learning 🟡

Machine learning with **scikit-learn**: models that learn patterns from examples.

| Script | Concept |
|---|---|
| `01_linear_regression.py` | Predict a number; slope, intercept, R² |
| `02_train_test_split.py` | Evaluate on unseen data; MAE and R² |
| `03_classification.py` | Predict a category; compare 3 models; confusion matrix, precision/recall |
| `04_project_breast_cancer_classifier.py` | 🏁 **Mini-project:** end-to-end tumor classifier with scaling, 2 models, feature importance |

## 🏁 Mini-project result
![Classifier report](output/classifier_report.png)

## 📝 Notes
- **Regression** predicts a number (price, score). **Classification** predicts a category (spam / not spam).
- Always split into **train** and **test** sets. The test score is the honest one.
- **Accuracy** can mislead on imbalanced data. **Recall** = of the real positives, how many did we catch? (In medicine, missing a malignant case is the worst error.)
- **Scaling** (StandardScaler) helps models like logistic regression that are sensitive to feature ranges.
- **Coming next:** cross-validation, overfitting vs underfitting, feature engineering, clustering.
