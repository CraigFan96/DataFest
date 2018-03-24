with open('sampled_csv.csv', 'r') as f:
    for count, line in enumerate(f, start=1):
        if count % 2 == 1:
            print(line)