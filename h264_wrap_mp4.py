import os
import re
import sys
import glob
import subprocess

fileList = glob.glob('./*.h264')
fileList = sorted(fileList)

count = 0
for path in fileList:
    match = re.search(r'.\Dump_sid_(\d+)_uid_(\d+)_time_(\d+)_(\d+)_(\d+)_(\d+)_(\d+)_(\d+).h264', path)
    ouptName = '{:03d}_sid_{}_uid_{}.mp4'.format(count, match.group(1), match.group(2))
    cmd = 'ffmpeg -i {} -c:v copy -f mp4 {}'.format(path, ouptName)
    os.system(cmd)
    print(cmd)
    count = count + 1