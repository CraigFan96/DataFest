import numpy as np
import matplotlib.pyplot as plt
import sklearn
import csv
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from numpy import genfromtxt
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn import linear_model
from sklearn.model_selection import GridSearchCV
from sklearn import svm
from sklearn import tree
from sklearn.linear_model import Ridge
from sklearn.naive_bayes import GaussianNB
from math import sqrt
from sklearn.metrics import make_scorer, mean_absolute_error
from tqdm import tqdm
import csv
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

# file = "temp.csv"
file = "labelscomplete_firstrowdeleted.csv"

csvfile = open(file, 'r', encoding = "utf-8")
reader = csv.reader(csvfile)

cutOff = 425000

trainData = []
labels = []
count = 0
for row in reader:
	count += 1
	if len(row) == 0:
		continue
	if count == cutOff:
		break
	else:
		trainData.append(row[:-1])
		labels.append(row[-1])


# clf = RandomForestClassifier()
clf = MLPClassifier(solver='sgd', hidden_layer_sizes=(5, 2), random_state=1)
# clf = svm.SVC(verbose = True)
# clf = GaussianNB()
# clf = tree.DecisionTreeClassifier(max_depth=300)
#clf.fit(trainData,labels)


file1 = "labelscomplete_firstrowdeleted.csv"
csvfile1 = open(file1, 'r', encoding = "utf-8")
reader1 = csv.reader(csvfile1)
newCount = 0
testData = []
answers = []
for row in reader1:
	newCount += 1

	if len(row) == 0:
		continue
	if newCount >= cutOff:
		testData.append(row[:-1])
		answers.append(row[-1])

#print(testData)
arrayWithPredictions = []
#for i in clf.predict(testData):
#	arrayWithPredictions.append(i)
#print(len(arrayWithPredictions))
#print(len(answers))
#print(clf.score(testData, answers))

X_train, X_test, y_train, y_test = train_test_split(trainData, labels, test_size = 0.8, random_state = 0)
#print(np.asarray(X_train))
#print(np.asarray(X_train)[0].shape)
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))

"""
Results:

Random Forest Classification:
With n = 10,000 and cross-validation of 85%/15% split, we received an accuracy
of about 5%
With n = 500,000 and cross-validation of 85%/15% split, we received an accuracy
of about 10%

SVM

"""