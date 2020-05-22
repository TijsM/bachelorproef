import csv
import numpy as np

data = []
with open('/Users/Tijs/Documents/projectenTijs/bp-data-analysis/python/data_alternatief.csv', 'rb') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        data.append(row)

# print(data)


exp, cont = data.condition.value_counts()
