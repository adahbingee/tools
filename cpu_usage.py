import psutil


while True:
    usage = psutil.cpu_percent()
    print(usage)