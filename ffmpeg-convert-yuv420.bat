:: yuv420p  limited range 16-239
:: yuvj420p full    range 0 -255
ffmpeg -i %1 -c:v rawvideo -pix_fmt yuvj420p %~n1.yuv
