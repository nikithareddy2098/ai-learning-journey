"""Stage 1 - String handling: text is everywhere in AI (LLMs work on text!)."""
text = "  Machine Learning is FUN and machine learning is useful  "

clean = text.strip().lower()          # remove outer spaces, lowercase
print("Clean:", clean)
words = clean.split()                 # split into a list of words
print("Words:", words, "| count:", len(words))
print("Times 'learning' appears:", clean.count("learning"))
print("Replace:", clean.replace("fun", "awesome"))
print("Joined with dashes:", "-".join(words[:3]))
print("Starts with 'machine'?", clean.startswith("machine"))
print("First 7 chars (slicing):", clean[:7])
