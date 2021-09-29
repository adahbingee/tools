:: https://trac.ffmpeg.org/wiki/Capture/Desktop
::ffmpeg -f gdigrab -framerate 30 -i desktop -c:v h264_nvenc -qp 0 output.mkv
ffmpeg -f gdigrab -framerate 30 -i desktop -pix_fmt yuv420p -c:v libx265 output.mp4