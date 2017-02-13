import csv
import os 
import sys
import statistics


def predict(mileage, teta0, teta1):
    ret = teta0 + teta1 * float(mileage)
    return ret


data = []
with open('data.csv', 'r') as csvfile:
	spamreader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
            data.append((float(row['km']), float(row['price'])))


minimum = min(data, key=lambda item:item[0])[0]
maximum = max(data, key=lambda item:item[0])[0]

d = []
for mil, price in data:
    d.append((float((mil - minimum)/(maximum - minimum)), price))


print (d)

lr = 0.1
t0 = 0.0
t1 = 0.0
k = 0
while (k < 10000):
    grad0 = 1.0/float(len(d)) * sum([(t0 + t1*d[i][0] - d[i][1]) for i in range(len(d))]) 
    grad1 = 1.0/float(len(d)) * sum([(t0 + t1*d[i][0] - d[i][1])*d[i][0] for i in range(len(d))])

    temp0 = t0 - lr * grad0
    temp1 = t1 - lr * grad1

    t0 = temp0
    t1 = temp1
    k += 1


print (t0, (t1 - minimum) / (maximum - minimum))

with open('values.csv', 'w') as csvfile:
	writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	writer.writerow(['teta0', 'teta1', 'min', 'max'])
	writer.writerow([t0, t1, minimum, maximum])


x1 = minimum
y1 = predict((minimum - minimum) / (maximum - minimum), t0, t1)
x2 = maximum
y2 = predict((maximum - minimum) / (maximum - minimum), t0, t1)



import sys, csv
from plotly.offline import plot
import plotly.graph_objs as go

def readDatasFromCsv(filename):
    datas = []

    try:
        with open(filename, 'r') as datafile:
            reader = csv.reader(
                datafile,
                delimiter=',',
                quotechar='|'
            )
            junk = next(reader)

            for km, price in reader:
                datas.append((float(km), float(price)))
    except:
        sys.exit(1)
    
    return datas

datas = readDatasFromCsv('data.csv')

xList = [x for x, y in datas]
yList = [y for x, y in datas]

points = [go.Scatter(x = xList, y = yList, mode = 'markers')]
#points = [go.Scatter(x, y, mode = 'markers') for x, y in datas]

layout = {
    'shapes': [
    {
        'type': 'line',
        'x0': x1,
        'y0': y1,
        'x1': x2,
        'y1': y2,
        'line': {
            'color': 'rgb(0, 128, 0)',
            'width': 3,
        },
    }]
}

fig = {
    'data': points,
    'layout': layout
}

plot(fig, filename='graph.html')
