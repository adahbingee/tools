#!/bin/bash

# bash yuv2mp4.sh test_800x720.yuv 800 720
ffmpeg -f rawvideo -pix_fmt yuvj420p -s:v $2x$3 -i $1 -c:v libx265 -crf 26 "${1%.*}.mp4"


