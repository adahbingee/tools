set left="./0003_720x1280.yuv"
set rigt="./0003_720x1280_out.yuv"
set size="720x1280"
ffmpeg ^
-f rawvideo -pix_fmt yuvj420p -s:v %size% -i %left% ^
-f rawvideo -pix_fmt yuvj420p -s:v %size% -i %rigt% ^
-filter_complex hstack -c:v libx264 -qp 18 out.mp4