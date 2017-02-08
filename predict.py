import csv

teta0 = 3
teta1 = 3
with open('values.csv', 'rb') as csvfile:
	reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
	for row in reader:
		teta0 = row['teta0']
		teta1 = row['teta1']

print teta0, teta1
