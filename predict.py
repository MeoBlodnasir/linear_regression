import csv

teta0 = 0
teta1 = 0
minimum = 0
maximum = 0
with open('values.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        teta0 = float(row['teta0'])
        teta1 = float(row['teta1'])
        maximum = float(row['max'])
        minimum = float(row['min'])

prompt = '> What is the car\'s mileage ?\n> '
mileage = float(input(prompt))
ret = teta0 + teta1 * float((mileage - minimum) / (maximum - minimum))
print (ret)
