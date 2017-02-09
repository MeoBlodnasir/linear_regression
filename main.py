import csv
import os 
import sys

def predict(mileage):
    teta0 = 0.0
    teta1 = 0.0
    with open('values.csv', 'rb') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            teta0 = float(row['teta0'])
            teta1 = float(row['teta1'])

    ret = teta0 + teta1 * float(mileage)
    return ret


data = []
with open('data.csv', 'rb') as csvfile:
	spamreader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
            data.append((float(row['km']), float(row['price'])))


minimum = min(data, key=lambda item:item[0])[0]
maximum = max(data, key=lambda item:item[0])[0]
norm_data = []
for mil, price in data:
    norm_data.append((((mil - minimum)/(maximum - minimum)), price))


lr = 1
i = 0
while (i < 10000):
    tmpteta0 = 0.0
    tmpteta1 = 0.0
    for mil, price in norm_data:
        tmpteta0 += float(predict(mil)) - float(price)
    tmpteta0 =  lr * (1.0 / len(norm_data)) * tmpteta0


    for mil, price in norm_data:
        tmpteta1 += (float(predict(mil)) - float(price)) * float(mil)
    tmpteta1 =  lr * (1.0 / len(norm_data)) * tmpteta1


    
    with open('values.csv', 'rb') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            teta0 = float(row['teta0'])
            teta1 = float(row['teta1'])


    with open('values.csv', 'wb') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(['teta0', 'teta1'])
            writer.writerow([teta0 - tmpteta0, teta1 - tmpteta1])
    i = i + 1


with open('values.csv', 'rb') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        teta0 = float(row['teta0'])
        teta1 = float(row['teta1']) 
        print teta0, teta1 / (maximum - minimum)
