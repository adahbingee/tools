setlocal enabledelayedexpansion
set left=%~nx1
set right=%~nx2
ffplay -window_title "%left% %right%" -loop 0 -f lavfi "movie=%left%:loop=0:discontinuity=1,scale=720:1280[v0];movie=%right%:loop=0:discontinuity=1,scale=720:1280[v1];[v0][v1]hstack"