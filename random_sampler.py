from tqdm import tqdm
import numpy as np
import csv



def sample(n):
	file = "..\\data.csv"
	f = open(file, 'r', encoding = "utf-8")
	#Max size = n
	reservior = []

	fields = None
	first = True

	for line in tqdm(f):
		if first:
			fields = line
			first = False

		if len(reservior) < n:
			# reservior.append(line.encode("utf-8"))
			encoded = [x.encode("utf-8") for x in line.split(",")]
			# reservior.append(encoded)
			reservior.append(line.split(","))

		else:
			rand = np.random.randint(0, n)
			if rand < n:
				encoded = [x.encode("utf-8") for x in line.split(",")]
				# reservior[rand] = encoded
				reservior[rand] = line.split(",")

				# reservior[rand] = line.encode("utf-8")
		
	fields = fields.split(",")
	# f = open("sampled.txt", "wb")
	# for i in range(len(reservior)):
	# 	f.write(reservior[i])
	# print(fields)
	fields[len(fields) - 1] = "jobHash"
	print(fields)
	with open("sampled_csv.csv", "w", encoding = "utf-8") as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=fields)
		writer.writeheader()
		for i in range(len(reservior)):
			build_dict = {}
			for j in range(len(fields)):
				build_dict[fields[j]] = str(reservior[i][j])
			writer.writerow(build_dict)
if __name__ == "__main__":
	n = 500000
	sample(n)		