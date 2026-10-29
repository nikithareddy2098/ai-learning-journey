"""Stage 3 - Train/test split: test the model on data it has NEVER seen.
Scoring on training data is like grading an exam using the answer key you studied from."""
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

X, y = load_diabetes(return_X_y=True)        # built-in dataset, no download needed
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Train rows:", len(X_train), "| Test rows:", len(X_test))

model = LinearRegression().fit(X_train, y_train)
for name, Xs, ys in [("train", X_train, y_train), ("test", X_test, y_test)]:
    pred = model.predict(Xs)
    print(f"{name:>5}: R^2={r2_score(ys, pred):.3f}  MAE={mean_absolute_error(ys, pred):.1f}")
