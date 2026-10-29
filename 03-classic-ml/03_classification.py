"""Stage 3 - Classification: predict a CATEGORY (here: which iris flower species)."""
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.3, random_state=0, stratify=data.target)

models = {
    "Logistic Regression": LogisticRegression(max_iter=500),
    "K-Nearest Neighbors": KNeighborsClassifier(n_neighbors=5),
    "Decision Tree": DecisionTreeClassifier(max_depth=3, random_state=0),
}
for name, model in models.items():
    model.fit(X_train, y_train)
    print(f"{name:<20} accuracy: {accuracy_score(y_test, model.predict(X_test)):.3f}")

best = models["Logistic Regression"]
pred = best.predict(X_test)
print("\nConfusion matrix (rows = true, cols = predicted):\n", confusion_matrix(y_test, pred))
print(classification_report(y_test, pred, target_names=data.target_names))
