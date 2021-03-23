import re
import sys
import glob
import subprocess

# ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 input.mp4

fileList = glob.glob('./*.mp4')
fileList = sorted(fileList)

for path in fileList:
    result = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=width,height', '-of', 'csv=s=x:p=0', path], stdout=subprocess.PIPE)
    match  = re.search(r'(\d+)x(\d+)', result.stdout.decode('utf-8'))
    sizeX  = match.group(1)
    sizeY  = match.group(2)
    print('{} {}x{}'.format(path, sizeX, sizeY))