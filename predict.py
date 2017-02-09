import csv

teta0 = 0
teta1 = 0
with open('values.csv', 'rb') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        teta0 = int(row['teta0'])
        teta1 = int(row['teta1'])

prompt = '> What is the car\'s mileage ?\n> '
mileage = raw_input(prompt)
ret = teta0 + teta1 * int(mileage)
print ret
