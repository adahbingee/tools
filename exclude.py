import csv
import sys

filePath = sys.argv[1]

col0 = []
col1 = []

with open(filePath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if len(row[0].split()) != 0:
            col0.append( row[0] )
        if len(row[1].split()) != 0:
            col1.append( row[1] )
        # print('Col 0: {} Col 1: {}'.format(row[0], row[1]))

print('num0 {} num1 {}'.format(len(col0), len(col1)))

# find large column
if len(col0) > len(col1):
    small = col1
    large = col0
else:
    small = col0
    large = col1

# find exclude item
exclude = []
for itemL in large:
    hasPair = False
    for itemS in small:
        if itemL == itemS:
            hasPair = True
            break
    if hasPair == False:
        exclude.append( itemL )

print('excludeNum {}'.format(len(exclude)))

# print exclude item
for item in exclude:
    print(item)