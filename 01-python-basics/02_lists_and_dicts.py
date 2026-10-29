"""Day 1 - Lists and dictionaries: the two most used containers in Python."""

# A list is an ordered collection; indexes start at 0
topics = ["Python", "Math", "ML", "Deep Learning", "LLMs"]
print("First topic:", topics[0])
print("Last topic:", topics[-1])
topics.append("RAG")                     # add to the end
print("All topics:", topics, "| count:", len(topics))

# A dictionary maps keys -> values (like a mini database row)
student = {"name": "Nikitha", "day": 1, "skills": ["python"]}
student["skills"].append("numpy")       # change a value inside
student["day"] += 1
for key, value in student.items():
    print(f"{key}: {value}")

# List comprehension: build a new list in one line
lengths = [len(t) for t in topics]
print("Length of each topic name:", lengths)
