:: skip_frame
:: nointra  Discard all frames except I frames.
:: nokey    Discard all frames excepts keyframes.
ffmpeg -skip_frame nointra -i %1 -vsync 0 %%04d.png