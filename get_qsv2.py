import glob
import re

fileList = glob.glob('*.log')
sorted(fileList)

for filePath in fileList:
    qsv2 = -1.0
    strList = open(filePath, 'r').readlines()
    for line in strList:
        match = re.search(r'QSv2 = [+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?', line)
        if match is not None:
            qsv2 = float (match.group(1))
    print('{} = {}'.format(filePath, qsv2))