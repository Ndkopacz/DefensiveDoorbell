# Getting access to the pi

## VPN Access



## SSH Credentials
Host adam
    HostName 192.168.1.92
    User adampi
    Port 9092
    Password SpicyEye5!

## Interesting Commands
libcamera-still -o image.jpg
-o, --output [filename]: Specify the output file name (e.g., -o image.jpg).
-t, --timeout [ms]: Time (in milliseconds) to wait before taking the picture (e.g., -t 5000 for a 5-second delay). Default is 5 seconds (5000 ms).
-n, --nopreview: Disable the preview window.
-h, --help: Show help information about the options.
--width [pixels]: Set the width of the image (e.g., --width 1920).
--height [pixels]: Set the height of the image (e.g., --height 1080).
-q, --quality [0-100]: Set the image quality (JPEG) from 0 to 100. Default is 93.
--rotation [0, 90, 180, 270]: Rotate the image by the specified degrees.
--hflip: Flip the image horizontally.
--vflip: Flip the image vertically.

## Connecting to the pi cam

I'll be honest. No idea. 

It's on cam/disp0. You will need to stream the video through a webserver to make sure it works (that way you can actually see the data stream)