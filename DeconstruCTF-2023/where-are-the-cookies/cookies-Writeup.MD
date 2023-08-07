# where-are-the-cookies

## DESCRIPTION
> Tom is feeling especially snacky during the CTF, can you find where the cookies are?
Note: This challenge works best on Chrome  
**FLAG FORMAT**:
dsc{[a-zA-Z0-9_]+}

## Solution
* Checking cookies gives us nothing
* Visiting `/robots.txt` gives us `/cookiesaretotallynothere`
* Visting the page and checking the cookies we see a cookies named `caniseethecookie` and value `bm8==`
* Using [CyberChef](https://gchq.github.io/CyberChef/) and Base64 Decoding the value gives `no`
* base64 encode `yes` gives us `eWVz` and put it as the cookie value.
* Refresh the page and we get the flag
* Flag:  
`dsc{1_f0unD_Th3_c0oK135}` 
