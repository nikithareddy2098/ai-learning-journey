"""Mini project: what lines up with higher scores?
Combines everything: files, functions, error handling, pandas, NumPy, matplotlib.
Outputs: output/report.txt and output/study_report.png"""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

HERE = Path(__file__).parent
OUT = HERE / "output"

def load_and_clean(path):
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        raise SystemExit(f"Data file not found: {path}")
    for col in ["hours_studied", "sleep_hours"]:
        df[col] = df[col].fillna(df[col].median())
    return df.dropna(subset=["score"])

def build_report(df):
    corr_hours = np.corrcoef(df.hours_studied, df.score)[0, 1]
    corr_sleep = np.corrcoef(df.sleep_hours, df.score)[0, 1]
    best = df.loc[df.score.idxmax()]
    city = df.groupby("city")["score"].mean().round(1)
    lines = [
        "STUDY DATA REPORT",
        "=================",
        f"Students analyzed: {len(df)}",
        f"Average score: {df.score.mean():.1f}",
        f"Top student: {best['name']} ({best.score:.0f})",
        f"Correlation hours vs score: {corr_hours:.2f}",
        f"Correlation sleep vs score: {corr_sleep:.2f}",
        "Average score by city:",
        *[f"  {c}: {s}" for c, s in city.items()],
        "Conclusion: " + ("study hours matter most." if abs(corr_hours) > abs(corr_sleep) else "sleep matters most."),
    ]
    return "\n".join(lines), city

def make_chart(df, city):
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4))
    a1.scatter(df.hours_studied, df.score, color="purple")
    m, b = np.polyfit(df.hours_studied, df.score, 1)          # best-fit line
    xs = np.linspace(df.hours_studied.min(), df.hours_studied.max(), 50)
    a1.plot(xs, m * xs + b, "--", color="orange", label=f"trend: +{m:.1f} pts/hour")
    a1.set(title="Hours studied vs score", xlabel="Hours", ylabel="Score"); a1.legend()
    a2.bar(city.index, city.values, color="skyblue")
    a2.set(title="Average score by city", ylabel="Score")
    fig.tight_layout()
    fig.savefig(OUT / "study_report.png", dpi=120)

if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    df = load_and_clean(HERE / "study_data.csv")
    report, city = build_report(df)
    (OUT / "report.txt").write_text(report + "\n")
    make_chart(df, city)
    print(report)
    print("\nSaved output/report.txt and output/study_report.png")
