#BY SHU

from tqdm import tqdm 
import csv
import numpy as np
import chardet

"""
Assumes that sampled_csv.csv is in the current directory, reads it and parses
the normtitlecategory column of the csv to create unique integer descriptors
for each of them.

Returns an dictionary with the labels

params: write(boolean)
	Parameter to specify whether it is wanted to write the descriptors to a txt
	file
"""
def match_categories(write = True):
	file = "sampled_csv.csv"
	with open(file, encoding="Latin-1") as csvfile:
		reader = csv.reader(csvfile)

		fields = None
		norm_title_categories = {}

		"""
		Reads through the CSV file row by row
		"""
		count = 0 
		for row in reader:
			"""
			Skips unnecessary rows
			"""
			if count == 0:
				fields = row
				count += 1
				continue
			if len(row) == 0:
				continue

			count += 1

			"""
			Assigns each unique normtitlecategory to an inteer
			"""
			if row[23] not in norm_title_categories:
				norm_title_categories[row[23]] = len(norm_title_categories) + 1

		if write:
			with open("normtitlecategory_number.txt", "w", encoding = "utf-8") as file:
				for k,v in norm_title_categories.items():
					s = k + " " + str(v) + "\n"
					file.write(s)

def add_to_file(mapping):
	"""

	"""
	def _is_empty(arr):
		count = 0 
		for x in arr:
			if len(x) == 0:
				count += 1
		return count == len(arr)

	with open("outputlabels.csv", "r", encoding = "utf-8") as csvfile:
		reader = csv.reader(csvfile)
		writer = csv.writer(csvfile)
		row = next(reader)
		row.append("normtitlecategory_labels")
		every = []
		every.append(row)
		for row in reader:
			if _is_empty(row):
				continue
			row.append()
			#UNFINISHED

if __name__ == "__main__":
	mapping = match_categories(False)
	add_to_file(mapping)