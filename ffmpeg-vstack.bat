ffmpeg -i %1 -i %1 -i %1 -filter_complex "vstack=inputs=3,scale=-3:720" -c:v libx264 -tune film -crf 16 -b:a 256k triple.mp4
pause