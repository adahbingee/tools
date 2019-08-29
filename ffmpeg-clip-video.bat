:: https://superuser.com/questions/138331/using-ffmpeg-to-cut-up-video

:: input start time
set inptFile=inpt.mp4
set ouptFile=oupt.mp4
set strTime=00:00:00
set duration=00:00:26

ffmpeg -ss %strTime% -i %inptFile% -c copy -t %duration% %ouptFile%