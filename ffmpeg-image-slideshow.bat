set startNum=0
set durationIn=5
set fpsOut=25
ffmpeg -start_number %startNum% -framerate 1/%durationIn% -i %%04d.png -c:v libx264 -vf fps=%fpsOut% -pix_fmt yuv420p -qp 18 out.mp4