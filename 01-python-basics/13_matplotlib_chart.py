"""Stage 1 - Your first chart with matplotlib, saved as a PNG."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")                 # draw to file, no window needed
import matplotlib.pyplot as plt
import pandas as pd

here = Path(__file__).parent
df = pd.read_csv(here / "students.csv")

plt.figure(figsize=(6, 4))
plt.scatter(df["hours_studied"], df["score"], color="teal")
for _, row in df.iterrows():
    plt.annotate(row["name"], (row["hours_studied"], row["score"]), fontsize=8)
plt.title("Hours studied vs score")
plt.xlabel("Hours studied")
plt.ylabel("Score")
plt.grid(alpha=0.3)
(here / "output").mkdir(exist_ok=True)
plt.savefig(here / "output" / "hours_vs_score.png", dpi=120, bbox_inches="tight")
print("Saved output/hours_vs_score.png")
