Zsteg is a wonderful tool to analyze .png files

***Challenge Statement***
Find the flag in this picture
format -> picoCTF{}

>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
binwalk --extract --dd=".*" pico_img.png

cd _pico_img.png.extracted

strings -n 9 37C.zlib


>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
flag = picoCTF{s0_m3ta_505fdd8b}
