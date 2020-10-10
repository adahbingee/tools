set INPUTVIDEO=hdr_clip.mp4
set OUTPUTVIDEO=hdr_clip_r.mp4
ffmpeg -i %INPUTVIDEO% -metadata:s:v rotate="-90" -codec copy %OUTPUTVIDEO%