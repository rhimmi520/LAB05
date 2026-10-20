from sklearn.model_selection import KFold, cross_val_score
from sklearn.linear_model import LogisticRegression
import numpy as np

X = np.array([[1], [2], [3], [4], [5], [6]])
y = [0, 0, 0, 1, 1, 1]

model = LogisticRegression()
kfold = KFold(n_splits=3, shuffle=True, random_state=1)

scores = cross_val_score(model, X, y, cv=kfold)

print("Scores:", scores)
print("Average Accuracy:", scores.mean())
