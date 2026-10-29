"""Stage 3 MINI-PROJECT: End-to-end classifier - tumor benign vs malignant.
Steps: load -> explore -> split -> scale -> train -> evaluate -> save chart.
Dataset: scikit-learn's built-in Breast Cancer Wisconsin dataset (569 samples, 30 features)."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

OUT = Path(__file__).parent / "output"
OUT.mkdir(exist_ok=True)

# 1. Load & explore
data = load_breast_cancer(as_frame=True)
df = data.frame
print("Shape:", df.shape)
print("Class balance:", df["target"].map(dict(enumerate(data.target_names))).value_counts().to_dict())

# 2. Split
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 3. Train two models (scaling puts all features on a similar range)
models = {
    "Logistic Regression": make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000)),
    "Random Forest": RandomForestClassifier(n_estimators=200, random_state=42),
}
results = {}
for name, m in models.items():
    m.fit(X_train, y_train)
    p = m.predict(X_test)
    # recall on class 0 (malignant): of real malignant cases, how many did we catch?
    results[name] = (accuracy_score(y_test, p), recall_score(y_test, p, pos_label=0))
    print(f"{name:<20} accuracy={results[name][0]:.3f}  malignant recall={results[name][1]:.3f}")

# 4. Feature importance + confusion matrix chart
rf = models["Random Forest"]
top = pd.Series(rf.feature_importances_, index=X.columns).nlargest(8).sort_values()
fig, (a1, a2) = plt.subplots(1, 2, figsize=(12, 4.5))
top.plot.barh(ax=a1, color="seagreen"); a1.set_title("Top 8 features (Random Forest)")
ConfusionMatrixDisplay.from_estimator(models["Logistic Regression"], X_test, y_test,
                                      display_labels=data.target_names, ax=a2, colorbar=False)
a2.set_title("Logistic Regression - test set")
fig.tight_layout(); fig.savefig(OUT / "classifier_report.png", dpi=120)
print("Saved output/classifier_report.png")
