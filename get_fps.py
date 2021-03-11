import re
import sys
import glob
import subprocess

fileList = glob.glob('./*.mp4')
fileList = sorted(fileList)

for path in fileList:
    result = subprocess.run(['ffprobe', '-v', 'quiet', '-show_streams', '-select_streams', 'v:0', path], stdout=subprocess.PIPE)
    match  = re.search(r'avg_frame_rate=(\d+)\/(\d+)', result.stdout.decode('utf-8'))
    a      = match.group(1)
    b      = match.group(2)
    fps    = float(a)/float(b)
    print('{} {:0>6.2f}'.format(path, fps))