set left=left.mp4
set right=right.mp4
ffplay -loop 0 -f lavfi "movie=%left%:loop=0:discontinuity=1,scale=iw/2:ih[v0];movie=%right%:loop=0:discontinuity=1,scale=iw/2:ih[v1];[v0][v1]hstack"