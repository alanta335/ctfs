Binwalk 
Binwalk is a tool for searching a given binary image for embedded files and 
executable code. Specifically, it is designed for identifying files and code embedded inside of firmware images.

Figure out how to extract data using Binwalk

***Challenge Statement***
Extract Me


>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>>>>>>binwalk --extract hell.jpg

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
0             0x0             JPEG image data, JFIF standard 1.02
30            0x1E            TIFF image data, big-endian, offset of first image directory: 8
265845        0x40E75         Zip archive data, at least v2.0 to extract, uncompressed size: 69, name: hello_there.txt
266099        0x40F73         End of Zip archive, footer length: 22


>>>ls
40E75.zip  hello_there.txt

>>>strings hello_there.txt
Thank you for extracting me, you are the best!
THM{y0u_w4lk_m3_0u7}



>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

flag = THM{y0u_w4lk_m3_0u7}
