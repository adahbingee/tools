import sys

fileName = sys.argv[1]
fileStr  = open(fileName, 'r')
lines    = fileStr.readlines()

lists = []
for line in lines:
    clip = line.strip().split(' => ')
    if len(clip) > 1:
        lists.append( [clip[0], clip[1]] )

for line in lists:
    print('{}{}'.format(line[0].ljust(50), line[1]))