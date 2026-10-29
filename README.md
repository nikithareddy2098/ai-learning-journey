# ai-learning-journey

This is where I'm learning AI/ML from scratch. Each folder is one stage, and every script runs on its own. I write short notes as I go, mostly so future me remembers what was confusing.

## Where I'm at

| Stage | Status |
|---|---|
| [01 Python & data basics](01-python-basics) | done |
| [02 Math for ML](02-math-for-ml) | done |
| [03 Classic ML (scikit-learn)](03-classic-ml) | in progress |
| 04 Deep learning (PyTorch) | next |
| 05 LLMs | later |
| 06 RAG | later |
| 07 AI agents | later |
| 08 Fine-tuning & deployment | later |

## Small projects so far

**Study data analysis** ([code](01-python-basics/14_mini_project_study_analysis.py)): I made a messy little dataset of students (study hours, sleep, scores), cleaned it, and checked what lines up with higher scores. Study hours won by a lot (correlation 0.94). Sleep barely mattered in this data, which surprised me, but it's only 9 rows so I wouldn't trust it much.

![study report](01-python-basics/output/study_report.png)

**Gradient descent by hand** ([code](02-math-for-ml/04_gradient_descent.py)): I fit a line using only NumPy. It got y = 3.07x + 6.80 when the real line was 3x + 7.

**Tumor classifier** ([code](03-classic-ml/04_project_breast_cancer_classifier.py)): I used the breast cancer dataset that comes with scikit-learn. Logistic regression got 98.2% on the test set and caught 97.6% of the malignant cases. Random forest did a bit worse, which I didn't expect.

![classifier report](03-classic-ml/output/classifier_report.png)

## Things I want to build later
- chat with my own PDFs (RAG)
- resume vs job description matcher
- a small agent that researches a topic and writes a summary
- a text classifier I fine-tune myself
- an image classifier with a simple web page

## Running it
```
pip install -r requirements.txt
python 03-classic-ml/04_project_breast_cancer_classifier.py
```

Daily notes are in [PROGRESS.md](PROGRESS.md).
