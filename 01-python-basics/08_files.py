"""Stage 1 - Reading and writing files."""
from pathlib import Path

out = Path(__file__).parent / "output"
out.mkdir(exist_ok=True)
notes_file = out / "my_notes.txt"

# 'w' = write (overwrites). 'with' closes the file automatically.
with open(notes_file, "w") as f:
    f.write("Day 1: Python basics\n")
    f.write("Day 2: Loops and files\n")

with open(notes_file, "a") as f:     # 'a' = append to the end
    f.write("Day 3: NumPy and pandas\n")

with open(notes_file) as f:          # default mode 'r' = read
    for line_no, line in enumerate(f, start=1):
        print(line_no, line.strip())
