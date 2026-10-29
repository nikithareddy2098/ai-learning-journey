# 01 · Python & Data Basics ✅

| Script | Concept |
|---|---|
| `01_variables_and_types.py` | Variables, `str`/`int`/`float`/`bool`, f-strings, casting |
| `02_lists_and_dicts.py` | Lists, indexing, dictionaries, list comprehensions |
| `03_functions.py` | Defining functions, return values, default parameters |
| `04_numpy_intro.py` | NumPy arrays, vectorized math, boolean filtering, correlation |
| `05_pandas_intro.py` | Loading a CSV, `describe()`, new columns, filtering, `groupby` |
| `06_loops_and_conditionals.py` | `for`, `while`, `if/elif/else`, `enumerate`, `break` |
| `07_strings.py` | `strip`, `lower`, `split`, `replace`, `join`, slicing |
| `08_files.py` | Writing, appending, and reading text files with `with open(...)` |
| `09_classes.py` | Classes, `__init__`, attributes, methods, `__repr__` |
| `10_error_handling.py` | `try/except/finally`, `raise` |
| `11_numpy_more.py` | 2D arrays, `shape`, row/column indexing, `axis`, matrix multiply |
| `12_pandas_more.py` | Missing values (`isna`, `fillna`, `dropna`), multi-filters, `groupby().agg` |
| `13_matplotlib_chart.py` | Scatter plot saved to PNG |
| `14_mini_project_study_analysis.py` | 🏁 **Mini-project:** clean data → report + 2-panel chart |

## 🏁 Mini-project result
![Study report](output/study_report.png)

## 📝 Notes
- Python decides a variable's type automatically. Use `type(x)` to check it.
- Lists keep order (`topics[0]`); dicts look things up by key (`student["name"]`).
- Loops repeat work; `if/elif/else` makes decisions.
- Strings matter a lot in AI because LLMs work on text. Cleaning text (`strip`, `lower`) is the first step.
- `with open(...)` closes files for you automatically.
- Classes bundle data + functions. PyTorch models are written as classes.
- `try/except` lets a program handle bad input instead of crashing.
- NumPy `axis=0` = down the columns, `axis=1` = across the rows. `@` is matrix multiplication, the core math of neural networks.
- Real data has gaps. Always check `df.isna().sum()` before analyzing.
- A chart often shows a pattern faster than a table does.

Run any script: `python 14_mini_project_study_analysis.py`
