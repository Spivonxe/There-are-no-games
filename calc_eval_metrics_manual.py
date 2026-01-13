import pandas as pd
import numpy as np
import math

# written with chatgpt

# Load data
df = pd.read_csv("manual_query_export.csv")

grade_cols = [f"game {i} grade" for i in range(1, 6)]

# -----------------------------
# Helper functions
# -----------------------------

def binarize(grades):
    """Convert grades: 1,2 -> 1 ; 0 -> 0"""
    return [1 if g > 0 else 0 for g in grades]

def dcg(grades):
    return sum(
        (2**rel - 1) / math.log2(i + 2)
        for i, rel in enumerate(grades)
    )

def ndcg(grades):
    ideal = sorted(grades, reverse=True)
    idcg = dcg(ideal)
    return dcg(grades) / idcg if idcg > 0 else 0.0

def average_precision(binary_grades):
    score = 0.0
    hits = 0
    for i, rel in enumerate(binary_grades):
        if rel == 1:
            hits += 1
            score += hits / (i + 1)
    return score / hits if hits > 0 else 0.0

def reciprocal_rank(binary_grades):
    for i, rel in enumerate(binary_grades):
        if rel == 1:
            return 1 / (i + 1)
    return 0.0

# -----------------------------
# Metric computation
# -----------------------------

precisions = []
failures = []
ndcgs = []
maps = []
mrrs = []

for _, row in df.iterrows():
    grades = [row[c] for c in grade_cols]
    binary = binarize(grades)

    # Precision@5
    precisions.append(sum(binary) / 5)

    # Failure: at least one 0-grade result
    failures.append(1 if 0 in grades else 0)

    # Ranking metrics
    ndcgs.append(ndcg(grades))
    maps.append(average_precision(binary))
    mrrs.append(reciprocal_rank(binary))

# -----------------------------
# Print results
# -----------------------------

print(f"Precision@5: {np.mean(precisions):.3f}")
print(f"Failure rate: {np.mean(failures):.3f}")
print(f"nDCG@5: {np.mean(ndcgs):.3f}")
print(f"MAP@5: {np.mean(maps):.3f}")
print(f"MRR: {np.mean(mrrs):.3f}")
