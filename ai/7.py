from sklearn.datasets import load_digits
from sklearn.ensemble import RandomForestClassifier

digits = load_digits()
X, y = digits.data, digits.target

model = RandomForestClassifier()
model.fit(X, y)

print(model.predict([X[0]]))