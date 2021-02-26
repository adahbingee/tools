setlocal enabledelayedexpansion
set lft=%~nx1
set mid=%~nx2
set rit=%~nx3
ffplay -window_title "%lft% %mid% %rit%" -loop 0 -f lavfi "movie=%lft%:loop=0:discontinuity=1,scale=720:1280[v0];movie=%mid%:loop=0:discontinuity=1,scale=720:1280[v1];movie=%rit%:loop=0:discontinuity=1,scale=720:1280[v2];[v0][v1][v2]hstack=3"
