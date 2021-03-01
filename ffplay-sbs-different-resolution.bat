setlocal enabledelayedexpansion
:: normalize size
set szX=720
set szY=1280
:: resample algorithm
set sws=lanczos
:: inputs
set lft=%~nx1
set rit=%~nx2
set cmd_lft=movie=%lft%:loop=0:discontinuity=1,scale=%szX%:%szY%:sws_flags=%sws%,drawtext=text='%lft%':fontcolor=white:box=1:boxcolor=black@0.5[v0]
set cmd_rit=movie=%rit%:loop=0:discontinuity=1,scale=%szX%:%szY%:sws_flags=%sws%,drawtext=text='%rit%':fontcolor=white:box=1:boxcolor=black@0.5[v1]
ffplay -window_title "%lft% %rit%" -loop 0 -f lavfi "%cmd_lft%;%cmd_rit%;[v0][v1]hstack=2"
