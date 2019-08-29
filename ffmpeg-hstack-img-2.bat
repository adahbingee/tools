set left="G:\workspace\clip25_540x960_20_2100\%%04d.jpg"
set rigt="G:\workspace\run-pool\%%04d.png"

ffmpeg -i %left% -i %rigt% -filter_complex hstack out.mp4