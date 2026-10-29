"""Day 1 - pandas intro. A DataFrame is like an Excel table you control with code."""
from pathlib import Path
import pandas as pd

df = pd.read_csv(Path(__file__).parent / "students.csv")
print(df.head(), "\n")
print(df.describe(), "\n")                     # quick stats for each numeric column

df["passed"] = df["score"] >= 60               # add a new column
print("Students who passed:\n", df[df["passed"]][["name", "score"]], "\n")
print("Top student:", df.loc[df["score"].idxmax(), "name"])
print("Avg score by pass/fail:\n", df.groupby("passed")["score"].mean())
