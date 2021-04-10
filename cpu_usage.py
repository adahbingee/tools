import psutil


while True:
    usage = psutil.cpu_percent()
    if usage == 0:
        continue
    print(usage)