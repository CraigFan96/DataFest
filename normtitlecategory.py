from tqdm import tqdm 
import csv
import numpy as np

def match_categories()

if __name__ == "__main__":
	file = "sampled_csv.csv"
	csvfile = open(file, 'r', encoding = "utf-8")
	reader = csv.reader(csvfile)

	fields = None
	norm_title_categories = {}

	count = 0 
	for row in reader:
		if count == 0:
			fields = row
			count += 1
			continue
		if len(row) == 0:
			continue

		count += 1
		# norm_title_categories.add(row[23])
		if row[23] not in norm_title_categories:
			norm_title_categories[row[23]] = len(norm_title_categories) + 1

	# print(norm_title_categories)
	for k,v in norm_title_categories.items():
		print(k,v)
	with open("normtitlecategory_number.txt", "w", encoding = "utf-8") as file:
		for k,v in norm_title_categories.items():
			s = k + " " + str(v) + "\n"
			file.write(s)