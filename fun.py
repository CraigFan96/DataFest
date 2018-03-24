import requests
import json
from time import sleep

def nonblank_lines(f):
	for l in f:
		line = l.strip()
		if line:
			yield line


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
			print(currState)
			print(currCity)


			raw_url = "https://maps.googleapis.com/maps/api/geocode/json?address="
			city = currCity
			state = currState
			key = "AIzaSyAt3K6rCaD_TyMWvixrPGi4sG1Ky-8deVU"
			strToFind = 'lat'

			r = requests.get(raw_url + "+" +city + ",+" + state + "&" + key)
			print(str(r.json()).find(strToFind))
			try:
				sleep(.5)
				#lat_lng = r.json()["results"][0]["geometry"]["location"]
			except:
				print('getting here')
				print(r.json())
			lat = lat_lng["lat"]
			lng = lat_lng["lng"]

		print(lat, lng)

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