import re
import sys
import time
import subprocess
import matplotlib.pyplot as plt

pid       = sys.argv[1]
time_list = []
mem_list  = []
ts        = 0

cmd = 'nvidia-smi | grep {}'.format(pid)

while(True):
    time.sleep(3)

    out   = subprocess.check_output(cmd, shell=True)
    match = re.search(r'(\d+)MiB', out.decode('UTF-8'))

    if match == None:
        break

    mem   = int(match.group(1))
    mem_list.append(mem)

    time_list.append(ts)
    ts += 3
    print(mem_list)

plt.title('Transcoder GPU Memory(VSS)')
plt.xlabel('Time(s)')
plt.ylabel('VSS(MB)')
color_list = ['g', 'b', 'r', 'y', 'p', 'v']
plt.plot(time_list, mem_list, color='g', linewidth=1, alpha=1)
plt.savefig('gpu_memory_test_result.png')
