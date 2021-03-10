import subprocess
import sys
import re

path   = sys.argv[1]
result = subprocess.run(['ffprobe', '-v', 'quiet', '-show_streams', '-select_streams', 'v:0', path], stdout=subprocess.PIPE)
match  = re.search(r'avg_frame_rate=(\d+)\/(\d+)', result.stdout.decode('utf-8'))
a      = match.group(1)
b      = match.group(2)
fps    = round(float(a)/float(b), 2)
print('{}'.format(fps))