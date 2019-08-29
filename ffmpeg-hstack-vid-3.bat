set left="./0003_720x1280.yuv"
set cent="./0003_720x1280_out.yuv"
set rigt="./0003_720x1280_out2.yuv"
set size="720x1280"
ffmpeg ^
-f rawvideo -pix_fmt yuvj420p -s:v %size% -i %left% ^
-f rawvideo -pix_fmt yuvj420p -s:v %size% -i %cent% ^
-f rawvideo -pix_fmt yuvj420p -s:v %size% -i %rigt% ^
-filter_complex "[0:v:0][1:v:0][2:v:0]hstack=inputs=3" ^
-c:v libx264 -preset veryslow -qp 18 triple.mp4