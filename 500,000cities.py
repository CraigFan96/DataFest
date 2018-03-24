import requests
import re 
import json
from time import sleep

def nonblank_lines(f):
	for l in f:
		line = l.strip()
		if line:
			yield line

lat = []
lng = []
lat_lng = []
if __name__ == "__main__":
	with open('cities.txt', 'r') as f_in:
		for line in nonblank_lines(f_in):
			line = line.split()
			currState = line[0]
			currCity = ''
			if(len(line[1:]) > 1):
				for x in line[1:]:
					currCity += x + ' '
			else:
				currCity = line[1:][0]
			#print(currState)
			#print(currCity)


			raw_url = "https://maps.googleapis.com/maps/api/geocode/json?address="
			city = currCity
			state = currState
			key = "AIzaSyAQ_eHaj0eOuppitnM_IdhfuhJm1EE8Exg"
            #"AIzaSyAt3K6rCaD_TyMWvixrPGi4sG1Ky-8deVU"
			strToFind = 'lat'
			strToFind1 = 'lng'

			r = requests.get(raw_url + "+" +city + ",+" + state + "&key=" + key)
			#print(str(r.json()).find(strToFind))
			#print(str(r.json()).find(strToFind1))
			index = str(r.json()).find(strToFind)
			index1 = str(r.json()).find(strToFind1)
			strlat = str(r.json())[index+6:index+10]
			strlng = str(r.json())[index+6:index+10]
            

			lat.append(strlat)
			lng.append(strlng)
            

lat_lng.append(lat)
lat_lng.append(lng)


def readcol(col):
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

    file = "sampled_csv_500000.csv"
    csvfile = open(file, 'r', encoding = "Latin-1")
    reader = csv.reader(csvfile)


    count = 0
    count1 = 0
    x = {}
    col_list = []
    for row in reader:
        count += 1
        if len(row) == 0:
            continue
        if count % 2 == 0:
            continue
        else:
            
            col_list.append(row[col])
            
        
          
            
    return col_list


nodegree = readcol(13)
hs = readcol(14)
highed = readcol(15)

loc = []
loc.append(lat_lng)
loc.append(nodegree)
loc.append(hs)
loc.append(highed)



"""
with open("outputlat_lng.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(lat_lng)
"""
 
"""

f = open('cities.txt', 'r')
count = 0
for i in range(1000):
	#print(count)
	count += 1
	if count % 2 == 1:
		continue
	else:
		current = f.readline()
		print(current)

for i in range(1000):
	for x in 
print(f.read())
"""