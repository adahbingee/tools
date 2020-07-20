:: adb exec-out screencap is a safe way to generate screenshot in bitmap format.
:: You can use pipe read that raw data. The first 4 bytes mark the little-endian integer for width. The next 4 bytes is the height. The next 4 bytes indicate the image format. Following bytes is raw data for the images like RGBA8888.
:: Note: Do not use raw data from adb shell screencap. The shell will insert some line breaks so data could broke.
:: Ref: https://github.com/aosp-mirror/platform_system_core/blob/46f281edf5e78a51c5c1765460cddcf805e88d48/adb/daemon/framebuffer_service.cpp#L88-L91

adb exec-out screencap -p