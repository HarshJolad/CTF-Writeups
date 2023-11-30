# Missing

## DESCRIPTION
> Jason todd went missing and all alfred was able to recover from his pc was this file
Help Alfred find Jason  
Author: Rakhul  
**FLAG FORMAT**:
dsc{[a-zA-Z0-9_]+}

## Solution 
* Use [this online tool](hhttps://www.lostmypass.com/file-types/rar/) and get password `1983`
* Unzip the `rar` file, we get 2 folders
* check `.git` folder in the `nothing_here_to_look_at` folder
* Check commit `f50086b592f94cc8d05f9b1dde2eeb10d6c4713c`, we get a base64 encoded string  

```base64
aHR0cHM6Ly93d3cuaW5zdGFncmFtLmNvbS90b2RkX2phc29uX3NlY3VyZS8=
```
* Base64 decode gives us an instagram profile link : `https://www.instagram.com/todd_jason_secure/`
* Stalking the instagram profile and going through the posts, we get the first part of the flag in one of the posts  
`dsc{h4vINg_FuN_w1`
* Looking up for the same username on twitter and going to the profile, there are 2 encoded strings but one of them is a fake flag and the other one gives us the 2nd half of the flag on base32 decoding
* base32 decoding the string `G5UF6TZVJFHFIX2AJZSF63JUOA2X2===` gives `7h_O5INT_@Nd_m4p5}`
* Combining both the parts gives us the flag
* FLAG:  
`dsc{h4vINg_FuN_w17h_O5INT_@Nd_m4p5}`


