"""Stage 1 - More pandas: missing values, filtering, groupby."""
from pathlib import Path
import pandas as pd

df = pd.read_csv(Path(__file__).parent / "study_data.csv")
print("Missing values per column:\n", df.isna().sum(), "\n")

# Cleaning: fill missing numbers with the column median, drop rows with no score
df["hours_studied"] = df["hours_studied"].fillna(df["hours_studied"].median())
df["sleep_hours"] = df["sleep_hours"].fillna(df["sleep_hours"].median())
df = df.dropna(subset=["score"])
print("Rows after cleaning:", len(df))

# Filtering with multiple conditions (& = and, | = or)
print("\nStudied 5+ hours AND slept 7+:\n", df[(df.hours_studied >= 5) & (df.sleep_hours >= 7)])

# Group by city
print("\nPer city:\n", df.groupby("city").agg(avg_score=("score", "mean"), students=("name", "count")))
print("\nSorted by score:\n", df.sort_values("score", ascending=False)[["name", "score"]].head(3))
