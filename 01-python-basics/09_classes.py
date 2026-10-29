"""Stage 1 - Classes and objects: bundle data + behavior together.
(PyTorch models later are written as classes, so this matters!)"""

class Student:
    def __init__(self, name, scores):   # runs when you create an object
        self.name = name                # attributes = data the object holds
        self.scores = scores

    def average(self):                  # methods = functions belonging to the object
        return sum(self.scores) / len(self.scores)

    def add_score(self, score):
        self.scores.append(score)

    def __repr__(self):                 # how the object prints
        return f"Student({self.name}, avg={self.average():.1f})"

nikitha = Student("Nikitha", [70, 80])
nikitha.add_score(95)
print(nikitha)
print("Scores:", nikitha.scores)
