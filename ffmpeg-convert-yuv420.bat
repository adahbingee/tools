:: yuv420p  limited range 16-239
:: yuvj420p full    range 0 -255
:: add -vsync 0 to drop duplicate frames
ffmpeg -i %1 -c:v rawvideo -pix_fmt yuvj420p -vsync 0 %~n1.yuv
