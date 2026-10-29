# 03 classic ml (in progress)

Starting with scikit-learn.

- `01_linear_regression.py`: predicting score from study hours
- `02_train_test_split.py`: diabetes dataset, comparing train vs test scores
- `03_classification.py`: iris flowers with logistic regression, KNN and a decision tree
- `04_project_breast_cancer_classifier.py`: full small project with scaling, two models, a confusion matrix and feature importance

Things I learned:
- regression = predict a number, classification = predict a category
- only trust the test set score
- accuracy isn't everything. For cancer, missing a malignant case is way worse, so I looked at recall too
- scaling the features helped logistic regression

Still to do here: cross-validation, overfitting/underfitting, feature engineering, clustering.

![classifier report](output/classifier_report.png)
