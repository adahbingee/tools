setlocal enabledelayedexpansion
set lft=%~nx1
set mid=%~nx2
set rit=%~nx3
set cmd_lft=movie=%lft%:loop=0:discontinuity=1,scale=720:1280,drawtext=text='%lft%':fontcolor=white:box=1:boxcolor=black@0.5[v0]
set cmd_mid=movie=%mid%:loop=0:discontinuity=1,scale=720:1280,drawtext=text='%mid%':fontcolor=white:box=1:boxcolor=black@0.5[v1]
set cmd_rit=movie=%rit%:loop=0:discontinuity=1,scale=720:1280,drawtext=text='%rit%':fontcolor=white:box=1:boxcolor=black@0.5[v2]
ffplay -window_title "%lft% %mid% %rit%" -loop 0 -f lavfi "%cmd_lft%;%cmd_mid%;%cmd_rit%;[v0][v1][v2]hstack=3"
pause