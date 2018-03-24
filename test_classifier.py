

if __name__ == "__main__":
	file = "sampled_csv.csv"
	csvfile = open(file, 'r', encoding = "utf-8")
	reader = csv.reader(csvfile)

	fields = None
	norm_title_categories = {}

	count = 0 
	for row in reader:
		if len(row) == 0:
			continue
		print(row[0])