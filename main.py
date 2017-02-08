import csv

data = {}
with open('data.csv', 'rb') as csvfile:
	spamreader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		data[row['km']] = row['price']
print data
teta0 = 0
teta1 = 0
lr = 2
i = 1
while (i < len(data)):
	i = i + 1
