::
::
ffmpeg -i 2Aurnd_30fps.mp4 -i ramp.png ^
-filter_complex "[0:v][1:v] overlay=25:700:enable='between(t,0,20)'" ^
-pix_fmt yuv420p -c:a copy ^
-c:v libx264 -qp 18 ^
output.mp4