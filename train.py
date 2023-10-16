import pandas as pd
import os
import glob
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import recall_score, precision_score
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# read in data
# get all csv files present in "numbers" dir
path = os.getcwd() 
train_files = glob.glob(path + "/data/numbers/*.csv")
test_files = glob.glob(path + "/data/test/*.csv")

# read in csv files, adding to "train" and "test" DFs
train = pd.DataFrame()
test = pd.DataFrame()
for f in train_files:
    train = pd.concat([train, pd.read_csv(f)], ignore_index=True)
for f in test_files:
    test = pd.concat([test, pd.read_csv(f)], ignore_index=True)
print(f"train size: {train.shape}\ntest size: {test.shape}")

# create feature/label objects
X_train = train.loc[:,train.columns != "label"]
y_train = train["label"]
X_test = test.loc[:,test.columns != "label"]
y_test = test["label"]

# scale the feature data for use in logistic regression
scaler = MinMaxScaler()
scaler.fit(X_train)
X_train_s = scaler.transform(X_train)
X_test_s = scaler.transform(X_test)

# train a classifier
clf = LogisticRegression(max_iter = 1000)
clf.fit(X_train_s, y_train)

# score the model
acc = clf.score(X_test_s, y_test)
y_pred = clf.predict(X_test_s)
precision = precision_score(y_test, y_pred, average="micro")
recall = recall_score(y_test, y_pred, average="micro")
print(precision, recall)

# output the metrics for the report markdown
with open("metrics.json", "w") as outfile:
    json.dump({"accuracy": acc, "precision": precision, "recall": recall}, outfile)

# output the confusion matrix
cm = ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.savefig("confusion_matrix.png")



