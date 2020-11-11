set inpt=video.mp4
set oupt=log.txt
ffmpeg -i %inpt% -dump -map 0:v -f null - >%oupt% 2>&1