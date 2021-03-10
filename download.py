import csv
import requests
import os
from urllib.parse import urlparse

fileName = 'ab_anchor.txt'

i = 0
with open(fileName, newline='') as csvFile:
    rows = csv.reader(csvFile)
    for row in rows:
        url = row[0]
        #qs = row[1]
        #country = row[2]
        videoFileName = os.path.basename( urlparse(url).path )
        extension     = os.path.splitext( videoFileName )[1]
        #print( extension )
        #print(url)
        #print(videoFileName)
        #print(qs)
        #print(country)
        #newName = '%03d_%s_%s.mp4'%(i, qs, country)
        #print(newName)
        #os.rename(videoFileName, newName)
        #i = i + 1
        if extension.lower() == '.mp4':
            videoFile = requests.get(url)
            outFileName = '{}_{}'.format(str(i).zfill(6), )
            open(outFileName, 'wb').write(videoFile.content)
