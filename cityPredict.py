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
from sklearn.linear_model import Ridge
from math import sqrt
from sklearn.metrics import make_scorer, mean_absolute_error
from tqdm import tqdm
import csv
import numpy as np

file = "sampled_csv.csv"
csvfile = open(file, 'r', encoding = "utf-8")
reader = csv.reader(csvfile)


count = 0 
for row in reader:
	count += 1
	if len(row) == 0:
		continue
	if count % 2 == 0:
		continue
	else:
		print(row)





clf = RandomForestClassifier()