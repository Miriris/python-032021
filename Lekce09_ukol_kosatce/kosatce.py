import requests
import pandas
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix, precision_score, f1_score
import matplotlib.pyplot as plt

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/kosatce.csv")
open("kosatce.csv", "wb").write(r.content)

data = pandas.read_csv("kosatce.csv")
print(data.head())
print(data.columns)
print(data.shape)

X = data.drop(columns=["target"])

y = data["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=40)
print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

clf = KNeighborsClassifier()
clf.fit(X_train, y_train)
print(clf)

y_pred = clf.predict(X_test)

print(confusion_matrix(y_true=y_test, y_pred=y_pred))

ConfusionMatrixDisplay.from_estimator(clf, X_test, y_test,
                                      display_labels=clf.classes_,
                                      cmap=plt.cm.Blues)
plt.show()

print(precision_score(y_test, y_pred))

ks = [1, 3, 5, 7, 9]
for k in ks:
    clf = KNeighborsClassifier(n_neighbors=k)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print(k, f1_score(y_test, y_pred))

clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(f1_score(y_test, y_pred))

# ano, 85% dosáhne u KN = 3 nebo 5
