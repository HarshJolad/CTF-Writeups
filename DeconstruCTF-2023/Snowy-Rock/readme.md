# Snowy Rock
## DESCRIPTION
> am loves puzzles and his dad working in alaska sent a message hidden within for him to uncover.
Can you decode it?  
Author: Rakhul  
**FLAG FORMAT**:
dsc{[a-zA-Z0-9_]+}

## Solution
* Running `strings` on the jpg provided we see there is a `snowyrock.txt` embedded in it
* We can extract it using   
`binwalk -e snowy_rock_fi.jpg`
* We get a encrypted zip file
* We can crack it using `John the Ripper` and using the `rockyou` wordlist  
`zip2john 3CA15.zip > zip.hash`  
`john zip.hash -w=/usr/share/wordlists/rockyou.txt`
```bash
┌──(kali㉿kali)-[~/…/Writeups/DeconstruCTF 2023/Snowy-Rock/_snowy_rock_fi.jpg.extracted]
└─$ john zip.hash -w=/usr/share/wordlists/rockyou.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
Will run 4 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
11snowbird       (3CA15.zip/snowyrock.txt)     
1g 0:00:00:01 DONE (2023-08-07 15:16) 0.6666g/s 8918Kp/s 8918Kc/s 8918KC/s 1208417808..11ppt06895s
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```
* We get the password as `11snowbird`
* extracting `snowyrock.txt` using the password, we find whitespaces in it  
* Stegsnow can deal with whitespaces   
`stegsnow -C snowyrock.txt`
* We get a base64 encoded string:   `OFTHA62GMFBGUX3FIJYFQZS7ONBGKX3FGM2HS7I=` which decodes to `qfp{FaBj_eBpXf_sBe_e34y}`
* Then we rot13 decode it to get the flag
```sh
┌──(kali㉿kali)-[~/…/Writeups/DeconstruCTF 2023/Snowy-Rock/_snowy_rock_fi.jpg.extracted]
└─$ echo "qfp{FaBj_eBpXf_sBe_e34y}" | rot13   
dsc{SnOw_rOcKs_fOr_r34l}
```
* FLAG:  
`dsc{SnOw_rOcKs_fOr_r34l}`
